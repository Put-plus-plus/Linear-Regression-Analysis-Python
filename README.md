## Description 
In linear regression analysis an estimation is made of the linear relationship between the dependent variable and the independent variable(s). In this case the regression analysis is organised into the `RegressionAnalysis` class, which has five methods. The `format_data()` method creates a dataset with long data (eg var1, var2) from a dataset with wide data (eg var1_1, var1_2, var2_1, var2_2, var2_3). The `clean_data()` method filters the dataset so to remove anomalies and to create a dataset with complete data. The `inspect_data()` method creates histograms for all variables before and after the dataset was cleaned. The `fit_reg_model()` method accepts the dependent variable and fits a regression model with all the independent variables in the dataset. The `create_summaries()` method accepts a list with the desired confidence intervals (eg [0.1, 0.5, 0.01], ie the 90%, 95%, and 99% CI respectively) and creates model summaries.

The dataset used in the example below is an adapted version of Lichtinghagen,Ralf, Klawonn,Frank, and Hoffmann,Georg. (2020). HCV data. UCI Machine Learning Repository. https://doi.org/10.24432/C5D612, and is used under a Creative Commons Attribution 4.0 International licence. A selection of variables was made, and the format of the original data was changed and anomalous values were introduced to illustrate the data cleaning capabilities of the above described methods.


## Dependencies
* Microsoft Windows 10.0.19045
* Python 3.9.1
* numpy 1.22.2, pandas 1.2.2, re 2.2.1, matplotlib 3.3.4, statsmodels 0.14.1, time (built-in module) 

## Execution - regression analysis example
```python
from regressionanalysis import *

blood_df_wide = pd.read_csv('C:\\Users\\User\\Desktop\\regression_data.csv')          
blood = RegressionAnalysis(blood_df_wide)  

blood.format_data()

blood_allowed_dict = {'ALB':[10.0, 100.0], 'ALP':[10.0, 450.0], 'ALT':[0.5, 350.0],
                'AST':[10.0, 350.0], 'BIL':[0.5, 300.0], 'CHE':[1.0, 20.0],
                'CHOL':[1.0, 10.0], 'CREA':[5.0, 1200.0], 'GGT':[1.0, 700.0],
                'PROT':[40.0, 100.0]}
blood.clean_data(blood_allowed_dict)

blood_pdf_path = 'C:\\Users\\User\\Desktop'                     
blood.inspect_data(blood_pdf_path)

blood_dependent_var = 'PROT'                                                   
blood.fit_reg_model(blood_dependent_var)

blood_ci_list = [0.1, 0.075, 0.05, 0.03, 0.01]                                  
blood_summaries_path = 'C:\\Users\\User\\Desktop'                                 
blood.create_summaries(blood_ci_list, blood_summaries_path)
```

