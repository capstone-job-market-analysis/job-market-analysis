# Texas Job Market Analysis README.md

- put an image here

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

- 

[(Back to top)](#table-of-contents)

---

#### Project Objectives

[(Back to top)](#table-of-contents)

- 

#### Conclusions and Takeaways 

[(Back to top)](#table-of-contents)

- 

- 

#### Next Steps and Recommendations

[(Back to top)](#table-of-contents)

-

#### Audience
- Anyone interested in taking a look at the Texas job market during the COVID-19 pandemic

#### Project Context
- The Cluster dataset was obtained from:

- The Explore dataset was obtained from:

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

- Question 1

- Question 2

#### Formal Hypotheses

[(Back to top)](#table-of-contents)

- See notebook for formal hypotheses and statistical testing

---

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

- Store functions that are needed to acquire data from Kaggle; make sure the acquire.py module contains the necessary imports to run our code.
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

##### Model and Evaluate

[(Back to top)](#table-of-contents)

- 

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