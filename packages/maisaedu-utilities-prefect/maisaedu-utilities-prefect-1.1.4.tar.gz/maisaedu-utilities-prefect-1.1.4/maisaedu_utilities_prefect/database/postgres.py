import psycopg2
import psycopg2.extras as extras
import pandas as pd
import numpy as np
import os
from psycopg2.extensions import register_adapter, AsIs

register_adapter(np.int64, AsIs)


def connect(params_dic):
    """Connect to the PostgreSQL database server"""

    conn = psycopg2.connect(params_dic)
    return conn


def insert_batch(
    conn, dbLlist, table, onconflict="", page_size=100, default_commit=True
):
    """
    Using psycopg2.extras.execute_batch() to insert the dataframe
    """

    df = pd.DataFrame(dbLlist)
    df = df.replace({np.nan: None})
    tuples = [tuple(x) for x in df.to_numpy()]
    cols = ",".join(list(df.columns))
    query_placeholders = ", ".join(["%s"] * len(list(df.columns)))

    query = "INSERT INTO %s(%s) VALUES(%s) %s" % (
        table,
        cols,
        query_placeholders,
        onconflict,
    )
    cursor = conn.cursor()

    try:
        extras.execute_batch(cursor, query, tuples, page_size)
        if default_commit:
            conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        if default_commit:
            conn.rollback()
        cursor.close()
        raise error


def copy(
    conn,
    table_name,
    copy_list,
    file_name="copy_temp_file.csv",
    copy_config=None,
    default_commit=True,
):
    if os.path.exists(file_name) and os.path.isfile(file_name):
        os.remove(file_name)

    df = pd.DataFrame(copy_list)
    if copy_config is not None:
        if copy_config["force_columns_to_int"] is not None:
            for col in copy_config["force_columns_to_int"]:
                df[col] = df[col].astype(float).astype("Int64")

    df = df.replace({np.nan: None})
    cols = ",".join(list(df.columns))
    df.to_csv(file_name, index=False, header=False, sep=";")
    cursor = conn.cursor()

    try:
        with open(file_name, encoding="utf8") as f:
            cursor.copy_expert(
                "COPY %s (%s) FROM STDIN DELIMITER as ';' NULL as ''"
                % (table_name, cols),
                f,
            )
        if default_commit:
            conn.commit()
        cursor.close()
        os.remove(file_name)
    except (Exception, psycopg2.DatabaseError) as error:
        if default_commit:
            conn.rollback()
        cursor.close()
        raise error


def select(conn, str):
    cur = conn.cursor()
    try:
        cur.execute(str)
        row = cur.fetchall()
        cur.close()
        return row
    except (Exception, psycopg2.DatabaseError) as error:
        cur.close()
        raise error


def execute(conn, str, default_commit=True):
    cur = conn.cursor()
    try:
        cur.execute(str)
        if default_commit:
            conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        if default_commit:
            conn.rollback()
        cur.close()
        raise error
