import csv, numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#TEMP 
from sklearn.linear_model import LinearRegression, Lasso



def load_data(filename):
    """
    Returns 4 np.arrays: X_train, X_test, y_train, y_test
    """

    data = pd.read_csv(filename, sep=',')
    data = data.to_numpy()
   
    X, y = data[:, 2:12], data[:, 1] #X data --> All columns but 0,1,& 13 (i.e. index, lrscale, and p_avg) &&& y data --> column 1


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)


    return X_train, X_test, y_train, y_test

#     reg = LinearRegression()
#     reg.fit(x_train, y_train)

#     predicted = reg.predict(x_test)
#     print("Accuracy of: ", np.mean(predicted == y_test))
 #   X_all = data.drop(data.columns[[0, 1]], axis=1) #remove  index, lrscale columns from training set
 #   y_all = data['lrscale']


# load_data("/Users/alexiscarras/Desktop/cm backend/climatemind-backend/ml_models/politcial_preference/datasets/pvq21CENTRED.csv") #QUESTION REGARDING LOADING DATA: HOW DO I SPECIFY THE URL?