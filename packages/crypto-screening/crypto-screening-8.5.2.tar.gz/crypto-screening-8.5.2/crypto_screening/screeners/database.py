# data.py

import os
import time
import datetime as dt
from typing import Dict, Any, Optional, Union, Iterable, List, Tuple

import pandas as pd

from sqlalchemy import create_engine as _create_engine, Engine, inspect, text

from multithreading import Caller, multi_threaded_call

from crypto_screening.dataset import DATE_TIME
from crypto_screening.symbols import (
    symbol_to_parts, adjust_symbol, parts_to_symbol
)
from crypto_screening.screeners.base import BaseScreener

__all__ = [
    "insert_database_record",
    "extract_database_record",
    "validate_database_engines",
    "parts_to_database_table_name",
    "database_table_name_to_parts",
    "extract_database_tables",
    "database_file_path",
    "await_database_creation",
    "await_all_databases_creation",
    "extract_data_into_screener_dataset",
    "extract_database_length",
    "extract_database_table_record",
    "create_engine",
    "screeners_tables_names",
    "extract_database_table_names",
    "extract_database_table_parts"
]

def parts_to_database_table_name(
        name: str, exchange: str, symbol: str, interval: Optional[str] = None
) -> str:
    """
    Creates the database table name.

    :param name: The name for the data.
    :param exchange: The exchange name of the data.
    :param symbol: The symbol of the data.
    :param interval: The interval.

    :return: The table name.
    """

    return (
        f"{name}__"
        f"{exchange}__"
        f"{'_'.join(symbol_to_parts(adjust_symbol(symbol)))}__"
        f"{interval or ''}"
    )
# end parts_to_database_table_name

def database_table_name_to_parts(table: str) -> Tuple[str, str, str, Optional[str]]:
    """
    Converts the table name to the naming parts.

    :param table: The table name.

    :return: The name parts.
    """

    values = table.split("__")

    symbol = parts_to_symbol(*values[-2].split("_"))

    values.remove(values[-2])
    interval = values[-1] or None
    name = values[0]
    exchange = values[1]

    return name, exchange, symbol, interval
# end database_table_name_to_parts

def database_file_path(path: str) -> str:
    """
    Finds the name of the database file.

    :param path: The path to the database.

    :return: The file path to the database.
    """

    path = path[path.find("://") + 3:]

    if path.startswith("/"):
        path = path[1:]
    # end if

    return path
# end database_file_path

def await_database_creation(path: str) -> None:
    """
    Waits for the database to be created.

    :param path: The path to the database.
    """

    path = database_file_path(path)

    while not os.path.exists(path):
        time.sleep(0.001)
    # end while
# end await_database_creation

def await_all_databases_creation(paths: Iterable[str]) -> None:
    """
    Waits for the databases to be created.

    :param paths: The paths to the databases.
    """

    callers = [
        Caller(target=lambda: await_database_creation(path))
        for path in paths
    ]

    multi_threaded_call(callers)
# end await_all_databases_creation

def insert_database_record(
        name: str,
        exchange: str,
        symbol: str,
        dataset: pd.DataFrame,
        engine: Engine,
        interval: Optional[str] = None
) -> None:
    """
    Inserts the data into the databases.

    :param name: The name for the data.
    :param exchange: The exchange name of the data.
    :param symbol: The symbol of the data.
    :param dataset: The dataframe of the symbol.
    :param engine: The engine for the database.
    :param interval: The interval.
    """

    table = parts_to_database_table_name(
        name=name, exchange=exchange, symbol=symbol, interval=interval
    )

    location = os.path.split(database_file_path(str(engine.url)))[0]

    if location:
        os.makedirs(location, exist_ok=True)
    # end if

    dataset.to_sql(table, engine, if_exists='append', index=True)
# end insert_database_record

def extract_database_length(
        name: str,
        exchange: str,
        symbol: str,
        engine: Engine,
        interval: Optional[str] = None
) -> int:
    """
    Extracts the length of the data from the databases.

    :param name: The name for the data.
    :param exchange: The exchange name of the data.
    :param symbol: The symbol of the data.
    :param engine: The engine for the database.
    :param interval: The interval.

    :return: The returned database lengths.
    """

    table = parts_to_database_table_name(
        name=name, exchange=exchange,
        symbol=symbol, interval=interval
    )

    query = 'SELECT COUNT(' + DATE_TIME + ') FROM ' + table

    connection = engine.connect()

    size = connection.execute(text(query)).all()[0][0]

    connection.close()

    return size
# end extract_database_length

def extract_database_table_record(
        table: str,
        engine: Engine,
        length: Optional[int] = None,
        start: Optional[dt.datetime] = None
) -> pd.DataFrame:
    """
    Extracts the data from the databases.

    :param table: The table name.
    :param engine: The engine for the database.
    :param length: Yne length of the dataset to extract.
    :param start: The starting row.

    :return: The returned databases.
    """

    query = 'SELECT * FROM ' + table

    if length is not None:
        if isinstance(start, int) and (start > 0):
            length_query = f" WHERE DateTime > {start}"

        else:
            length_query = f'COUNT(*) - {length}'
        # end if

        query += (
            f' LIMIT {length} OFFSET '
            f'(SELECT {length_query} FROM  ' + table + ')'
        )

    elif isinstance(start, int) and (start > 0):
        query += f' WHERE DateTime > {start}'
    # end if

    dataset: pd.DataFrame = pd.read_sql(query, engine)

    dataset.index = pd.DatetimeIndex(dataset[DATE_TIME])
    del dataset[DATE_TIME]
    dataset.index.name = DATE_TIME

    return dataset
    # end for
# end extract_database_record

def extract_database_record(
        name: str,
        exchange: str,
        symbol: str,
        engine: Engine,
        interval: Optional[str] = None,
        length: Optional[int] = None,
        start: Optional[dt.datetime] = None
) -> pd.DataFrame:
    """
    Extracts the data from the databases.

    :param name: The name for the data.
    :param exchange: The exchange name of the data.
    :param symbol: The symbol of the data.
    :param engine: The engine for the database.
    :param length: Yne length of the dataset to extract.
    :param interval: The interval.
    :param start: The starting row.

    :return: The returned databases.
    """

    table = parts_to_database_table_name(
        name=name, exchange=exchange,
        symbol=symbol, interval=interval
    )

    return extract_database_table_record(
        table=table, engine=engine, length=length, start=start
    )
# end extract_database_record

def extract_data_into_screener_dataset(
        screener: BaseScreener,
        engine: Engine,
        length: Optional[int] = None,
        start: Optional[dt.datetime] = None
) -> None:
    """
    Extracts the data and inserts it into the screener dataset.

    :param screener: The screener object.
    :param engine: The database engine.
    :param length: The length of data to extract.
    :param start: The start index.
    """

    interval = (
        screener.interval if (
            hasattr(screener, "interval") and
            (screener.NAME == "OHLCV")
        ) else None
    )

    data = extract_database_record(
        name=screener.NAME, exchange=screener.exchange,
        symbol=screener.symbol, interval=interval, start=start,
        length=length, engine=engine
    )

    for index, row in data.iterrows():
        row = row.to_dict()

        screener.market.loc[row.pop(DATE_TIME)] = row
    # end for
# end extract_data_into_screener_dataset

TablesNameParts = Dict[str, List[Tuple[str, str, str, Optional[str]]]]

def extract_database_table_names(engine: Engine) -> List[str]:
    """
    Extracts the databases table name.

    :param engine: The database engines.

    :return: The returned databases table name.
    """

    await_database_creation(str(engine.url))

    return list(inspect(engine).get_table_names())
# end extract_database_table_names

def extract_database_table_parts(tables: Iterable[str]) -> TablesNameParts:
    """
    Extracts the databases table name.

    :param tables: The database tables.

    :return: The returned databases table name.
    """

    return {
        table: database_table_name_to_parts(table)
        for table in tables
    }
# end extract_database_table_parts

def extract_database_tables(engine: Engine) -> TablesNameParts:
    """
    Extracts the databases table name.

    :param engine: The database engines.

    :return: The returned databases table name.
    """

    await_database_creation(str(engine.url))

    return extract_database_table_parts(extract_database_table_names(engine))
# end extract_database_table_parts

Databases = Union[Iterable[str], Dict[str, Engine]]

def create_engine(database: str) -> Engine:
    """
    Creates the engine for the database.

    :param database: The path to the database.

    :return: The engine.
    """

    location = os.path.split(database_file_path(database))[0]

    if location:
        os.makedirs(location, exist_ok=True)
    # end if

    return _create_engine(database)
# end create_engine

def validate_database_engines(data: Any) -> Dict[str, Engine]:
    """
    Validates the databases.

    :param data: The databases to validate.

    :return: The database engines.
    """

    data = data or []

    if not isinstance(data, dict):
        data = {path: create_engine(path) for path in data}
    # end if

    if not all(
        isinstance(path, str) and isinstance(engine, Engine)
        for path, engine in data.items()
    ):
        raise ValueError(f"databases must be: {Databases}, not: {data}")
    # end if

    return data
# end validate_database_engines

def screeners_tables_names(screeners: Iterable[BaseScreener]) -> Dict[BaseScreener, str]:
    """
    Finds the table names for the screeners.

    :param screeners: The screener objects

    :return: The table names in the database for the screeners.
    """

    return {
        screener: parts_to_database_table_name(
            name=screener.NAME, exchange=screener.exchange,
            symbol=screener.symbol, interval=(
                screener.interval if (
                    hasattr(screener, "interval") and
                    (screener.NAME == "OHLCV")
                ) else None
            )
        ) for screener in screeners
    }
# end screeners_tables_names