'''
This file will store scripts for acquiring and cleaning the Quarterly Workforce Indicators (QWI)
Census data for the State of Texas. 
'''

# Imports --------------------------------------------------------------------------------------
import pandas as pd
from datetime import datetime


# Functions ------------------------------------------------------------------------------------

#### Function to create a timeseries column:

def quarterly_dates(df):
    '''Takes in a dataframe with a year and a quarter column 
    and then combines them into a datetime timeseries column'''       
        # Adding a column with month number to represent the begining of a quarter year:
    df['first_month_qtr'] = df.quarter.apply(lambda x: '1' if x==1 
                                                             else '4' if x==2 
                                                             else '7' if x==3
                                                             else '10')
        # Combining month and year into a single column:
    df['quarterly'] = df.year.astype('string') + '-' + df.first_month_qtr.astype('string')
        # Transforming the month/year into datetime format:
    df['date'] = pd.to_datetime(df.quarterly)
        # Dropping the 'first_month_qtr' and 'quarterly' columns:
    col_to_drop = ['first_month_qtr', 'quarterly']
    df = df.drop(columns=col_to_drop)
    return df


#### Function to Clean the Texas Census Data with no Subgroups:

def wrangle_census_data():
    '''This function will take in a specific file with QWI data
    for the state of Texas. It will then clean the dataframe by 
    removing unneeded columns, and renaming a column in preparation 
    for exploration.'''
        # Read the CSV file:
    census = pd.read_csv('census_data_overview.csv')
        # List of columns that need to be dropped:
    col_to_drop = ['sEmp', 'sSep', 'sSepBeg', 'sSepBegR', 'periodicity', 'periodicity_label.value',
               'seasonadj', 'seasonadj_label.value', 'geo_level', 'geo_level_label.value', 
               'geography', 'geography_label.value', 'ind_level', 'sex', 'ownercode',
               'ownercode_label.value', 'sex_label.value', 'agegrp_label.value', 'race_label.value',
               'ethnicity_label.value', 'education_label.value', 'firmage_label.value', 'firmsize_label.value',
               'agegrp', 'race', 'ethnicity',  'education', 'firmage', 'firmsize', ]
        # Drop the list of columns:
    census_light = census.drop(columns=col_to_drop)
        # Renaming:
    census_light = census_light.rename(columns={'industry_label.value': 'industry_name'})  
        # Adding quarters (i.e. quarter years) as a datetime format:
    census_light = quarterly_dates(census_light)
    return census_light  
        

#### Function to Clean the Texas Census Data with Education Subgroups:    
    
def education_census_data():
    '''This function will take in a specific file with QWI education 
    data for the state of Texas. It will then clean the dataframe by 
    removing unneeded columns, and renaming a column in preparation 
    for exploration.'''
        # Read the CSV file:
    census = pd.read_csv('LaborMarketWEducation.csv')
        # List of columns that need to be dropped:
    col_to_drop = ['sEmp', 'sSep', 'periodicity', 'periodicity_label.value',
               'seasonadj', 'seasonadj_label.value', 'geo_level', 'geo_level_label.value', 
               'geography', 'geography_label.value', 'ind_level', 'ownercode', 'HirA',
               'ownercode_label.value', 'agegrp_label.value', 'race_label.value',
               'ethnicity_label.value', 'firmage_label.value', 'firmsize_label.value',
               'agegrp', 'race', 'ethnicity', 'firmage', 'firmsize', 
               'FrmJbGn', 'FrmJbLs', 'EarnBeg', 'Payroll', 'sHirA', 'sFrmJbGn', 'sFrmJbLs', 'sEarnBeg', 'sPayroll']
        # Drop the list of columns:
    census_light = census.drop(columns=col_to_drop)
        # Renaming:
    census_light = census_light.rename(columns={'industry_label.value': 'industry_name'})  
        # Adding quarters (i.e. quarter years) as a datetime format:
    census_light = quarterly_dates(census_light)
    return census_light     
    
    
#### Function to Clean the Texas Census Data with Age Subgroups: 

def age_census_data():
    '''This function will take in a specific file with QWI education 
    data for the state of Texas. It will then clean the dataframe by 
    removing unneeded columns, and renaming a column in preparation 
    for exploration.'''
        # Read the CSV file:
    census = pd.read_csv('LaborMarketWAge.csv')
        # List of columns that need to be dropped:
    col_to_drop = ['sEmp', 'sSep', 'periodicity', 'periodicity_label.value',
               'seasonadj', 'seasonadj_label.value', 'geo_level', 'geo_level_label.value', 
               'geography', 'geography_label.value', 'ind_level', 'ownercode', 'HirA',
               'ownercode_label.value', 'race_label.value', 'agegrp', 'education', 'education_label.value',
               'ethnicity_label.value', 'firmage_label.value', 'firmsize_label.value',
               'race', 'ethnicity', 'firmage', 'firmsize', 'FrmJbC', 'HirAEndReplR', 'sFrmJbC', 'sHirAEndReplR',
               'FrmJbGn', 'FrmJbLs', 'EarnBeg', 'Payroll', 'sHirA', 'sFrmJbGn', 'sFrmJbLs', 'sEarnBeg', 'sPayroll']
        # Drop the list of columns:
    census_light = census.drop(columns=col_to_drop)
        # Renaming:
    census_light = census_light.rename(columns={'industry_label.value': 'industry_name'})  
        # Adding quarters (i.e. quarter years) as a datetime format:
    census_light = quarterly_dates(census_light)
    return census_light 


#### Function to Clean the Texas Census Data with education Subgroups: 

def race_census_data():
    '''This function will take in a specific file with QWI education 
    data for the state of Texas. It will then clean the dataframe by 
    removing unneeded columns, and renaming a column in preparation 
    for exploration.'''
        # Read the CSV file:
    census = pd.read_csv('LaborMarketWRace.csv')
        # List of columns that need to be dropped:
    col_to_drop = ['sEmp', 'sSep', 'periodicity', 'periodicity_label.value',
               'seasonadj', 'seasonadj_label.value', 'geo_level', 'geo_level_label.value', 
               'geography', 'geography_label.value', 'ind_level', 'ownercode', 'HirA',
               'ownercode_label.value', 'agegrp_label.value', 'FrmJbC', 'HirAEndReplR', 
               'firmage_label.value', 'firmsize_label.value', 'sFrmJbC', 'sHirAEndReplR',
               'agegrp', 'firmage', 'firmsize', 'education', 'education_label.value',
               'FrmJbGn', 'FrmJbLs', 'EarnBeg', 'Payroll', 'sHirA', 'sFrmJbGn', 'sFrmJbLs', 'sEarnBeg', 'sPayroll']
        # Drop the list of columns:
    census_light = census.drop(columns=col_to_drop)
        # Renaming:
    census_light = census_light.rename(columns={'industry_label.value': 'industry_name'})  
        # Adding quarters (i.e. quarter years) as a datetime format:
    census_light = quarterly_dates(census_light)
    return census_light 
    

    
####### WRANGLE FUNCTIONS FOR DATA FROM QCEW DATA FROM TEXASLMI.COM #######
        
def extract_date(df):
    '''
    Takes each row of df and creates a date column for the observation based on values in two different columns
    '''
    if (df[1] == 1) & (df[4] == 1): # first quarter, first month
        return str(df[0]) + '-' + '01' # January
    elif (df[1] == 1) & (df[4] == 2): # first quarter, second month
        return str(df[0]) + '-' + '02' # February
    elif (df[1] == 1) & (df[4] == 3): # etc.
        return str(df[0]) + '-' + '03'
    elif (df[1] == 2) & (df[4] == 1):
        return str(df[0]) + '-' + '04'
    elif (df[1] == 2) & (df[4] == 2):
        return str(df[0]) + '-' + '05'
    elif (df[1] == 2) & (df[4] == 3):
        return str(df[0]) + '-' + '06'
    elif (df[1] == 3) & (df[4] == 1):
        return str(df[0]) + '-' + '07'
    elif (df[1] == 3) & (df[4] == 2):
        return str(df[0]) + '-' + '08'
    elif (df[1] == 3) & (df[4] == 3):
        return str(df[0]) + '-' + '09'
    elif (df[1] == 4) & (df[4] == 1):
        return str(df[0]) + '-' + '10'
    elif (df[1] == 4) & (df[4] == 2):
        return str(df[0]) + '-' + '11'
    elif (df[1] == 4) & (df[4] == 3):
        return str(df[0]) + '-' + '12'
    
def get_tx_data():
    '''
    Reads in raw data, filters, melts some columns to rows to get monthly observations, and creates datetime index
    '''
    df = pd.read_excel('QCEW-TX-L3.xlsx') # get raw data
    df = df[df.Ownership == 'Total All'] # filter just to all ownership groups
    df = df[['Year', 'Period', 'Industry Code', 'Industry', 'Month 1 Employment', 'Month 2 Employment', 'Month 3 Employment']] # only keep necessary columns
    df = df.melt(id_vars=['Year', 'Period', 'Industry Code', 'Industry'], var_name='Month', value_name='Total Employment') # melt columns to rows to get monthly instead of quarterly
    df['Month'] = df.Month.apply(lambda x: [int(s) for s in x.split() if s.isdigit()][0]) # pull month integer out of string
    df['Date'] = df.apply(extract_date, axis=1) # use function to pull out date from multiple columns
    df.Date = pd.to_datetime(df.Date) # convert data to datetime dtype
    return df

def create_df_dict(df):
    '''
    Takes in df and creates a dictionary of series for all industries and the time interval we are interested in
    '''
    ind_list = df.Industry.value_counts().index.tolist() # get list of industries
    ind_list.remove('Monetary Authorities-Central Bank') # remove this industry since it has missing data
    ind_list.remove('Unclassified') # remove this industry since it is a catchall for a lot of unique industries that would be noise for our clustering
    industry_df_dict = {} # create empty df for dfs for each industry
    for ind in ind_list:
        industry_df_dict[ind] = df[df.Industry == ind][['Date', 'Total Employment']].set_index('Date')['Total Employment'].sort_index()['2019' : ] # pull out series
    return industry_df_dict, ind_list

def get_tx_forecasting_data():
    '''
    Reads in raw data, filters, melts some columns to rows to get monthly observations, and creates datetime index
    '''
    df = pd.read_excel('QCEW-TX-L3-2016.xlsx') # get raw data
    df = df[['Year', 'Period', 'Industry Code', 'Industry', 'Month 1 Employment', 'Month 2 Employment', 'Month 3 Employment']] # only keep necessary columns
    df = df.melt(id_vars=['Year', 'Period', 'Industry Code', 'Industry'], var_name='Month', value_name='Total Employment') # melt columns to rows to get monthly instead of quarterly
    df['Month'] = df.Month.apply(lambda x: [int(s) for s in x.split() if s.isdigit()][0]) # pull month integer out of string
    df['Date'] = df.apply(extract_date, axis=1) # use function to pull out date from multiple columns
    df.Date = pd.to_datetime(df.Date) # convert data to datetime dtype
    return df

def create_df_dict_forecasting(df):
    '''
    Takes in df and creates a dictionary of series for all industries and the time interval we are interested in
    '''
    ind_list = df.Industry.value_counts().index.tolist() # get list of industries
    ind_list.remove('Monetary Authorities-Central Bank') # remove this industry since it has missing data
    ind_list.remove('Unclassified') # remove this industry since it is a catchall for a lot of unique industries that would be noise for our clustering
    industry_df_dict = {} # create empty df for dfs for each industry
    for ind in ind_list:
        industry_df_dict[ind] = df[df.Industry == ind][['Date', 'Total Employment']].set_index('Date')['Total Employment'].sort_index() # pull out series
    return industry_df_dict, ind_list