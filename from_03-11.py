# import pandas as pd
import dask.dataframe as dd

df_read = dd.read_csv("CSV-03-11/03-11/LDAP.csv", dtype={'SimillarHTTP': 'object'})  # Mudar caminho do csv
df_read.compute()  # Transforma em um dataframe que pode ser usado pelo pandas


def get_columns_names():
    global df_read

    return df_read.columns


def get_data_types():
    global df_read

    return df_read.dtypes


def get_values():
    global df_read

    return df_read


def get_info():
    global df_read

    return df_read.info()


# print('#### Alguns dados ###\n', df_read.head())
# print('#### Colunas ###\n', df_chunk.columns)
# print('#### Colunas ###\n', df_chunk.dtypes)
# print('#### Informações gerais ###\n', df_read.info(verbose=False))
