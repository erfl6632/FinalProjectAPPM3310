import numpy as np
import csv 
A = np.array([[7,3,2],[2,0,7]])
B = np.genfromtxt('test.csv',delimiter=',')
# print(B)
Product = np.linalg.cholesky(B)
# print(Product)
