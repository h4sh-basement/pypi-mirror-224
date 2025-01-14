import functools
import inspect
import logging
from types import CodeType, FunctionType, ModuleType
from typing import Any, Callable, Collection, Dict, List, Optional, Set, Tuple, Type, Union

import numpy as np
import pandas as pd
import pyspark.pandas as ps
from pyspark.sql import Column, DataFrame, dataframe, types
from pyspark.sql.functions import column, lit, pandas_udf, udf

from hamilton import base, htypes, node
from hamilton.execution import graph_functions
from hamilton.function_modifiers import base as fm_base
from hamilton.function_modifiers import subdag
from hamilton.function_modifiers.recursive import assign_namespace
from hamilton.htypes import custom_subclass_check

logger = logging.getLogger(__name__)


class KoalasDataFrameResult(base.ResultMixin):
    """Mixin for building a koalas dataframe from the result"""

    @staticmethod
    def build_result(**outputs: Dict[str, Any]) -> ps.DataFrame:
        """Right now this class is just used for signaling the return type."""
        pass


class SparkKoalasGraphAdapter(base.HamiltonGraphAdapter, base.ResultMixin):
    """Class representing what's required to make Hamilton run on Spark with Koalas, i.e. Pandas on Spark.

    This walks the graph and translates it to run onto `Apache Spark <https://spark.apache.org/">`__ \
    using the \
    `Pandas API on Spark <https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/index.html>`__

    Use `pip install sf-hamilton[spark]` to get the dependencies required to run this.

    Currently, this class assumes you're running SPARK 3.2+. You'd generally use this if you have an existing spark \
    cluster running in your workplace, and you want to scale to very large data set sizes.

    Some tips on koalas (before it was merged into spark 3.2):

     - https://databricks.com/blog/2020/03/31/10-minutes-from-pandas-to-koalas-on-apache-spark.html
     - https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/index.html

    Spark is a more heavyweight choice to scale computation for Hamilton graphs creating a Pandas Dataframe.

    Notes on scaling:
    -----------------
      - Multi-core on single machine ✅ (if you setup Spark locally to do so)
      - Distributed computation on a Spark cluster ✅
      - Scales to any size of data as permitted by Spark ✅

    Function return object types supported:
    ---------------------------------------
      - ⛔ Not generic. This does not work for every Hamilton graph.
      - ✅ Currently we're targeting this at Pandas/Koalas types [dataframes, series].

    Pandas?
    -------
      - ✅ Koalas on Spark 3.2+ implements a good subset of the pandas API. Keep it simple and you should be good to go!

    CAVEATS
    -------
      - Serialization costs can outweigh the benefits of parallelism, so you should benchmark your code to see if it's\
      worth it.

    DISCLAIMER -- this class is experimental, so signature changes are a possibility!
    """

    def __init__(self, spark_session, result_builder: base.ResultMixin, spine_column: str):
        """Constructor

        You only have the ability to return either a Pandas on Spark Dataframe or a Pandas Dataframe. To do that you \
        either use the stock \
        `base.PandasDataFrameResult <https://github.com/dagworks-inc/hamilton/blob/main/hamilton/base.py#L39>`__ class,\
         or you use `h_spark.KoalasDataframeResult <https://github.com/dagworks-inc/hamilton/blob/main/hamilton/experimental/h_spark.py#L16>`__.

        :param spark_session: the spark session to use.
        :param result_builder: the function to build the result -- currently on Pandas and Koalas are "supported".
        :param spine_column: the column we should use first as the spine and then subsequently join against.
        """
        self.spark_session = spark_session
        if not (
            isinstance(result_builder, base.PandasDataFrameResult)
            or isinstance(result_builder, KoalasDataFrameResult)
            or isinstance(result_builder, base.DictResult)
        ):
            raise ValueError(
                "SparkKoalasGraphAdapter only supports returning:"
                ' a "pandas" DF at the moment, a "koalas" DF at the moment, or a "dict" of results.'
            )
        self.result_builder = result_builder
        self.spine_column = spine_column

    @staticmethod
    def check_input_type(node_type: Type, input_value: Any) -> bool:
        """Function to equate an input value, with expected node type.

        We need this to equate pandas and koalas objects/types.

        :param node_type: the declared node type
        :param input_value: the actual input value
        :return: whether this is okay, or not.
        """
        # TODO: flesh this out more
        if (node_type == pd.Series or node_type == ps.Series) and (
            isinstance(input_value, ps.DataFrame) or isinstance(input_value, ps.Series)
        ):
            return True
        elif node_type == np.array and isinstance(input_value, dataframe.DataFrame):
            return True

        return base.SimplePythonGraphAdapter.check_input_type(node_type, input_value)

    @staticmethod
    def check_node_type_equivalence(node_type: Type, input_type: Type) -> bool:
        """Function to help equate pandas with koalas types.

        :param node_type: the declared node type.
        :param input_type: the type of what we want to pass into it.
        :return: whether this is okay, or not.
        """
        if node_type == ps.Series and input_type == pd.Series:
            return True
        elif node_type == pd.Series and input_type == ps.Series:
            return True
        elif node_type == ps.DataFrame and input_type == pd.DataFrame:
            return True
        elif node_type == pd.DataFrame and input_type == ps.DataFrame:
            return True
        return node_type == input_type

    def execute_node(self, node: node.Node, kwargs: Dict[str, Any]) -> Any:
        """Function that is called as we walk the graph to determine how to execute a hamilton function.

        :param node: the node from the graph.
        :param kwargs: the arguments that should be passed to it.
        :return: returns a koalas column
        """
        return node.callable(**kwargs)

    def build_result(self, **outputs: Dict[str, Any]) -> Union[pd.DataFrame, ps.DataFrame, dict]:
        if isinstance(self.result_builder, base.DictResult):
            return self.result_builder.build_result(**outputs)
        # we don't use the actual function for building right now, we use this hacky equivalent
        df = ps.DataFrame(outputs[self.spine_column])
        for k, v in outputs.items():
            logger.info(f"Got column {k}, with type [{type(v)}].")
            df[k] = v
        if isinstance(self.result_builder, base.PandasDataFrameResult):
            return df.to_pandas()
        else:
            return df


def numpy_to_spark_type(numpy_type: Type) -> types.DataType:
    """Function to convert a numpy type to a Spark type.

    :param numpy_type: the numpy type to convert.
    :return: the Spark type.
    :raise: ValueError if the type is not supported.
    """
    if (
        numpy_type == np.int8
        or numpy_type == np.int16
        or numpy_type == np.int32
        or numpy_type == np.int64
    ):
        return types.IntegerType()
    elif numpy_type == np.float16 or numpy_type == np.float32 or numpy_type == np.float64:
        return types.FloatType()
    elif numpy_type == np.bool_:
        return types.BooleanType()
    elif numpy_type == np.unicode_ or numpy_type == np.string_:
        return types.StringType()
    elif numpy_type == np.bytes_:
        return types.BinaryType()
    else:
        raise ValueError("Unsupported NumPy type: " + str(numpy_type))


def python_to_spark_type(python_type: Union[int, float, bool, str, bytes]) -> types.DataType:
    """Function to convert a Python type to a Spark type.

    :param python_type: the Python type to convert.
    :return: the Spark type.
    :raise: ValueError if the type is not supported.
    """
    if python_type == int:
        return types.IntegerType()
    elif python_type == float:
        return types.FloatType()
    elif python_type == bool:
        return types.BooleanType()
    elif python_type == str:
        return types.StringType()
    elif python_type == bytes:
        return types.BinaryType()
    else:
        raise ValueError("Unsupported Python type: " + str(python_type))


def get_spark_type(return_type: Any) -> types.DataType:
    if return_type in (int, float, bool, str, bytes):
        return python_to_spark_type(return_type)
    elif hasattr(return_type, "__module__") and getattr(return_type, "__module__") == "numpy":
        return numpy_to_spark_type(return_type)
    else:
        raise ValueError(
            f"Currently unsupported return type {return_type}. "
            f"Please create an issue or PR to add support for this type."
        )


def _get_pandas_annotations(node_: node.Node, bound_parameters: Dict[str, Any]) -> Dict[str, bool]:
    """Given a function, return a dictionary of the parameters that are annotated as pandas series.

    :param hamilton_udf: the function to check.
    :return: dictionary of parameter names to boolean indicating if they are pandas series.
    """
    return {
        name: type_ == pd.Series
        for name, (type_, dep_type) in node_.input_types.items()
        if name not in bound_parameters and dep_type == node.DependencyType.REQUIRED
    }


def _determine_parameters_to_bind(
    actual_kwargs: dict,
    df_columns: Set[str],
    node_input_types: Dict[str, Tuple],
    node_name: str,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Function that we use to bind inputs to the function, or determine we should pull them from the dataframe.

    It does two things:

    1. If the parameter name matches a column name in the dataframe, create a pyspark column object for it.
    2. If the parameter name matches a key in the input dictionary, and the value is not a dataframe,\
    bind it to the function.

    :param actual_kwargs: the input dictionary of arguments for the function.
    :param df_columns: the set of column names in the dataframe.
    :param hamilton_udf: the callable to bind to.
    :param node_input_types: the input types of the function.
    :param node_name: name of the node/function.
    :return: a tuple of the params that come from the dataframe and the parameters to bind.
    """
    params_from_df = {}
    bind_parameters = {}
    for input_name, (type_, dep_type) in node_input_types.items():
        if input_name in df_columns:
            params_from_df[input_name] = column(input_name)
        elif input_name in actual_kwargs and not isinstance(actual_kwargs[input_name], DataFrame):
            bind_parameters[input_name] = actual_kwargs[input_name]
        elif dep_type == node.DependencyType.REQUIRED:
            raise ValueError(
                f"Cannot satisfy {node_name} with input types {node_input_types} against a "
                f"dataframe with "
                f"columns {df_columns} and input kwargs {actual_kwargs}."
            )
    return params_from_df, bind_parameters


def _inspect_kwargs(kwargs: Dict[str, Any]) -> Tuple[DataFrame, Dict[str, Any]]:
    """Inspects kwargs, removes any dataframes, and returns the (presumed single) dataframe, with remaining kwargs.

    :param kwargs: the inputs to the function.
    :return: tuple of the dataframe and the remaining non-dataframe kwargs.
    """
    df = None
    actual_kwargs = {}
    for kwarg_key, kwarg_value in kwargs.items():
        if isinstance(kwarg_value, DataFrame):
            if df is None:
                df = kwarg_value
        else:
            actual_kwargs[kwarg_key] = kwarg_value
    return df, actual_kwargs


def _format_pandas_udf(func_name: str, ordered_params: List[str]) -> str:
    formatting_params = {
        "name": func_name,
        "return_type": "pd.Series",
        "params": ", ".join([f"{param}: pd.Series" for param in ordered_params]),
        "param_call": ", ".join([f"{param}={param}" for param in ordered_params]),
    }
    func_string = """
def {name}({params}) -> {return_type}:
    return partial_fn({param_call})
""".format(
        **formatting_params
    )
    return func_string


def _format_udf(func_name: str, ordered_params: List[str]) -> str:
    formatting_params = {
        "name": func_name,
        "params": ", ".join(ordered_params),
        "param_call": ", ".join([f"{param}={param}" for param in ordered_params]),
    }
    func_string = """
def {name}({params}):
    return partial_fn({param_call})
""".format(
        **formatting_params
    )
    return func_string


def _fabricate_spark_function(
    node_: node.Node,
    params_to_bind: Dict[str, Any],
    params_from_df: Dict[str, Any],
    pandas_udf: bool,
) -> FunctionType:
    """Fabricates a spark compatible UDF. We have to do this as we don't actually have a funtion
    with annotations to use, as its lambdas passed around by decorators. We may consider pushing
    this upstreams so that everything can generate its own function, but for now this is the
    easiest way to do it.

    The rules are different for pandas series and regular UDFs.
    Pandas series have to:
    - be Decorated with pandas_udf
    - Have a return type of a pandas series
    - Have a pandas series as the only input types
    Regular UDFs have to:
    - Have no annotations at all

    See https://spark.apache.org/docs/3.1.3/api/python/reference/api/pyspark.sql.functions.udf.html
    and https://spark.apache.org/docs/3.1.3/api/python/reference/api/pyspark.sql.functions.pandas_udf.html

    :param node_: Node to place in a spark function
    :param params_to_bind: Parameters to bind to the function -- these won't go into the UDF
    :param params_from_df: Parameters to retrieve from the dataframe
    :return: A function that can be used in a spark UDF
    """
    partial_fn = functools.partial(node_.callable, **params_to_bind)
    ordered_params = sorted(params_from_df)
    func_name = node_.name.replace(".", "_")
    if pandas_udf:
        func_string = _format_pandas_udf(func_name, ordered_params)
    else:
        func_string = _format_udf(func_name, ordered_params)
    module_code = compile(func_string, "<string>", "exec")
    func_code = [c for c in module_code.co_consts if isinstance(c, CodeType)][0]
    return FunctionType(func_code, {**globals(), **{"partial_fn": partial_fn}}, func_name)


def _lambda_udf(df: DataFrame, node_: node.Node, actual_kwargs: Dict[str, Any]) -> DataFrame:
    """Function to create a lambda UDF for a function.

    This functions does the following:

    1. Determines whether we can bind any arguments to the function, e.g. primitives.
    2. Determines what type of UDF it is, regular or Pandas, and processes the function accordingly.
    3. Determines the return type of the UDF.
    4. Creates the UDF and applies it to the dataframe.

    :param df: the spark dataframe to apply UDFs to.
    :param node_: the node representing the function.
    :param hamilton_udf: the function to apply.
    :param actual_kwargs: the actual arguments to the function.
    :return: the dataframe with one more column representing the result of the UDF.
    """
    params_from_df, params_to_bind = _determine_parameters_to_bind(
        actual_kwargs, set(df.columns), node_.input_types, node_.name
    )
    pandas_annotation = _get_pandas_annotations(node_, params_to_bind)
    if any(pandas_annotation.values()) and not all(pandas_annotation.values()):
        raise ValueError(
            f"Currently unsupported function for {node_.name} with function signature:\n{node_.input_types}."
        )
    elif all(pandas_annotation.values()):
        hamilton_udf = _fabricate_spark_function(node_, params_to_bind, params_from_df, True)
        # pull from annotation here instead of tag.
        base_type, type_args = htypes.get_type_information(node_.type)
        logger.debug("PandasUDF: %s, %s, %s", node_.name, base_type, type_args)
        if not type_args:
            raise ValueError(
                f"{node_.name} needs to be annotated with htypes.column[pd.Series, TYPE], "
                f"where TYPE could be the string name of the python type, or the python type itself."
            )
        type_arg = type_args[0]
        if isinstance(type_arg, str):
            spark_return_type = type_arg  # spark will handle converting it.
        else:
            spark_return_type = get_spark_type(type_arg)
        spark_udf = pandas_udf(hamilton_udf, spark_return_type)
    else:
        hamilton_udf = _fabricate_spark_function(node_, params_to_bind, params_from_df, False)
        logger.debug("RegularUDF: %s, %s", node_.name, node_.type)
        spark_return_type = get_spark_type(node_.type)
        spark_udf = udf(hamilton_udf, spark_return_type)
    out = df.withColumn(
        node_.name,
        spark_udf(*[_value for _name, _value in sorted(params_from_df.items())]),
    )
    return out


class PySparkUDFGraphAdapter(base.SimplePythonDataFrameGraphAdapter):
    """UDF graph adapter for PySpark.

    This graph adapter enables one to write Hamilton functions that can be executed as UDFs in PySpark.

    Core to this is the mapping of function arguments to Spark columns available in the passed in dataframe.

    This adapter currently supports:

    - regular UDFs, these are executed in a row based fashion.
    - and a single variant of Pandas UDFs: func(series+) -> series
    - can also run regular Hamilton functions, which will execute spark driver side.

    DISCLAIMER -- this class is experimental, so signature changes are a possibility!
    """

    def __init__(self):
        self.df_object = None
        self.original_schema = []
        self.call_count = 0

    @staticmethod
    def check_input_type(node_type: Type, input_value: Any) -> bool:
        """If the input is a pyspark dataframe, skip, else delegate the check."""
        if isinstance(input_value, DataFrame):
            return True
        return base.SimplePythonDataFrameGraphAdapter.check_input_type(node_type, input_value)

    @staticmethod
    def check_node_type_equivalence(node_type: Type, input_type: Type) -> bool:
        """Checks for the htype.column annotation and deals with it."""
        # Good Cases:
        # [pd.Series, int] -> [pd.Series, int]
        # pd.series -> pd.series
        # [pd.Series, int] -> int
        node_base_type, node_annotations = htypes.get_type_information(node_type)
        input_base_type, input_annotations = htypes.get_type_information(input_type)
        exact_match = node_type == input_type
        series_to_series = node_base_type == input_base_type
        if node_annotations:
            series_to_primitive = node_annotations[0] == input_base_type
        else:
            series_to_primitive = False
        return exact_match or series_to_series or series_to_primitive

    def execute_node(self, node: node.Node, kwargs: Dict[str, Any]) -> Any:
        """Given a node to execute, process it and apply a UDF if applicable.

        :param node: the node we're processing.
        :param kwargs: the inputs to the function.
        :return: the result of the function.
        """
        self.call_count += 1
        logger.debug("%s, %s", self.call_count, self.df_object)
        # get dataframe object out of kwargs
        df, actual_kwargs = _inspect_kwargs(kwargs)
        if df is None:  # there were no dataframes passed in. So regular function call.
            return node.callable(**actual_kwargs)
        if self.df_object is None:
            self.df_object = df  # this is done only once.
            self.original_schema = list(df.columns)
        logger.debug("%s, %s", self.call_count, self.df_object)
        logger.debug("%s, Before, %s", node.name, self.df_object.columns)
        schema_length = len(df.schema)
        df = _lambda_udf(self.df_object, node, actual_kwargs)
        assert node.name in df.columns, f"Error {node.name} not in {df.columns}"
        delta = len(df.schema) - schema_length
        if delta == 0:
            raise ValueError(
                f"UDF {node.name} did not add any columns to the dataframe. "
                f"Does it already exist in the dataframe?"
            )
        self.df_object = df
        logger.debug("%s, After, %s", node.name, df.columns)
        return df

    def build_result(self, **outputs: Dict[str, Any]) -> DataFrame:
        """Builds the result and brings it back to this running process.

        :param outputs: the dictionary of key -> Union[ray object reference | value]
        :return: The type of object returned by self.result_builder.
        """
        df: DataFrame = self.df_object
        output_schema = self.original_schema
        # what's in the dataframe:
        for output_name, output_value in outputs.items():
            if output_name not in output_schema:
                output_schema.append(output_name)
            if output_name in df.columns:
                continue
            else:
                df = df.withColumn(output_name, lit(output_value))
        # original schema + new columns should be the order.
        # if someone requests a column that is in the original schema we won't duplicate it.
        result = df.select(*[column(col_name) for col_name in output_schema])
        # clear state out
        self.df_object = None
        self.original_schema = []
        return result


def sparkify_node_with_udf(
    node_: node.Node,
    linear_df_dependency_name: str,
    base_df_dependency_name: str,
    base_df_dependency_param: Optional[str],
    dependent_columns_in_group: Set[str],
    dependent_columns_from_dataframe: Set[str],
) -> node.Node:
    """ """
    """Turns a node into a spark node. This does the following:
    1. Makes it take the prior dataframe output as a dependency, in
       conjunction to its current dependencies. This is so we can represent
       the "logical" plan (the UDF-dependencies) as well as
       the "physical plan" (linear, df operations)
    2. Adjusts the function to apply the specified UDF on the
       dataframe, ignoring all inputs in column_dependencies
       (which are only there to demonstrate lineage/make the DAG representative)
    3. Returns the resulting pyspark dataframe for downstream functions to use


    :param node_: Node we're sparkifying
    :param linear_df_dependency_name: Name of the linearly passed along dataframe dependency
    :param base_df_dependency_name: Name of the base (parent) dataframe dependency.
        this is only used if dependent_columns_from_dataframe is not empty
    :param base_df_dendency_param: Name of the base (parent) dataframe dependency parameter, as known
        by the node. This is only used if `dataframe_subdag_param` is provided, which means that
        dependent_columns_from_dataframe is empty.
    :param dependent_columns_in_group: Columns on which this depends in the with_columns
    :param dependent_columns_from_dataframe:  Columns on which this depends in the
        base (parent) dataframe that the with_columns is operating on
    :return:

    """

    def new_callable(
        __linear_df_dependency_name: str = linear_df_dependency_name,
        __base_df_dependency_name: str = base_df_dependency_name,
        __dependent_columns_in_group: Set[str] = dependent_columns_in_group,
        __dependent_columns_from_dataframe: Set[str] = dependent_columns_from_dataframe,
        __base_df_dependency_param: str = base_df_dependency_param,
        __node: node.Node = node_,
        **kwargs,
    ) -> ps.DataFrame:
        """This is the new function that the node will call.
        Note that this applies the hamilton UDF with *just* the input dataframe dependency,
        ignoring the rest."""
        # gather the dataframe from the kwargs
        df = kwargs[__linear_df_dependency_name]
        kwargs = {
            k: v
            for k, v in kwargs.items()
            if k not in __dependent_columns_from_dataframe
            and k not in __dependent_columns_in_group
            and k != __linear_df_dependency_name
            and k != __base_df_dependency_name
        }
        return _lambda_udf(df, node_, kwargs)

    # Just extract the dependeency type
    # TODO -- add something as a "logical" or "placeholder" dependency
    new_input_types = {
        # copy over the old ones
        **{
            dep: value
            for dep, value in node_.input_types.items()
            if dep not in dependent_columns_from_dataframe
        },
        # add the new one (from the previous)
        linear_df_dependency_name: (DataFrame, node.DependencyType.REQUIRED),
        # Then add all the others
        # Note this might clobber the linear_df_dependency_name, but they'll be the same type
        # If we have "logical" dependencies we'll want to be careful about the type
        **{
            dep: (DataFrame, node.DependencyType.REQUIRED)
            for dep, _ in node_.input_types.items()
            if dep in dependent_columns_in_group
        },
    }

    if base_df_dependency_param is not None and base_df_dependency_name in node_.input_types:
        # In this case we want to add a dependency for visualization/lineage
        new_input_types[base_df_dependency_name] = (
            DataFrame,
            node.DependencyType.REQUIRED,
        )
    if len(dependent_columns_from_dataframe) > 0:
        new_input_types[base_df_dependency_name] = (
            DataFrame,
            node.DependencyType.REQUIRED,
        )
    return node_.copy_with(callabl=new_callable, input_types=new_input_types, typ=DataFrame)


def derive_dataframe_parameter(
    param_types: Dict[str, Type], requested_parameter: str, location_name: Callable
) -> str:
    dataframe_parameters = {
        param for param, val in param_types.items() if custom_subclass_check(val, DataFrame)
    }
    if requested_parameter is not None:
        if requested_parameter not in dataframe_parameters:
            raise ValueError(
                f"Requested parameter {requested_parameter} not found in " f"{location_name}"
            )
        return requested_parameter
    if len(dataframe_parameters) == 0:
        raise ValueError(
            f"No dataframe parameters found in: {location_name}. "
            f"Received parameters: {param_types}. "
            f"@with_columns must inject a dataframe parameter into the function."
        )
    elif len(dataframe_parameters) > 1:
        raise ValueError(
            f"More than one dataframe parameter found in function: {location_name}. Please "
            f"specify the desired one with the 'dataframe' parameter in @with_columns"
        )
    return list(dataframe_parameters)[0]


def derive_dataframe_parameter_from_fn(fn: Callable, requested_parameter: str = None) -> str:
    """Utility function to grab a pyspark dataframe parameter from a function.
    Note if one is supplied it'll look for that. If none is, it will look to ensure
    that there is only one dataframe parameter in the function.

    :param fn: Function to grab the dataframe parameter from
    :param requested_parameter: If supplied, the name of the parameter to grab
    :return: The name of the dataframe parameter
    :raises ValueError: If no datframe parameter is supplied:
    - if no dataframe parameter is found, or if more than one is found
    if a requested parameter is supplied:
    - if the requested parameter is not found
    """
    sig = inspect.signature(fn)
    parameters_with_types = {param.name: param.annotation for param in sig.parameters.values()}
    return derive_dataframe_parameter(parameters_with_types, requested_parameter, fn.__qualname__)


def derive_dataframe_parameter_from_node(node_: node.Node, requested_parameter: str = None) -> str:
    """Derives the only/requested dataframe parameter from a node.

    :param node_:
    :param requested_parameter:
    :return:
    """
    types_ = {key: value[0] for key, value in node_.input_types.items()}
    originating_function_name = (
        node_.originating_functions[-1] if node_.originating_functions is not None else node_.name
    )
    return derive_dataframe_parameter(types_, requested_parameter, originating_function_name)


def prune_nodes(nodes: List[node.Node], select: Optional[List[str]] = None) -> List[node.Node]:
    """Prunes the nodes to only include those upstream from the select columns.
    Conducts a depth-first search using the nodes `input_types` field.

    If select is None, we just assume all nodes should be included.

    :param nodes: Full set of nodes
    :param select: Columns to select
    :return:  Pruned set of nodes
    """
    if select is None:
        return nodes

    node_name_map = {node_.name: node_ for node_ in nodes}
    seen_nodes = set(select)
    stack = list({node_name_map[col] for col in select if col in node_name_map})
    output = []
    while len(stack) > 0:
        node_ = stack.pop()
        output.append(node_)
        for dep in node_.input_types:
            if dep not in seen_nodes and dep in node_name_map:
                dep_node = node_name_map[dep]
                stack.append(dep_node)
            seen_nodes.add(dep)
    return output


class transforms(fm_base.NodeTransformer):
    """Decorator for spark that allows for the specification of columns to transform.
    These are columns within a specific node in a decorator, enabling the user to make use of pyspark
    transformations inside a with_columns group. Note that this will have no impact if it is not
    decorating a node inside `with_columns`.

    Note that this currently does not work with other decorators, but it definitely could.
    """

    TRANSFORM_TARGET_TAG = "hamilton.spark.target"
    TRANSFORM_COLUMNS_TAG = "hamilton.spark.columns"

    def __init__(self, *columns: str, target_parameter=None):
        super(transforms, self).__init__(target=None)
        self._columns = columns
        self._target = target_parameter

    def transform_node(
        self, node_: node.Node, config: Dict[str, Any], fn: Callable
    ) -> Collection[node.Node]:
        """Generates nodes for the `@transforms` decorator.

        This does two things, but does not fully prepare the node:
        1. It adds the columns as dependencies to the node
        2. Adds tags with relevant metadata for later use

        Note that, at this point, we don't actually know which columns will come from the
        base dataframe, and which will come from the upstream nodes. This is handled in the
        `with_columns` decorator, so for now, we need to give it enough information to topologically
        sort/assign dependencies.

        :param node_: Node to transform
        :param config: Configuration to use (unused here)
        :return:
        """
        param = derive_dataframe_parameter_from_node(node_, self._target)

        # This allows for injection of any extra parameters
        def new_fn(**kwargs):
            return node_.callable(
                **{key: value for key, value in kwargs.items() if key in node_.input_types}
            )

        # Add the upstream columns as additional dependencies
        additional_input_types = {
            param: (DataFrame, node.DependencyType.REQUIRED) for param in self._columns
        }
        node_out = node_.copy_with(
            input_types={**node_.input_types, **additional_input_types},
            callabl=new_fn,
            tags={
                transforms.TRANSFORM_TARGET_TAG: param,
                transforms.TRANSFORM_COLUMNS_TAG: self._columns,
            },
        )
        # if it returns a column, we just turn it into a withColumn expression
        if custom_subclass_check(node_.type, Column):

            def transform_output(output: Column, kwargs: Dict[str, Any]) -> DataFrame:
                return kwargs[param].withColumn(node_.name, output)

            node_out = node_out.transform_output(transform_output, DataFrame)
        return [node_out]

    def validate(self, fn: Callable):
        """Validates on the function, even though it operates on nodes. We can always loosen
        this, but for now it should help the code stay readable.

        :param fn: Function this is decorating
        :return:
        """

        derive_dataframe_parameter_from_fn(fn, self._target)

    @staticmethod
    def _extract_dataframe_params(node_: node.Node) -> List[str]:
        """Extracts the dataframe parameters from a node.

        :param node_: Node to extract from
        :return: List of dataframe parameters
        """
        return [
            key
            for key, value in node_.input_types.items()
            if custom_subclass_check(value[0], DataFrame)
        ]

    @staticmethod
    def is_default_pyspark_udf(node_: node.Node) -> bool:
        """Tells if a node is, by default, a pyspark UDF. This means:
        1. It has a single dataframe parameter
        2. That parameter name determines an upstream column name

        :param node_: Node to check
        :return: True if it functions as a default pyspark UDF, false otherwise
        """
        df_columns = transforms._extract_dataframe_params(node_)
        return len(df_columns) == 1

    @staticmethod
    def is_decorated_pyspark_udf(node_: node.Node):
        """Tells if this is a decorated pyspark UDF. This means it has been
        decorated by the `@transforms` decorator.

        :return: True if it can be run as part of a group, false otherwise
        """
        if "hamilton.spark.columns" in node_.tags and "hamilton.spark.target" in node_.tags:
            return True
        return False

    @staticmethod
    def sparkify_node(
        node_: node.Node,
        linear_df_dependency_name: str,
        base_df_dependency_name: str,
        base_df_param_name: Optional[str],
        dependent_columns_from_upstream: Set[str],
        dependent_columns_from_dataframe: Set[str],
    ) -> node.Node:
        """Transforms a pyspark node into a node that can be run as part of a `with_columns` group.

        :param node_: Node to transform
        :param linear_df_dependency_name: Dependency on continaully modified dataframe (this will enable us
        :param base_df_dependency_name:
        :param dependent_columns_in_group:
        :param dependent_columns_from_dataframe:
        :return: The final node with correct dependencies
        """
        transformation_target = node_.tags.get(transforms.TRANSFORM_TARGET_TAG)
        # These are the only dependencies that are truly necessary,
        # aside from the other ones the node already takes
        new_input_types = {
            # transform the prior dataframe
            **{col: base_df_dependency_name for col in dependent_columns_from_dataframe},
            **{transformation_target: linear_df_dependency_name},
        }
        # we can add extra ones to represent lineage, as we know the function takes in kwargs
        node_ = node_.reassign_input_names(new_input_types)
        additional_input_types = {}
        for item in dependent_columns_from_upstream:
            if item not in node_.input_types:
                additional_input_types[item] = (DataFrame, node.DependencyType.REQUIRED)

        if (
            transformation_target == base_df_param_name
            and base_df_dependency_name not in node_.input_types
        ):
            additional_input_types[base_df_dependency_name] = (
                DataFrame,
                node.DependencyType.REQUIRED,
            )
        node_ = node_.copy_with(
            input_types={**additional_input_types, **node_.input_types},
        )
        return node_


def _identify_upstream_dataframe_nodes(nodes: List[node.Node]) -> List[str]:
    """Gives the upstream dataframe name. This is the only ps.DataFrame parameter not
    produced from within the subdag.

    :param nodes: Nodes in the subdag
    :return: The name of the upstream dataframe
    """
    node_names = {node_.name for node_ in nodes}
    df_deps = set()

    for node_ in nodes:
        # In this case its a df node that is a linear dependency, so we don't count it
        # Instead we count the columns it wants, as we have not yet created them TODO --
        # consider moving this validation afterwards so we don't have to do this check
        df_dependencies = node_.tags.get(
            transforms.TRANSFORM_COLUMNS_TAG,
            [
                dep
                for dep, (type_, _) in node_.input_types.items()
                if custom_subclass_check(type_, DataFrame)
            ],
        )
        for dependency in df_dependencies:
            if dependency not in node_names:
                df_deps.add(dependency)
    return list(df_deps)


class with_columns(fm_base.NodeCreator):
    def __init__(
        self,
        *load_from: Union[Callable, ModuleType],
        initial_schema: List[str] = None,
        select: List[str] = None,
        dataframe: Optional[str] = None,
        dataframe_subdag_param: str = None,
        namespace: str = None,
        mode: str = "append",
    ):
        """Initializes a with_columns decorator for spark. This allows you to efficiently run
         groups of map operations on a dataframe, represented as pandas/primitives UDFs. This
         effectively "linearizes" compute -- meaning that a DAG of map operations can be run
         as a set of .withColumn operations on a single dataframe -- ensuring that you don't have
         to do a complex `extract` then `join` process on spark, which can be inefficient.

         Here's an example of calling it -- if you've seen `@subdag`, you should be familiar with
         the concepts:

         .. code-block:: python
         # my_module.py
         def a(a_from_df: pd.Series) -> pd.Series:
             return _process(a)

         def b(b_from_df: pd.Series) -> pd.Series:
             return _process(b)

         def a_plus_b(a_from_df: pd.Series, b_from_df: pd.Series) -> pd.Series:
             return a + b


         # the with_columns call
         @with_columns(
             load_from=[my_module], # Load from any module
             initial_schema=["a_from_df", "b_from_df"], # The initial schema of the dataframe
             select=["a", "b", "a_plus_b"], # The columns to select from the dataframe
         )
         def final_df(df: ps.DataFrame) -> ps.DataFrame:
             # process, or just return unprocessed
             ...

         You can think of the above as a series of withColumn calls on the dataframe, where the
         operations are applied in topological order. This is significantly more efficient than
         extracting out the columns, applying the maps, then operating, but *also* allows you to
         express the operations individually, making it easy to unit-test and reuse.

         Note that the operation is "append", meaning that the columns that are selected are appended
         onto the dataframe. We will likely add an option to have this be either "select" or "append"
         mode.


        :param load_from: The functions that will be used to generate the group of map operations.
        :param select: Columns to select from the transformation. If this is left blank it will
            keep all columns in the subdag.
        :param initial_schema: The initial schema of the dataframe. This is used to determine which
            upstream inputs should be taken from the dataframe, and which shouldn't. Note that, if this is
            left empty (and external_inputs is as well), we will assume that all dependencies come
            from the dataframe. This cannot be used in conjunction with external_inputs.
        :param external_inputs: All dependencies referred to within the DAG that are not part of the
            DAG itself or the upstream dataframe. Note that, if this is left empty (and initial_schema is as well),
            we will assume that all dependencies come from the dataframe. This cannot be used in conjunction
            with initial_schema.
        :param namespace: The namespace of the nodes, so they don't clash with the global namespace
            and so this can be reused. If its left out, there will be no namespace (in which case you'll want
            to be careful about repeating it/reusing the nodes in other parts of the DAG.)
        :param dataframe: The name of the dataframe that we're modifying. If not provided,
            this will assume that there is only one pyspark.DataFrame parameter to the decorated function,
            and use that if there is more than one, we will error.
        :param mode: The mode of the operation. This can be either "append" or "select".
            If it is "append", it will keep all columns in the dataframe. If it is "select",
            it will only keep the columns in the dataframe from the `select` parameter. Note that,
            if the `select` parameter is left blank, it will keep all columns in the dataframe
            that are in the subdag (as that is the behavior of the `select` parameter. This
            defaults to `append`
        """
        self.subdag_functions = subdag.collect_functions(load_from)
        self.select = select
        self.initial_schema = initial_schema
        if (dataframe_subdag_param is not None and initial_schema is not None) or (
            dataframe_subdag_param is None and initial_schema is None
        ):
            raise ValueError(
                "You must specify only one of initial_schema and "
                "dataframe_subdag_param. "
                "This is because specifying dataframe_subdag_param injects into "
                "the set of columns, allowing you to perform your own extraction"
                " from the dataframe. We then execute all columns in the sbudag"
                " in order, passing in that initial dataframe. If you want"
                " to reference columns in your code, you'll have to specify "
                "the set of initial columns, and allow the subdag decorator "
                "to inject the dataframe through. The initial columns tell "
                "us which parameters to take from that dataframe, so we can"
                "feed the right data into the right columns."
            )
        self.dataframe_subdag_param = dataframe_subdag_param
        self.namespace = namespace
        self.upstream_dependency = dataframe
        self.mode = mode

    @staticmethod
    def _prep_nodes(initial_nodes: List[node.Node]) -> List[node.Node]:
        """Prepares nodes by decorating "default" UDFs with transform.
        This allows us to use the sparkify_node function in transforms
        for both the default ones and the decorated ones.

        :param initial_nodes:
        :return:
        """
        out = []
        for node_ in initial_nodes:
            if transforms.is_default_pyspark_udf(node_):
                col = derive_dataframe_parameter_from_node(node_)
                # todo -- wire through config/function correctly
                # the col is the only dataframe paameter so it is the target node
                (node_,) = transforms(col).transform_node(node_, {}, node_.callable)
            out.append(node_)
        return out

    @staticmethod
    def create_selector_node(
        upstream_name: str, columns: List[str], node_name: str = "select"
    ) -> node.Node:
        """Creates a selector node. The sole job of this is to select just the specified columns.
        Note this is a utility function that's only called

        :param upstream_name: Name of the upstream dataframe node
        :param columns: Columns to select
        :param node_namespace: Namespace of the node
        :param node_name: Name of the node to create
        :return:
        """

        def new_callable(**kwargs) -> DataFrame:
            return kwargs[upstream_name].select(*columns)

        return node.Node(
            name=node_name,
            typ=DataFrame,
            callabl=new_callable,
            input_types={upstream_name: DataFrame},
        )

    def _validate_dataframe_subdag_parameter(self, nodes: List[node.Node], fn_name: str):
        all_upstream_dataframe_nodes = _identify_upstream_dataframe_nodes(nodes)
        initial_schema = set(self.initial_schema) if self.initial_schema is not None else set()
        candidates_for_upstream_dataframe = set(all_upstream_dataframe_nodes) - set(initial_schema)
        if (
            len(candidates_for_upstream_dataframe) > 1
            or self.dataframe_subdag_param is None
            and len(candidates_for_upstream_dataframe) > 0
        ):
            raise ValueError(
                f"We found multiple upstream dataframe parameters for function: {fn_name} decorated with "
                f"@with_columns. You specified dataframe_subdag_param={self.dataframe_subdag_param} as the upstream "
                f"dataframe parameter, which means that your subdag must have exactly {0 if self.dataframe_subdag_param is None else 1} "
                f"upstream dataframe parameters. Instead, we found the following upstream dataframe parameters: {candidates_for_upstream_dataframe}"
            )
        if self.dataframe_subdag_param is not None:
            if len(candidates_for_upstream_dataframe) == 0:
                raise ValueError(
                    f"You specified your set of UDFs to use upstream dataframe parameter: {self.dataframe_subdag_param} "
                    f"for function: {fn_name} decorated with `with_columns`, but we could not find "
                    "that parameter as a dependency of any of the nodes. Note that that dependency "
                    "must be a pyspark dataframe. If you wish, instead, to supply an initial set of "
                    "columns for the upstream dataframe and refer to those columns directly within "
                    "your UDFs, please use initial_schema instead of dataframe_subdag_param."
                )
            (upstream_dependency,) = list(candidates_for_upstream_dataframe)
            if upstream_dependency != self.dataframe_subdag_param:
                raise ValueError(
                    f"You specified your set of UDFs to use upstream dataframe parameter: {self.dataframe_subdag_param} "
                    f"for function: {fn_name} decorated with `with_columns`, but we found that parameter "
                    f"as a dependency of a node, but it was not the same as the parameter you specified. "
                    f"Instead, we found: {upstream_dependency}."
                )

    def generate_nodes(self, fn: Callable, config: Dict[str, Any]) -> List[node.Node]:
        """Generates nodes in the with_columns groups. This does the following:

        1. Collects all the nodes from the subdag functions
        2. Prunes them to only include the ones that are upstream from the select columns
        3. Sorts them topologically
        4. Creates a new node for each one, injecting the dataframe parameter into the first one
        5. Creates a new node for the final one, injecting the last node into that one
        6. Returns the list of nodes

        :param fn: Function to generate from
        :param config: Config to use for generating/collecting nodes
        :return: List of nodes that this function produces
        """
        namespace = fn.__name__ if self.namespace is None else self.namespace
        initial_nodes = subdag.collect_nodes(config, self.subdag_functions)
        transformed_nodes = with_columns._prep_nodes(initial_nodes)
        self._validate_dataframe_subdag_parameter(transformed_nodes, fn.__qualname__)
        pruned_nodes = prune_nodes(transformed_nodes, self.select)
        if len(pruned_nodes) == 0:
            raise ValueError(
                f"No nodes found upstream from select columns: {self.select} for function: "
                f"{fn.__qualname__}"
            )
        sorted_initial_nodes = graph_functions.topologically_sort_nodes(pruned_nodes)
        output_nodes = []
        inject_parameter = derive_dataframe_parameter_from_fn(fn, self.upstream_dependency)
        current_dataframe_node = inject_parameter
        # Columns that it is dependent on could be from the group of transforms created
        columns_produced_within_mapgroup = {node_.name for node_ in pruned_nodes}
        columns_passed_in_from_dataframe = (
            set(self.initial_schema) if self.initial_schema is not None else []
        )
        # Or from the dataframe passed in...
        for node_ in sorted_initial_nodes:
            # dependent columns are broken into two sets:
            # 1. Those that come from the group of transforms
            dependent_columns_in_mapgroup = {
                column for column in node_.input_types if column in columns_produced_within_mapgroup
            }
            # 2. Those that come from the dataframe
            dependent_columns_in_dataframe = {
                column for column in node_.input_types if column in columns_passed_in_from_dataframe
            }
            # In the case that we are using pyspark UDFs
            if transforms.is_decorated_pyspark_udf(node_):
                sparkified = transforms.sparkify_node(
                    node_,
                    current_dataframe_node,
                    inject_parameter,
                    self.dataframe_subdag_param,
                    dependent_columns_in_mapgroup,
                    dependent_columns_in_dataframe,
                )
            # otherwise we're using pandas/primitive UDFs
            else:
                sparkified = sparkify_node_with_udf(
                    node_,
                    current_dataframe_node,
                    inject_parameter,
                    self.dataframe_subdag_param,
                    dependent_columns_in_mapgroup,
                    dependent_columns_in_dataframe,
                )
            output_nodes.append(sparkified)
            current_dataframe_node = sparkified.name
        # We get the final node, which is the function we're using
        # and reassign inputs to be the dataframe
        if self.mode == "select":
            select_columns = (
                self.select if self.select is not None else [item.name for item in output_nodes]
            )
            select_node = with_columns.create_selector_node(
                upstream_name=current_dataframe_node, columns=select_columns, node_name="_select"
            )
            output_nodes.append(select_node)
            current_dataframe_node = select_node.name
        output_nodes = subdag.add_namespace(output_nodes, namespace)
        final_node = node.Node.from_fn(fn).reassign_input_names(
            {inject_parameter: assign_namespace(current_dataframe_node, namespace)}
        )
        return output_nodes + [final_node]

    def validate(self, fn: Callable):
        derive_dataframe_parameter_from_fn(fn, self.upstream_dependency)
