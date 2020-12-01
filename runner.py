import readCSV
import decomps
import numpy as np


array = readCSV.readCSV('test.csv')
farray = decomps.strgToFloat(array)
#print(farray)
#print(decomps.QRDecomp(farray))
#print(decomps.EigDecomp(farray))

'''
print(q)
print(r)
print(np.dot(q,r)) 
'''
