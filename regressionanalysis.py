import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import statsmodels.formula.api as smf
import time




class RegressionAnalysis():



    def __init__(self, df_wide):
        self.df_wide = df_wide           
        self.df_long = None  
        self.df_clean = None 
        self.reg_model = None 




    def format_data(self):   
         
        # Uses a dataframe (self.df_wide) with wide data (eg var1_1, var1_2, var2_1, var2_2, var2_3) and creates a dataframe (self.df_long) with long data (eg var1, var2).

        try:
            wide_var_names = list(self.df_wide) 
            long_var_names = []
            for wide_var_name in wide_var_names:  
                long_var_name = ''.join(re.split("[^a-zA-Z-[1]\d]*", wide_var_name))
                long_var_names.append(long_var_name)
            long_var_names = list(set(long_var_names))  

            self.df_long = pd.DataFrame()                                                                    
            for long_var_name in long_var_names:  
                wide_var_cols = [x for x in list(self.df_wide) if re.match(long_var_name, x)]   
                wide_var_cols_df = self.df_wide[wide_var_cols]   
                long_col= pd.Series(dtype='float64')  
                for index, row in wide_var_cols_df.iterrows():  
                    if len(row.dropna()) == 1:
                        row_value = row.dropna()  
                        long_col = long_col.append(pd.Series([int(row_value)]), ignore_index=True)  
                    else:
                        long_col = long_col.append(pd.Series([np.nan]), ignore_index=True)      
                self.df_long[long_var_name] = long_col

        except:
            print(f'The {RegressionAnalysis.format_data.__name__} method could not create a dataframe with long data.')




    def clean_data(self, allowed_dict):

        # Accepts a dictionary (allowed_dict) with allowed variable value ranges (eg {'var1':[4, 8]}) and filters a dataframe with float data (self.df_long) so to create a dataframe with complete data with allowed values only (self.df_clean).       

        try:
            self.df_clean = self.df_long
            for var, value in allowed_dict.items():  
                if var in list(self.df_long):
                    self.df_clean = self.df_clean.loc[(self.df_clean[var] >= value[0]) & (self.df_clean[var] <= value[1]), ]
            self.df_clean = self.df_clean.dropna() 

        except:
            print(f'The {RegressionAnalysis.clean_data.__name__} method could not filter out disallowed values.')



    
    
    def inspect_data(self, pdf_path):     
        
        # Accepts a string (pdf_path) with the path to the desired location of a pdf, which is created and contains historgrams for all variables in two dataframes (self.df_long and self.df_clean). 
           
        try:
            pdf_path_name = f'{pdf_path}\\data_inspection_histograms_{time.strftime("%Y%m%d-%H%M%S")}.pdf'
            pdf = PdfPages(pdf_path_name)  
            var_names= list(self.df_clean)

            for var_name in var_names:
                fig, axes = plt.subplots(nrows=1, ncols=2)
                self.df_long.hist(var_name,  color='red', edgecolor='black', ax=axes[0])
                self.df_clean.hist(var_name,  color='darkblue', edgecolor='black', ax=axes[1])
                pdf.savefig(fig)

            pdf.close()
            
        except:
            print(f'The {RegressionAnalysis.inspect_data.__name__} method could not create a pdf with histograms representing untidy and clean data.')
                      




    def fit_reg_model(self, dependent_var):  

        # Accepts a string (dependent_var) with the desired dependent variable, and fits a regression model (self.reg_model) using all the independent variables variables in the clean dataframe (self.df_clean).

        try:
            all_vars = list(self.df_clean) 
            all_vars.remove(dependent_var)        
            indepdent_vars = ' + '.join(all_vars)
            formula = dependent_var + ' ~ ' + indepdent_vars

            self.reg_model = smf.ols(formula, data = self.df_clean).fit()    

        except:
            print(f'The {RegressionAnalysis.fit_reg_model.__name__} method could not fit a regression model to the data.')





    def create_summaries(self, ci_list, summaries_path):

        # Accepts a list (ci_list) with floats representing desired confidence intervals (eg [0.1, 0.5, 0.01], the 90%, 95%, and 99% CI respectively), and a string (summary_path) with the path to the desired location where the regression model summmaries are to be created as csv files. 

        try:
            for ci in ci_list:
                with open(f'{summaries_path}\\summary_ci{ci}_{time.strftime("%Y%m%d-%H%M%S")}.csv', 'w') as fh:
                    fh.write(self.reg_model.summary(alpha=ci).as_csv())

        except:
            print(f'The {RegressionAnalysis.create_summaries.__name__} method could not create summaries with different CIs for the regression model.')




























