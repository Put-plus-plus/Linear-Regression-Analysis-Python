## Description 
Regression analysis is a set of statistical processes for estimating the relationship between a dependent variable and independent variables. Here the user can X different convidence intervals An opportunity to try out multiprocessing – what learned.

The `DataPrep` class has a `merging_fun()` method for turning wide data long, a `cleaning_fun()` method for removing values that sit outside of permitted boundaries, and a `data_check_fun()` method for visually inspecting the data by generating histograms of all variables. The `RegressionModel` class has a `variable_preparation()` method for generating a powerset from the variables, and a `multip_best_regression_model()` method for generating regression models from  and storing summaries of the models in a. The method for generating regression models is used in. 

## Dependencies
* Microsoft Windows 10.0.19045
* Python 3.9.1
* numpy 1.22.2, pandas 1.2.2, re 2.2.1, matplotlib 3.3.4, statsmodels 0.14.1, time (built-in module) 

## Execution - blood panel example
```python
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
 
## Animation - Liver Disease Analysis Example
remember to add the link to the GIF, which I must also make sure to add to the repo, see stackoverflow - maybe show the output the CSV files  
