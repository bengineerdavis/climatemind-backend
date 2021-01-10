""" 
Implement: LASSO, Logistic Regression, and NB

"""

import numpy as np
from sklearn.linear_model import LinearRegression, Lasso

from data_loader import load_data

class Model:

    def __init__ (self, classifier_type):

        if classifier_type == 'LASSO':
            self.model = Lasso(alpha = 1.0) #'alpha' --> lambda value
        elif classifier_type == 'LinearRegression':
            self.model =LinearRegression()
        
    def train(self):
        
        print("training model...")
        #QUESTION for Kameron: What path do I pass?
        X_train, X_test, y_train, y_test = load_data("/Users/alexiscarras/Desktop/cm backend/climatemind-backend/ml_models/politcial_preference/datasets/pvq21CENTRED.csv")
        


    def predict(self, x_unknown = None):

        pass

    def test(self, X_test, y_test): 

        pass 

