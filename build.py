import pandas as pd
import operator

def load_data_1():
    df1 = pd.read_csv("./data/test_table.csv")
    return df1.head()

def load_data_2():
    df2 = pd.read_csv("./data/user_table.csv")
    return df2.head()

def join_dataframe(df1, df2):
    merge_df = pd.merge(df1,df2,on='user_id',how='outer')
    return merge_df


def get_categorical_variables(df):
    key = []
    values = []
    dic = {}
    delta_limit = 20

    for cols in list(df.columns):
        dic[cols] = len(df[cols].unique())

    dic_sorted = sorted(dic.items(), key=operator.itemgetter(1))

    for k,v in dic_sorted:
        key.append(k)
        values.append(v)

    for i in range(len(values)-1):
        next_delta = values[i+1] - values[i] / values[i] #measure the increase in value

        if next_delta > delta_limit:
            return df[key[:i+1]]


def get_numerical_variables(df):
    df_numeric = pd.DataFrame._get_numeric_data(df)
    return list(df_numeric)


def get_numerical_variables_percentile(df):
    return df.describe().transpose()


def get_categorical_variables_modes(df):
    #print df.head()
    df_mode = df.mode()
    return df_mode


def get_missing_values_count(df):
    ans_df = pd.DataFrame(df[df.isnull()].count(), columns=['missing_value_count'])
    return ans_df


def plot_histogram_with_numerical_values(df):
    pass


def plot_facet_box(df):
    pass


df1 = load_data_1()
#print df1.head()
df2 = load_data_2()
#print df2.head()
merge_df = join_dataframe(df1, df2)
df_cat = get_categorical_variables(merge_df)
#print df_cat.head()
#df_mode = get_categorical_variables_modes(df_cat)
get_missing_values_count(merge_df)
