# import pandas as pd
import dask.dataframe as dd

df_read = dd.read_csv("CSV-03-11/03-11/LDAP.csv")
df_read.compute()


def get_columns_names():
    global df_read

    return df_read.columns


def get_data_types():
    global df_read
    
    return df_read.dtypes


def get_values():
    global df_read

    return df_read


# print('#### Alguns dados ###\n', df_read.head())
# print('#### Colunas ###\n', df_chunk.columns)
# print('#### Colunas ###\n', df_chunk.dtypes)
# print('#### Informações gerais ###\n', df_read.info(verbose=False))

print(get_values())
