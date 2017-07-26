import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

df1 = pd.read_csv('data/test_table.csv')
df2 = pd.read_csv('data/user_table.csv')

def join_dataframe(df1, df2):
    df = pd.merge(df1, df2, on='user_id')
    df['conversion'] = df['conversion'].astype('category')
    df['test'] = df['test'].astype('category')
    return df

def get_categorical_variables(df):
    return df.select_dtypes(include=['object','category'])

def get_numerical_variables(df):
    return df.select_dtypes(include=['float','int'])

def get_numerical_variables_percentile(df):
    df_tp = get_numerical_variables(df)
    return df_tp.describe().T

def get_categorical_variables_modes(df):
     categorical_df = get_categorical_variables(df)
     return categorical_df.mode()

def get_missing_values_count(df):
    return pd.DataFrame(df.isnull().sum().rename('missing_value_count')).reset_index().rename(columns={'index': 'var_name'})

def plot_histogram_with_numerical_values(df):
    plt.subplot(121)
    plt.title(df.columns[0])
    sns.distplot(df.iloc[:,0], color='yellow', fit=norm, kde=False)
    plt.subplot(122)
    plt.title(df.columns[1])
    sns.distplot(df.iloc[:,1].dropna(), color='yellow', fit=norm, kde=False)

def plot_facet_box(df):
    plt.subplot(121)
    sns.boxplot('conversion','age',data=df)
    plt.subplot(122)
    sns.boxplot('conversion','user_id',data=df)
