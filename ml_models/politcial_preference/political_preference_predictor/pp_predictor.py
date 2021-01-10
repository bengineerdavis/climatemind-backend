import sys, argparse

from data_loader import load_data
from model import Model

def main():
    
    model = Model('LASSO')
    model.train()










if __name__ == "__main__":
    main()