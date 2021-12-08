# Help Wanted

<img src="https://i2.wp.com/kychamberbottomline.com/wp-content/uploads/2021/07/Jobs.jpg?resize=777%2C437&ssl=1" alt="Help Wanted" title="Help Wanted" width="777" height="437" />

### Team Members: Adam Talbot, Curtis Johansen, James Allen, Jeff Akins, Veronica Reyes

# Table of Contents

---

- [Executive Summary](#executive-summary)
    - [Project Objectives](#project-objectives)
    - [Conclusions and Takeaways](#conclusions-and-takeaways)
    - [Recommendations](#recommendations) 
    - [Next Steps](#next-steps)    
- [Data Dictionaries](#data-dictionaries)
- [Initial Questions](#initial-questions)
- [Pipeline Stages Breakdown](#pipeline-stages-breakdown)
    - [Plan](#plan)
    - [Acquire](#acquire)
    - [Prepare](#prepare)
    - [Explore](#explore)
    - [Cluster](#cluster)
    - [Forecast](#forecast)
- [Conclusion and Next Steps](#conclusion-and-next-steps)
- [Reproduce This Project](#reproduce-this-project)

---

### Executive Summary

---

- This project explored the impact of COVID-19 on the Texas job market. 98 Industries were examined using a combination of U.S. Census data and Texas Labor Market Information. Clustering analysis was used to group the industries into seven categories based on the magnitude of their job loss during the first half of 2020. For the industries that were most affected, subcategories were examined such as gender, age group, education, race, and ethnicity. Time Series modeling was then used to forecast when selected industries would return to pre-COVID levels of employment. 


[(Back to top)](#table-of-contents)

---

#### Project Objectives

[(Back to top)](#table-of-contents)

- Explore the impact of the COVID-19 pandemic on the Texas job market
    - Explore demographic subgroups of gender, ethnicity, race, age, and education level
- Group industries together based on effect of pandemic
- Forecast recovery timelines for most-affected industries

---

#### Conclusions and Takeaways 

[(Back to top)](#table-of-contents)

- Effect on industries
    - 87% Negative Impact
    - 10% Positive Impact
    - 3% No Impact
- Recovery timelines for 11 most-affected industries varied from 3 to 26 months from end of data (June 2021)
- Demographics Most Affected
    - Gender:  Women
    - Ethnicity: Hispanic or Latino
    - Race: African Americans
    - Age: 34 and below, especially 22-24
    - Education Level:  Those without a Bachelor's or Advanced Degree

---

#### Recommendations

[(Back to top)](#table-of-contents)

- Industries now have a better understanding of appropriate employment levels during a pandemic
- Planning and preparation
- State and local governments should also examine the disparity among demographic subgroups

---

#### Next Steps

[(Back to top)](#table-of-contents)

- Adjust forecasting model as new data becomes available 
- Examine the Pandemic's affect on the national economy
- Compare industry clusters by state
- Compare demographic job loss information by state

---

#### Audience
- Anyone interested in taking a look at the Texas job market during the COVID-19 pandemic

---

#### Project Context
- The cluster and forecasting dataset was obtained from: [Texas Labor Market](https://texaslmi.com/)
- The explore dataset was obtained from: [US Census](https://ledextract.ces.census.gov/static/data.html)

---

#### Data Dictionaries

---

[(Back to top)](#table-of-contents)

---

**Explore**

|Variable	|Type	|label |
| ----- | ----- | ----- |
|periodicity	|Char(1)	|Periodicity of report|
|seasonadj	|Char(1)	|Seasonal Adjustment Indicator|
|geo_level	|Char(1)	|Group: Geographic level of aggregation|
|geography	|Char(8)	|Group: Geography code|
|ind_level	|Char(1)	|Group: Industry level of aggregation|
|industry	|Char(5)	|Group: Industry code|
|ownercode	|Char(3)	|Group: Ownership group code|
|sex	|Char(1)	|Group: Gender code|
|agegrp	|Char(3)	|Group: Age group code (WIA)|
|race	|Char(2)	|Group: race|
|ethnicity	|Char(2)	|Group: ethnicity|
|education	|Char(2)	|Group: education|
|firmage	|Char(1)	|Group: Firm Age group|
|firmsize	|Char(1)	|Group: Firm Size group|
|year	|Num	|Time: Year|
|quarter	|Num	|Time: Quarter|


**Cluster**

| Feature | Definition | Data Type | Notes |
| ----- | ----- | ----- | ----- |
| 'Year'| year column | int64 | datetime for year
| 'Period' | One, Two, Three | int64 | Periods for each quarter |
| 'Industry Code' | industry classification code | int64 | Code to classify each industry
| 'Industry' | Industry name | object | Name of each industry |
| 'Month' | Month of the year | int64 | datetime for Month |
| 'Total Employment' | total number of employment | int64 | Total number of employment |
| 'Date' | year, month, day | datetime64 | date format YYYY-MM-DD |

---

#### Initial Questions

[(Back to top)](#table-of-contents)

1. How has the job market in Texas been affected by the COVID-19 pandemic?
2. Were groups of industries affected similarly?
3. Were certain demographic subgroups affected disproportionately?

### Pipeline Stages Breakdown

---

##### Plan

[(Back to top)](#table-of-contents)

- [x] Create README.md with data dictionary, project and business goals, and come up with initial hypotheses.
- [x] Acquire data from websites, save to local .csv and create a function to automate this process. Save the function in an wrangle.py file to import into the Final Report Notebook.
- [x] Clean and prepare data. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the function.
- [x] Clearly define at least two hypotheses and document findings and takeaways.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.
- [x] Iterate back through the pipeline imporving each phase as time permits
___

##### Acquire

[(Back to top)](#table-of-contents)

- Store functions that are needed to acquire data from internet sources; make sure the acquire.py module contains the necessary imports to run our code.
- The final function will return a pandas DataFrame.
- Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
- Complete some initial data summarization (`.info()`, `.describe()`, `.shape()`, ...).
___

##### Prepare

[(Back to top)](#table-of-contents)

- Store functions needed to prepare the data; make sure the module contains the necessary imports to run the code. The final function should do the following:
    - Handle any missing values.
    - Handle erroneous data and/or outliers that need addressing.
    - Encode variables as needed.
    - Identify unit measures and decide how to best scale any numeric data
    - Remove outliers
- Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.
- Plot distributions of individual variables.
___

##### Explore

[(Back to top)](#table-of-contents)

- Answer key questions, our hypotheses, and figure out the features that we want to identify to explore.
- Create visualizations that work toward discovering variable relationships 
- Summarize our conclusions, provide clear answers to our specific questions, and summarize any takeaways/action plan from the work above.
___

##### Cluster

[(Back to top)](#table-of-contents)

- Industries were clustered into 7 groups:

1. Moderate Negative Impact, Quick Recovery
2. Positively Impacted
3. Significant Negative Impact, Mostly Recovered
4. Significant Negative Impact, Mostly Recovered, Highly Seasonal
5. No Impact
6. Moderate Negative Impact, Slow or No Recovery
7. Minor Negative Impact, Quick Recovery

---

##### Forecast

[(Back to top)](#table-of-contents)

- Use recovery trend for recovering industries to predict timeline for full recovery
- Predict resumption of pre-COVID behavior after recovery

---

### Conclusion and Next Steps

[(See Executive Summary)](#executive-summary)

--- 


### Reproduce This Project

---

[(Back to top)](#table-of-contents)
 
- [x] Read this README.md
- [ ] Download the modules (.py files), and final_notebook.ipynb files into your working directory
- [ ] Download dataset csv files using links in final notebook
- [ ] Run the final_report.ipynb notebook