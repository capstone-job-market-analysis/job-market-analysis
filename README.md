# Texas Job Market Analysis README.md

- add image here

### Team Members: Adam Talbot, Curtis Johansen, James Allen, Jeff Akins, Veronica Reyes

# Table of Contents

---

- [Executive Summary](#executive-summary)
    - [Project Objectives](#project-objectives)
    - [Conclusions and Takeaways](#conclusions-and-takeaways)
    - [Next Steps and Recommendations](#next-steps-and-recommendations)    
- [Data Dictionary](#data-dictionary)
- [Initial Questions](#initial-questions)
- [Formal Hypotheses](#formal-hypotheses)
- [Pipeline Stages Breakdown](#pipeline-stages-breakdown)
    - [Plan](#plan)
    - [Acquire](#acquire)
    - [Prepare](#prepare)
    - [Explore](#explore)
    - [Model and Evaluate](#model-and-evaluate)
- [Conclusion and Next Steps](#conclusion-and-next-steps)
- [Reproduce My Project](#reproduce-my-project)

---

### Executive Summary

- This project explored the impact of COVID-19 on the Texas job market. 98 Industries were examined using a combination of U.S. Census data and Texas Labor Market Information. Clustering analysis was used to group the industries into seven categories based on the magnitude of their job loss during the first half of 2020. For the industries that were most affected, subcategories were examined such as gender, age group, education, race, and ethnicity. Time Series modeling was then used to forecast when selected industries would return to pre-COVID levels of employment. 


[(Back to top)](#table-of-contents)

---

#### Project Objectives

[(Back to top)](#table-of-contents)

- Determine the affect, if any, of the COVID-19 pandemic on the Texas labor market for the year 2020.

#### Conclusions and Takeaways 

[(Back to top)](#table-of-contents)

- After examining the impact of COVID-19 on the Texas job market, we discovered that out of the 98 industries examined, we could categorize those industries into seven distinct groupings based on their total employment trends


#### Next Steps and Recommendations

[(Back to top)](#table-of-contents)

- Continue to refine metrics to characterize time series data

- Forecast time until back to pre-COVID employment numbers for recovering industries

- Forecast continuation of pre-COVID trends after recovery

- Normalize subgroup drill down numbers

#### Audience
- Anyone interested in taking a look at the Texas job market during the COVID-19 pandemic

#### Project Context
- The Cluster dataset was obtained from: [link](https://texaslmi.com/)

- The Explore dataset was obtained from: [link](https://ledextract.ces.census.gov/static/data.html)

#### Data Dictionaries

[(Back to top)](#table-of-contents)

---

| Feature                        | Description                                                                                                            | Data Type | Notes |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | --------- | ------------- |


---
| Feature | Definition | Data Type | Notes |
| ----- | ----- | ----- | ----- |


---

#### Initial Questions

[(Back to top)](#table-of-contents)

- Question 1: How has the job market in Texas been affected by the COVID-19 pandemic?

- Question 2: Were different industries affect by the covid-19 pandemic?


### Pipeline Stages Breakdown

---

##### Plan

[(Back to top)](#table-of-contents)

- [x] Create README.md with data dictionary, project and business goals, and come up with initial hypotheses.
- [x] Acquire data from (_), save to local .csv and create a function to automate this process. Save the function in an wrangle.py file to import into the Final Report Notebook.
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

### Conclusion and Next Steps

[(See Executive Summary)](#executive-summary)

--- 


### Reproduce This Project

---

[(Back to top)](#table-of-contents)
 
- [x] Read this README.md
- [ ] Download the modules (.py files), and final_report.ipynb files into your working directory
- [ ] Download complete dataset from:
- [ ] Run the final_report.ipynb notebook