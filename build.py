import numpy as np
import pandas as pd
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt



def load_data_1():
    df1 = pd.read_csv("./data/test_table.csv")
    return df1.head()

def load_data_2():
    df2 = pd.read_csv("./data/user_table.csv")
    return df2.head()

def join_dataframe(df1, df2):
    df = pd.merge(df1,df2,on='user_id',how='outer')
    return df

def get_categorical_variables(df):
    categorical_data = list(df[['country', 'sex', 'date', 'source', 'device', 'browser_language', 'test', 'conversion', 'browser', 'ads_channel' ]])
    return categorical_data

def get_numerical_variables(df):
    numeric = pd.DataFrame._get_numeric_data(df)
    return list(numeric)

def get_numerical_variables_percentile(df):
    per = df.describe().T
    return per


def get_categorical_variables_modes(df):
    return df[get_categorical_variables(df)].mode()

def get_missing_values_count(df):
    return pd.DataFrame(df.isnull().sum())


def plot_histogram_with_numerical_values(df):

    num_cols = get_numerical_variables(df)
    plt.figure(figsize=(15,6))

    plt.subplot(221)
    plt.title(num_cols[0])
    sns.distplot(df[num_cols[0]], color='Blue', fit=norm, kde=False)

    plt.subplot(222)
    plt.title(num_cols[1])
    sns.distplot(df[num_cols[1]], color='Blue', fit=norm, kde=False)

    plt.subplot(223)
    plt.title(num_cols[2])
    sns.distplot(df[num_cols[2]], color='Blue', fit=norm, kde=False)

    plt.subplot(224)
    plt.title(num_cols[3])
    sns.distplot(df[num_cols[3]], color='Blue', fit=norm, kde=False)

    plt.tight_layout()
    plt.show()

def plot_facet_box(df):

    num_cols = get_numerical_variables(df)
    plt.figure(figsize=(10,10))

    plt.subplot(221)
    plt.title(num_cols[0])
    sns.boxplot(df[num_cols[0]], data=df)

    plt.subplot(222)
    plt.title(num_cols[1])
    sns.boxplot(df[num_cols[1]], data=df)

    plt.subplot(223)
    plt.title(num_cols[2])
    sns.boxplot(df[num_cols[2]], data=df)

    plt.subplot(224)
    plt.title(num_cols[3])
    sns.boxplot(df[num_cols[3]], data=df)

    plt.tight_layout()
    plt.show()
