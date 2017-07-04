import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

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
    return pd.concat([df.describe(), pd.DataFrame(df.median().rename('median')).T])


def get_categorical_variables_modes(df):
    df_cat = get_categorical_variables(df)
    return pd.DataFrame(df_cat.mode().rename(index={0:'mode'})).T


def get_missing_values_count(df):
    return pd.DataFrame(df.isnull().sum().rename('missing_value_count')).reset_index().rename(columns={'index': 'var_name'})

def plot_histogram_with_numerical_values(df):
    plt.subplot(121)
    plt.title(df_num.columns[0])
    sns.distplot(df_num.iloc[:,0], color='yellow', fit=norm, kde=False)
    plt.subplot(122)
    plt.title(df_num.columns[1])
    sns.distplot(df_num.iloc[:,1].dropna(), color='yellow', fit=norm, kde=False)

def plot_facet_box(df):
    plt.subplot(121)
    sns.boxplot('conversion','age',data=df)
    plt.subplot(122)
    sns.boxplot('conversion','user_id',data=df)
