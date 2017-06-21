from unittest import TestCase
import pandas as pd


filepath1 = "./data/test_table.csv"
filepath2 = "./data/user_table.csv"

data_test = pd.read_csv(filepath1)
data_user = pd.read_csv(filepath2)

df_user = pd.DataFrame(data_user)
df_test = pd.DataFrame(data_test)


class TestJoin_dataframe(TestCase):
    def test_join_dataframe(self):
        from build import join_dataframe
        res = join_dataframe(df_user, df_test)
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_get_categorical_variables(self):
        from build import get_categorical_variables, join_dataframe
        df = join_dataframe(df_user, df_test)
        res = get_categorical_variables(df=df)
        self.assertTrue("country" in res)
        self.assertTrue("sex" in res)
        self.assertTrue("date" in res)
        self.assertTrue("source" in res)
        self.assertTrue("device" in res)
        self.assertTrue("browser_language" in res)
        self.assertTrue("ads_channel" in res)
        self.assertTrue("browser" in res)
        self.assertTrue("conversion" in res)
        self.assertTrue("test" in res)

    def test_get_numerical_variables(self):
        from build import get_numerical_variables, join_dataframe
        df = join_dataframe(df_user, df_test)
        res = get_numerical_variables(df=df)
        self.assertTrue("age" in res)
        self.assertTrue("user_id" in res)

    def test_get_numerical_variables_percentile(self):
        from build import get_numerical_variables_percentile, join_dataframe
        df = join_dataframe(df_user, df_test)
        res = get_numerical_variables_percentile(df=df)
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_get_categorical_variables_modes(self):
        from build import get_categorical_variables_modes, join_dataframe
        df = join_dataframe(df_user, df_test)
        res = get_categorical_variables_modes(df=df)
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_get_missing_values_count(self):
        from build import get_missing_values_count, join_dataframe
        df = join_dataframe(df_user, df_test)
        res = get_missing_values_count(df=df)
        self.assertTrue(isinstance(res, pd.DataFrame))
