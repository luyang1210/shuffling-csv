'''
Title  : Pandas Row Shuffler 
Author : Felan Carlo Garcia
'''
import numpy as np
import pandas as pd


def shuffler(filename):
  df            = pd.read_csv(filename, header=0)
  shuffled_data = df.reindex(np.random.permutation(df.index))
  # return the pandas dataframe
  return shuffled_data
  
def main():
  output = shuffler('titanic3.csv')
  output.to_csv('shuffled_output.csv', sep=',')

if __name__ == '__main__': 
  main()