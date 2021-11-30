####### CLUSTRING EXPLORATION FUNCTIONS FOR DATA FROM QCEW DATA FROM TEXASLMI.COM #######

# ------------------------------- #
# standard imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# sklearn imports
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import wrangle as w
# ------------------------------- #

def characterize_series(s):
    '''
    Takes in a series of times series data and characterizes it based on it's behavior over a specified interval
    '''
    mean_2020 = s['2020'].mean() # to use for normalization
    std_2020 = s['2020'].std() # to use for normalization
    pcnt_decrease_mar_apr = ((s['2020-03'][0] - s['2020-04'][0]) / s['2020-03'][0]) * 100 # metric
    norm_slope_mar_apr = ((s['2020-04'][0] - s['2020-03'][0]) / 1) / mean_2020 # want to have both to see which is better metric
    pcnt_increase_apr_jun = ((s['2020-06'][0] - s['2020-04'][0]) / s['2020-04'][0]) * 100 # metric
    norm_slope_apr_jun = ((s['2020-06'][0] - s['2020-04'][0]) / 2) / mean_2020 # chose to go with percent change instead
    pcnt_increase_apr_recent = ((s['2021-06'][0] - s['2020-04'][0]) / s['2020-04'][0]) * 100 # metric
    norm_slope_apr_recent = (s['2021-06'][0] - s['2020-04'][0]) / 14 # metric
    pcnt_decrease_mar_recent = ((s['2020-03'][0] - s['2021-06'][0]) / s['2020-03'][0]) * 100 # metric
    norm_slope_mar_recent = (s['2021-06'][0] - s['2020-03'][0]) / 15 # metric
    cov_2020 = mean_2020 / std_2020 # metric
    min_2020 = s['2020'].min()
    max_2020 = s['2020'].max()
    mean_2019 = s['2019'].mean()
    std_2019 = s['2019'].std()
    cov_2019 = mean_2019 / std_2019 # Used to get change in cov metric
    cov_change = cov_2019 / cov_2020 # metric
    UB = mean_2019 + 3 * std_2019
    LB = mean_2019 - 3 * std_2019
    pct_b_min = (min_2020 - LB) / (UB - LB)
    pct_b_max = (max_2020 - LB) / (UB - LB)
    bounceback = pcnt_decrease_mar_apr - pcnt_increase_apr_jun
    characteristic_dict = {
        'pcnt_decrease_mar_apr' : pcnt_decrease_mar_apr, # measure of drop after shut down
#         'norm_slope_mar_apr' : norm_slope_mar_apr, # alternate measure of drop after shut down
#         'pcnt_increase_apr_jun' : pcnt_increase_apr_jun, # measure of immediate recovery after initial drop
        'norm_slope_apr_jun' : norm_slope_apr_jun, # alternate measure of immediate recovery after initial drop
#         'pcnt_increase_apr_recent' : pcnt_increase_apr_recent, # measure of longer-term recovery
#         'norm_slope_apr_recent' : norm_slope_apr_recent, # alternate measure of longer-term recovery
#         'pcnt_decrease_mar_recent' : pcnt_decrease_mar_recent, # measure of longer-term recovery for those that didn't have big drop and haven't recovered much
#         'norm_slope_mar_recent' : norm_slope_mar_recent, # alternate measure of above
        'cov_2020' : cov_2020, # measure of shake up due to COVID
#         'cov_2019' : cov_2019, # measure of variation pre-pandemic
#         'cov_change' : cov_change, # measure of change in variation due to pandemic
        'pct_b_min' : pct_b_min, # measure of min compared to 2019 data
        'pct_b_max' : pct_b_max, # measure of max compared to 2019 data
#         'bounceback' : bounceback # single metric to measure bounceback
    }
    return characteristic_dict

def create_char_df(industry_df_dict, ind_list):
    '''
    Creates a pandas df of characterstics of section of times series data
    '''
    characteristics = [] # create empty list for list of dictionaries
    for ind in ind_list: # loop through industries
        s = industry_df_dict[ind] # characterize them each using function
        characteristics.append(characterize_series(s)) # append to list of dicts
    char_df = pd.DataFrame(characteristics, index=ind_list) # convert to df
    return char_df

def scale(df, scaler):
    '''
    Takes in df and scaler of your choosing and returns df with only scaled columns
    '''
    cols = df.columns.tolist()
    new_column_names = [c + '_scaled' for c in cols]
    scaler.fit(df) # fit the scaler on the train
    df = pd.concat([df, pd.DataFrame(scaler.transform(df), columns=new_column_names, index=df.index)], axis=1) # transform
    df = df.drop(columns=cols) # drop unscaled columns
    return df

def cluster_and_plot_w_legend(scaled_char_df, char_df, df):
    '''
    Creates clusters and generates plots to visualize them with legend
    '''
    kmeans1 = KMeans(n_clusters=7, random_state=527) # create model object
    kmeans1.fit(scaled_char_df) # fit the object
    char_df['cluster_1'] = kmeans1.predict(scaled_char_df) # add cluster labels to original df
    print(char_df.cluster_1.value_counts()) # take a look at distribution of clusters
    print('\n')
    cluster_labels_dict = char_df[['cluster_1']].to_dict()['cluster_1'] # get dictionary of cluster labels for each industry
    df['Cluster'] = df.Industry.map(cluster_labels_dict) # add new column to df with labels via mapping
    df = df[df.Industry != 'Monetary Authorities-Central Bank'] # drop this since there was missing data for this industry
    df = df[df.Industry != 'Unclassified'] # drop this industry since it is a catchall and is noise for model
    df.Cluster = df.Cluster.astype('int') # cast as int
    cluster_list = df.Cluster.value_counts().index.tolist() # create list of clusters
    cluster_df_dict = {} # create empty dictionary for subset dfs for each cluster
    for clust in cluster_list: # loop through list of cluster labels
        cluster_df_dict[clust] = df[df.Cluster == clust] # add dfs to dictionary
    for clust in cluster_list: # plot industries for each cluster on same chart
        ind_list = cluster_df_dict[clust].Industry.value_counts().index.tolist() # create list of industries present in this specific cluster
        industry_df_dict = {} # create empty dictionary to house dfs for each industry df from each cluster
        for ind in ind_list:
            industry_df_dict[ind] = cluster_df_dict[clust][cluster_df_dict[clust].Industry == ind] # add dfs for each industry present in each cluster to dictionary
        for ind in ind_list:
            industry_df_dict[ind][['Date', 'Total Employment']].set_index('Date')['Total Employment'].sort_index().plot(label=ind) # plot each industry
        plt.gca().set(ylabel = 'Total Employment (Log Scale)', title=f'Cluster {clust}')
        plt.gca().yaxis.set_major_formatter(lambda x, pos: '{:.2f}M'.format(x / 1_000_000))
        plt.yscale('log')
        plt.legend(bbox_to_anchor= (1.03,1))
        plt.show()
    return kmeans1, char_df

def cluster_and_plot_no_legend(scaled_char_df, char_df, df):
    '''
    Creates clusters and generates plots to visualize them without legend
    '''
    kmeans1 = KMeans(n_clusters=7, random_state=527) # create model object
    kmeans1.fit(scaled_char_df) # fit the object
    char_df['cluster_1'] = kmeans1.predict(scaled_char_df) # add cluster labels to original df
    print(char_df.cluster_1.value_counts()) # take a look at distribution of clusters
    print('\n')
    cluster_labels_dict = char_df[['cluster_1']].to_dict()['cluster_1'] # get dictionary of cluster labels for each industry
    df['Cluster'] = df.Industry.map(cluster_labels_dict) # add new column to df with labels via mapping
    df = df[df.Industry != 'Monetary Authorities-Central Bank'] # drop this since there was missing data for this industry
    df = df[df.Industry != 'Unclassified'] # drop this industry since it is a catchall and is noise for model
    df.Cluster = df.Cluster.astype('int') # cast as int
    cluster_list = df.Cluster.value_counts().index.tolist() # create list of clusters
    cluster_df_dict = {} # create empty dictionary for subset dfs for each cluster
    for clust in cluster_list: # loop through list of cluster labels
        cluster_df_dict[clust] = df[df.Cluster == clust] # add dfs to dictionary
    for clust in cluster_list: # plot industries for each cluster on same chart
        ind_list = cluster_df_dict[clust].Industry.value_counts().index.tolist() # create list of industries present in this specific cluster
        industry_df_dict = {} # create empty dictionary to house dfs for each industry df from each cluster
        for ind in ind_list:
            industry_df_dict[ind] = cluster_df_dict[clust][cluster_df_dict[clust].Industry == ind] # add dfs for each industry present in each cluster to dictionary
        for ind in ind_list:
            industry_df_dict[ind][['Date', 'Total Employment']].set_index('Date')['Total Employment'].sort_index().plot() # plot each industry
        plt.gca().set(ylabel = 'Total Employment (Log Scale)', title=f'Cluster {clust}')
        plt.gca().yaxis.set_major_formatter(lambda x, pos: '{:.2f}M'.format(x / 1_000_000))
        plt.yscale('log')
        plt.show()
    return kmeans1, char_df

def acquire_to_cluster():
    df = pd.read_excel('QCEW-TX-L3.xlsx') # get raw data
    df = df[df.Ownership == 'Total All'] # filter just to all ownership groups
    df = df[['Year', 'Period', 'Industry Code', 'Industry', 'Month 1 Employment', 'Month 2 Employment', 'Month 3 Employment']] # only keep necessary columns
    df = df.melt(id_vars=['Year', 'Period', 'Industry Code', 'Industry'], var_name='Month', value_name='Total Employment') # melt columns to rows to get monthly instead of quarterly
    df['Month'] = df.Month.apply(lambda x: [int(s) for s in x.split() if s.isdigit()][0]) # pull month integer out of string
    df['Date'] = df.apply(w.extract_date, axis=1) # use function to pull out date from multiple columns
    df.Date = pd.to_datetime(df.Date) # convert data to datetime dtype
    ind_list = df.Industry.value_counts().index.tolist() # get list of industries
    ind_list.remove('Monetary Authorities-Central Bank')
    ind_list.remove('Unclassified')
    industry_df_dict = {} # create empty df for dfs for each industry
    for ind in ind_list:
        industry_df_dict[ind] = df[df.Industry == ind][['Date', 'Total Employment']].set_index('Date')['Total Employment'].sort_index()['2019' : ] # pull out series time interval
    characteristics = [] # create empty char list of dictionaries
    for ind in ind_list: # loop through industries and characterize them each using function, append to list of dicts
        s = industry_df_dict[ind]
        characteristics.append(characterize_series(s)) 
    char_df = pd.DataFrame(characteristics, index=ind_list) # convert to df
    scaled_char_df = scale(char_df, MinMaxScaler()) # scale df to use for clustering
    kmeans1 = KMeans(n_clusters=7, random_state=527)
    kmeans1.fit(scaled_char_df)
    char_df['cluster_1'] = kmeans1.predict(scaled_char_df)
    print(char_df.cluster_1.value_counts()) # take a look at distribution of clusters
    print('\n')
    cluster_labels_dict = char_df[['cluster_1']].to_dict()['cluster_1'] # get dictionary of cluster labels for each industry
    df['Cluster'] = df.Industry.map(cluster_labels_dict) # add new column to df with labels
    df = df[df.Industry != 'Monetary Authorities-Central Bank'] # need to drop this since there was missing data for this industry
    df = df[df.Industry != 'Unclassified'] # need to drop this since there was missing data for this industry
    df.Cluster = df.Cluster.astype('int') # cast as int
    cluster_list = df.Cluster.value_counts().index.tolist() # create list of clusters
    cluster_df_dict = {} # create empty dictionary for subset dfs for each cluster
    for clust in cluster_list:
        cluster_df_dict[clust] = df[df.Cluster == clust] # add dfs to dictionary
    for clust in cluster_list: # plot industries for each cluster on same chart
        ind_list = cluster_df_dict[clust].Industry.value_counts().index.tolist() # create list of industries present in this specific cluster
        industry_df_dict = {} # create empty dictionary to house dfs for each industry df from each cluster
        for ind in ind_list:
            industry_df_dict[ind] = cluster_df_dict[clust][cluster_df_dict[clust].Industry == ind] # add dfs for each industry present in each cluster to dictionary
        for ind in ind_list:
            industry_df_dict[ind][['Date', 'Total Employment']].set_index('Date')['Total Employment'].sort_index().plot(label=ind) # plot each industry
        plt.gca().set(ylabel = 'Total Employment (Log Scale)', title=f'Cluster: {clust}')
        plt.gca().yaxis.set_major_formatter(lambda x, pos: '{:.2f}M'.format(x / 1_000_000))
        plt.yscale('log')
        plt.legend(bbox_to_anchor= (1.03,1))
        plt.show()
        
## DIFFERENT FUNCTIONS FOR LOADING MODEL ##

def load_cluster_and_plot_w_legend(loaded_model, scaled_char_df, char_df, df):
    '''
    Creates clusters and generates plots to visualize them with legend
    '''
    char_df['cluster_1'] = loaded_model.predict(scaled_char_df) # add cluster labels to original df
    readable_label_dict = {
         0 : 'Moderate Negative Impact, Slow or No Recovery',
         1 : 'Moderate Negative Impact, Quick Recovery',
         2 : 'Significant Negative Impact, Mostly Recovered',
         3 : 'No Impact',
         4 : 'Minor Negative Impact, Quick Recovery',
         5 : 'Significant Negative Impact, Mostly Recovered, Highly Seasonal',
         6 : 'Positively Impacted'
         }
    char_df['cluster_1'] = char_df['cluster_1'].map(readable_label_dict)
#     print(char_df.cluster_1.value_counts()) # take a look at distribution of clusters
#     print('\n')
    cluster_labels_dict = char_df[['cluster_1']].to_dict()['cluster_1'] # get dictionary of cluster labels for each industry
    df['Cluster'] = df.Industry.map(cluster_labels_dict) # add new column to df with labels via mapping
    df = df[df.Industry != 'Monetary Authorities-Central Bank'] # drop this since there was missing data for this industry
    df = df[df.Industry != 'Unclassified'] # drop this industry since it is a catchall and is noise for model
    cluster_list = df.Cluster.value_counts().index.tolist() # create list of clusters
    cluster_df_dict = {} # create empty dictionary for subset dfs for each cluster
    for clust in cluster_list: # loop through list of cluster labels
        cluster_df_dict[clust] = df[df.Cluster == clust] # add dfs to dictionary
    for clust in cluster_list: # plot industries for each cluster on same chart
        ind_list = cluster_df_dict[clust].Industry.value_counts().index.tolist() # create list of industries present in this specific cluster
        industry_df_dict = {} # create empty dictionary to house dfs for each industry df from each cluster
        for ind in ind_list:
            industry_df_dict[ind] = cluster_df_dict[clust][cluster_df_dict[clust].Industry == ind] # add dfs for each industry present in each cluster to dictionary
        for ind in ind_list:
            industry_df_dict[ind][['Date', 'Total Employment']].set_index('Date')['Total Employment'].sort_index().plot(label=ind) # plot each industry
        plt.gca().set(ylabel = 'Total Employment (Log Scale)', title=f'{clust}')
        plt.gca().yaxis.set_major_formatter(lambda x, pos: '{:.2f}M'.format(x / 1_000_000))
        plt.yscale('log')
        plt.legend(bbox_to_anchor= (1.03,1))
        plt.show()
    return char_df

def load_cluster_and_plot_no_legend(loaded_model, scaled_char_df, char_df, df):
    '''
    Creates clusters and generates plots to visualize them without legend
    '''
    char_df['cluster_1'] = loaded_model.predict(scaled_char_df) # add cluster labels to original df
#     print(char_df.cluster_1.value_counts()) # take a look at distribution of clusters
#     print('\n')
    cluster_labels_dict = char_df[['cluster_1']].to_dict()['cluster_1'] # get dictionary of cluster labels for each industry
    df['Cluster'] = df.Industry.map(cluster_labels_dict) # add new column to df with labels via mapping
    df = df[df.Industry != 'Monetary Authorities-Central Bank'] # drop this since there was missing data for this industry
    df = df[df.Industry != 'Unclassified'] # drop this industry since it is a catchall and is noise for model
    df.Cluster = df.Cluster.astype('int') # cast as int
    cluster_list = df.Cluster.value_counts().index.tolist() # create list of clusters
    cluster_df_dict = {} # create empty dictionary for subset dfs for each cluster
    for clust in cluster_list: # loop through list of cluster labels
        cluster_df_dict[clust] = df[df.Cluster == clust] # add dfs to dictionary
    for clust in cluster_list: # plot industries for each cluster on same chart
        ind_list = cluster_df_dict[clust].Industry.value_counts().index.tolist() # create list of industries present in this specific cluster
        industry_df_dict = {} # create empty dictionary to house dfs for each industry df from each cluster
        for ind in ind_list:
            industry_df_dict[ind] = cluster_df_dict[clust][cluster_df_dict[clust].Industry == ind] # add dfs for each industry present in each cluster to dictionary
        for ind in ind_list:
            industry_df_dict[ind][['Date', 'Total Employment']].set_index('Date')['Total Employment'].sort_index().plot() # plot each industry
        plt.gca().set(ylabel = 'Total Employment (Log Scale)', title=f'Cluster {clust}')
        plt.gca().yaxis.set_major_formatter(lambda x, pos: '{:.2f}M'.format(x / 1_000_000))
        plt.yscale('log')
        plt.show()
    return char_df

def load_acquire_to_cluster(loaded_model):
    df = pd.read_excel('QCEW-TX-L3.xlsx') # get raw data
    df = df[df.Ownership == 'Total All'] # filter just to all ownership groups
    df = df[['Year', 'Period', 'Industry Code', 'Industry', 'Month 1 Employment', 'Month 2 Employment', 'Month 3 Employment']] # only keep necessary columns
    df = df.melt(id_vars=['Year', 'Period', 'Industry Code', 'Industry'], var_name='Month', value_name='Total Employment') # melt columns to rows to get monthly instead of quarterly
    df['Month'] = df.Month.apply(lambda x: [int(s) for s in x.split() if s.isdigit()][0]) # pull month integer out of string
    df['Date'] = df.apply(w.extract_date, axis=1) # use function to pull out date from multiple columns
    df.Date = pd.to_datetime(df.Date) # convert data to datetime dtype
    ind_list = df.Industry.value_counts().index.tolist() # get list of industries
    ind_list.remove('Monetary Authorities-Central Bank')
    ind_list.remove('Unclassified')
    industry_df_dict = {} # create empty df for dfs for each industry
    for ind in ind_list:
        industry_df_dict[ind] = df[df.Industry == ind][['Date', 'Total Employment']].set_index('Date')['Total Employment'].sort_index()['2019' : ] # pull out series time interval
    characteristics = [] # create empty char list of dictionaries
    for ind in ind_list: # loop through industries and characterize them each using function, append to list of dicts
        s = industry_df_dict[ind]
        characteristics.append(characterize_series(s)) 
    char_df = pd.DataFrame(characteristics, index=ind_list) # convert to df
    scaled_char_df = scale(char_df, MinMaxScaler()) # scale df to use for clustering
    char_df['cluster_1'] = loaded_model.predict(scaled_char_df)
    readable_label_dict = {
         0 : 'Moderate Negative Impact, Slow or No Recovery',
         1 : 'Moderate Negative Impact, Quick Recovery',
         2 : 'Significant Negative Impact, Mostly Recovered',
         3 : 'No Impact',
         4 : 'Minor Negative Impact, Quick Recovery',
         5 : 'Significant Negative Impact, Mostly Recovered, Highly Seasonal',
         6 : 'Positively Impacted'
         }
    char_df['cluster_1'] = char_df['cluster_1'].map(readable_label_dict)
#     print(char_df.cluster_1.value_counts()) # take a look at distribution of clusters
#     print('\n')
    cluster_labels_dict = char_df[['cluster_1']].to_dict()['cluster_1'] # get dictionary of cluster labels for each industry
    df['Cluster'] = df.Industry.map(cluster_labels_dict) # add new column to df with labels
    df = df[df.Industry != 'Monetary Authorities-Central Bank'] # need to drop this since there was missing data for this industry
    df = df[df.Industry != 'Unclassified'] # need to drop this since there was missing data for this industry
    cluster_list = df.Cluster.value_counts().index.tolist() # create list of clusters
    cluster_df_dict = {} # create empty dictionary for subset dfs for each cluster
    for clust in cluster_list:
        cluster_df_dict[clust] = df[df.Cluster == clust] # add dfs to dictionary
    for clust in cluster_list: # plot industries for each cluster on same chart
        ind_list = cluster_df_dict[clust].Industry.value_counts().index.tolist() # create list of industries present in this specific cluster
        industry_df_dict = {} # create empty dictionary to house dfs for each industry df from each cluster
        for ind in ind_list:
            industry_df_dict[ind] = cluster_df_dict[clust][cluster_df_dict[clust].Industry == ind] # add dfs for each industry present in each cluster to dictionary
        for ind in ind_list:
            industry_df_dict[ind][['Date', 'Total Employment']].set_index('Date')['Total Employment'].sort_index().plot(label=ind) # plot each industry
        plt.gca().set(ylabel = 'Total Employment (Log Scale)', title=f'{clust}')
        plt.gca().yaxis.set_major_formatter(lambda x, pos: '{:.2f}M'.format(x / 1_000_000))
        plt.yscale('log')
        plt.legend(bbox_to_anchor= (1.03,1))
        plt.show()

def load_acquire_to_cluster_lines(loaded_model):
    df = pd.read_excel('QCEW-TX-L3.xlsx') # get raw data
    df = df[df.Ownership == 'Total All'] # filter just to all ownership groups
    df = df[['Year', 'Period', 'Industry Code', 'Industry', 'Month 1 Employment', 'Month 2 Employment', 'Month 3 Employment']] # only keep necessary columns
    df = df.melt(id_vars=['Year', 'Period', 'Industry Code', 'Industry'], var_name='Month', value_name='Total Employment') # melt columns to rows to get monthly instead of quarterly
    df['Month'] = df.Month.apply(lambda x: [int(s) for s in x.split() if s.isdigit()][0]) # pull month integer out of string
    df['Date'] = df.apply(w.extract_date, axis=1) # use function to pull out date from multiple columns
    df.Date = pd.to_datetime(df.Date) # convert data to datetime dtype
    ind_list = df.Industry.value_counts().index.tolist() # get list of industries
    ind_list.remove('Monetary Authorities-Central Bank')
    ind_list.remove('Unclassified')
    industry_df_dict = {} # create empty df for dfs for each industry
    for ind in ind_list:
        industry_df_dict[ind] = df[df.Industry == ind][['Date', 'Total Employment']].set_index('Date')['Total Employment'].sort_index()['2019' : ] # pull out series time interval
    characteristics = [] # create empty char list of dictionaries
    for ind in ind_list: # loop through industries and characterize them each using function, append to list of dicts
        s = industry_df_dict[ind]
        characteristics.append(characterize_series(s)) 
    char_df = pd.DataFrame(characteristics, index=ind_list) # convert to df
    scaled_char_df = scale(char_df, MinMaxScaler()) # scale df to use for clustering
    char_df['cluster_1'] = loaded_model.predict(scaled_char_df)
    readable_label_dict = {
         0 : 'Moderate Negative Impact, Slow or No Recovery',
         1 : 'Moderate Negative Impact, Quick Recovery',
         2 : 'Significant Negative Impact, Mostly Recovered',
         3 : 'No Impact',
         4 : 'Minor Negative Impact, Quick Recovery',
         5 : 'Significant Negative Impact, Mostly Recovered, Highly Seasonal',
         6 : 'Positively Impacted'
         }
    char_df['cluster_1'] = char_df['cluster_1'].map(readable_label_dict)
#     print(char_df.cluster_1.value_counts()) # take a look at distribution of clusters
#     print('\n')
    cluster_labels_dict = char_df[['cluster_1']].to_dict()['cluster_1'] # get dictionary of cluster labels for each industry
    df['Cluster'] = df.Industry.map(cluster_labels_dict) # add new column to df with labels
    df = df[df.Industry != 'Monetary Authorities-Central Bank'] # need to drop this since there was missing data for this industry
    df = df[df.Industry != 'Unclassified'] # need to drop this since there was missing data for this industry
    cluster_list = df.Cluster.value_counts().index.tolist() # create list of clusters
    cluster_df_dict = {} # create empty dictionary for subset dfs for each cluster
    for clust in cluster_list:
        cluster_df_dict[clust] = df[df.Cluster == clust] # add dfs to dictionary
    for clust in cluster_list: # plot industries for each cluster on same chart
        ind_list = cluster_df_dict[clust].Industry.value_counts().index.tolist() # create list of industries present in this specific cluster
        industry_df_dict = {} # create empty dictionary to house dfs for each industry df from each cluster
        for ind in ind_list:
            industry_df_dict[ind] = cluster_df_dict[clust][cluster_df_dict[clust].Industry == ind] # add dfs for each industry present in each cluster to dictionary
        for ind in ind_list:
            industry_df_dict[ind][['Date', 'Total Employment']].set_index('Date')['Total Employment'].sort_index()['2018' : ].plot(label=ind) # plot each industry
        plt.gca().set(ylabel = 'Total Employment (Log Scale)', title=f'{clust}')
        # plt.vlines(x='2020-03', ymin=-1, ymax=12, linestyles='--', colors='darkorange', label='November 2021')
        plt.gca().axvline(x='2020-03', color = 'red', linestyle = '--', label='March 2020')
        plt.gca().yaxis.set_major_formatter(lambda x, pos: '{:.2f}M'.format(x / 1_000_000))
        plt.yscale('log')
        plt.legend(bbox_to_anchor= (1.03,1))
        plt.show()


#### Explore files for the Census Data:

# Function to calculate 2020 Q1 minus Q3 Job Loss
def q1_minus_q3_emp(census_light):
    '''This function will calculate job loss duering COVID shut downs.
    So, 2020 Q1 Employment minus Q3 Employment'''
        # Top 10 Job loss by industry of 2020 using q1 Emp minus q3 Emp:
    q1 = census_light[['industry', 'industry_name', 'Emp', 'date']][census_light.date == '2020-01-01']
    q3 = census_light[['industry', 'industry_name', 'Emp', 'date']][census_light.date == '2020-07-01']

        # match indexes so that I can subtract the quarterly columns
    q1.set_index('industry', drop=True, inplace=True)
    q3.set_index('industry', drop=True, inplace=True)

        # Subtract 2020 q1 - q3 employment:
    q1_minus_q3 = q1.Emp - q3.Emp

        # Add q3 numbers to the datafram for ease of comparison if needed:
    q1['q3_Emp'] = q3.Emp

        # Create the difference column:
    q1['q1_minus_q3'] = q1_minus_q3

        # Rename to q since the dataframe now contains q1 and q3 data:
    q = q1

        # Sort
    q = q.sort_values('q1_minus_q3', ascending=False)

    return q

# Function that creates a new dataframe with select industries 
def select_industries(df, first_industry, list_of_remaining_industries):
    '''This function creates a dataframe out of the census data
    for only the selected industries'''
        # Use one of the industries to initiate the dataframe:
    df_new = df[df.industry == first_industry]
        # Loop through the remaining industries to combine all industries
    for industry in list_of_remaining_industries:
        industry_loss = df[df.industry == industry]
        df_new = pd.concat([df_new, industry_loss], ignore_index=True)

    return df_new