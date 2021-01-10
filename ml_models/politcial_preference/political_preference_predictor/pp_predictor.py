import sys, argparse

from data_loader import load_data
from model import Model



# So far: 
#    - Linear Regressor accuracy 0.263
#    - LASSO accuracy 0.334

def main():
    
    model = Model('LASSO')
    model.train()

    model.test()




if __name__ == "__main__":
    main()