import pandas as pd
df1 = pd.read_csv('data/test_table.csv')
df2 = pd.read_csv('data/user_table.csv')

def join_dataframe(df1, df2):
    df = pd.merge(df1, df2, how='left', on='user_id')
    # df['age'] = df['age'].round().fillna(0.0).astype('int64')
    # df['age'] = pd.cut(df['age'],bins=10, include_lowest=True)
    return df

def get_categorical_variables(df):
    df['test'] = df['test'].astype('object')
    df['conversion'] = df['conversion'].astype('object')
    return df.select_dtypes(include=['object'])


def get_numerical_variables(df):
    return df.select_dtypes(exclude=['object'])


def get_numerical_variables_percentile(df):
    return df.select_dtypes(exclude=['object']).describe()


def get_categorical_variables_modes(df):
    return df.select_dtypes(include=['object']).mode()

def get_missing_values_count(df):
    return df.isnull()

def plot_histogram_with_numerical_values(df):
    return df.plot.hist()


def plot_facet_box(df):
    return df.plot.box()
