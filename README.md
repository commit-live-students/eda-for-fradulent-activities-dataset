# Exploratory Data Analysis for Translation Dataset

* Company XYZ is a worldwide e-commerce site with localized versions of the site.
* A data scientist at XYZ noticed that Spain-based users have a much higher conversion rate than any other Spanish-speaking country. She therefore went and talked to the international team in charge of Spain And LatAm to see if they had any ideas about why that was happening.
* Spain and LatAm country manager suggested that one reason could be translation. All Spanish- speaking countries had the same translation of the site which was written by a Spaniard. They agreed to try a test where each country would have its one translation written by a local.
* That is, Argentinian users would see a translation written by an Argentinian, Mexican users by a Mexican and so on. Obviously, nothing would change for users from Spain.
* After they run the test however, they are really surprised cause the test is negative. I.e., it appears that the non-localized translation was doing better!

**Goal**

The goal of this challenge is to build a machine learning model that predicts the probability that the first transaction of a new user is fraudulent.

* Confirm that the test is actually negative. That is, it appears that the old version of the site with just one translation across Spain and LatAm performs better
* Explain why that might be happening. Are the localized translations really worse?
* If you identified what was wrong, design an algorithm that would return FALSE if the same problem is happening in the future and TRUE if everything is good and the results can be trusted.


**Data**

We have 2 tables.

**Table 1: "test_table" - general information about the test results**

Columns:

* user_id : the id of the user. Unique by user. Can be joined to user id in the other table. For each user, we just check whether conversion happens the first time they land on the site since the test started.
* date : when they came to the site for the first time since the test started
* source : marketing channel: Ads, SEO, Direct . Direct means everything except for ads and SEO. Such as directly typing site URL on the browser, downloading the app w/o coming from SEO or Ads, referral friend, etc.
* device : device used by the user. It can be mobile or web
* browser_language : in browser or app settings, the language chosen by the user. It can be EN, ES, Other (Other means any language except for English and Spanish)
* ads_channel : if marketing channel is ads, this is the site where the ad was displayed. It can be: Google, Facebook, Bing, Yahoo ,Other. If the user didn't come via an ad, this field is NA
* browser : user browser. It can be: IE, Chrome, Android_App, FireFox, Iphone_App, Safari, Opera
* conversion : whether the user converted (1) or not (0). This is our label. A test is considered successful if it increases the proportion of users who convert.
* test : users are randomly split into test (1) and control (0). Test users see the new translation and control the old one. For Spain-based users, this is obviously always 0 since there is no change there.


**Table 2: "user_table" - some information about the user**

Columns:

* user_id : the id of the user. It can be joined to user id in the other table
* sex : user sex: Male or Female
* age : user age (self-reported)
* country : user country based on ip address

**Question 1**

Map each user to his country based on his IP address

* Define a function with name join_dataframe
* crate two dataframes from provided csv's under data directory
* Merge them according to user id and create one dataframe.
* you have to use this dataframe as input for all below functions


**Question 2**

Function that returns a list of the names of categorical variables

* Define a function with name get_categorical_variables
* Pass dataframe as parameter (Read csv file and convert it into pandas dataframe)
* Return list of all categorical fields available.


**Question 3**

Function that returns the list of the names of numeric variables

* Define a function with name get_numerical_variables
* Pass dataframe as parameter (Read csv file and convert it into pandas dataframe)
* Return list of all numerical fields available.


**Question 4**

Function that returns, for numeric variables, mean, median, 25, 50, 75th percentile

* Define a function with name get_numerical_variables_percentile
* Pass dataframe as parameter (Read csv file and convert it into pandas dataframe)
* Return dataframe with following columns:
    * variable name
    * mean
    * median
    * 25th percentile
    * 50th percentile
    * 75th percentile


**Question 5**

For categorical variables, get modes

* Define a function with name get_categorical_variables_modes
* Pass dataframe as parameter (Read csv file and convert it into pandas dataframe)
* Return dict object with following keys:
    * converted
    * country
    * new_user
    * source


**Question 6**

For each column, list the count of missing values

* Define a function with name get_missing_values_count
* Pass dataframe as parameter (Read csv file and convert it into pandas dataframe)
* Return dataframe with following columns:
    * var_name
    * missing_value_count


**Question 7**

Plot histograms using different subplots of all the numerical values in a single plot

* Define a function with name plot_histogram_with_numerical_values
* Pass dataframe and list of columns you want to plot as parameter
* Plot the graph
* Add column names as plot names (In case you dont understand this please connect with instructor)
* Change the histogram colour to yellow
* Fit a normal curve on those histograms (In case you dont understand this please connect with instructor)


**Question 8**

Plot facet box plots to check out the distribution according to the target variable

* Define a function with name plot_facet_box
* Pass dataframe and list of columns you want to plot as parameter
* Plot the graph