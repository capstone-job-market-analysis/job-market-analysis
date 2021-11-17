'''
This file will store scripts for acquiring and cleaning the Quarterly Workforce Indicators (QWI)
Census data for the State of Texas. 
'''

# Imports --------------------------------------------------------------------------------------
import pandas as pd
from datetime import datetime


# Functions ------------------------------------------------------------------------------------
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
        
        
        
        
