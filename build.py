import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns

def join_dataframe(df1, df2):
    df = pd.merge(df1, df2, on='user_id')
    return df


def get_categorical_variables(df):
    categorical_variables = ['date', 'source', 'device', 'browser_language', 'ads_channel', 'browser', 'conversion', 'test', 'sex', 'country']
    for col in categorical_variables:
        df[col] = df[col].astype('category')
    return categorical_variables


def get_numerical_variables(df):
    numerical_variables = [col for col in df.select_dtypes(include=['int64']).columns]
    return numerical_variables


def get_numerical_variables_percentile(df):
    return df.describe().T


def get_categorical_variables_modes(df):
    return df[get_categorical_variables(df)].mode()


def get_missing_values_count(df):
    return pd.DataFrame(df.isnull().sum())


def plot_histogram_with_numerical_values(df):
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=[15,6])
    sns.distplot(df['user_id'], ax=ax[0], fit=norm, kde=False, bins=10, color='yellow')
    sns.distplot(df['age'], ax=ax[1], fit=norm, kde=False, bins=10, color='yellow')
    plt.tight_layout()


def plot_facet_box(df):
    pass
