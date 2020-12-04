import readCSV
import decomps
import numpy as np


array = readCSV.readCSV('28x11Fib.csv')
farray = decomps.strgToFloat(array)
#print(np.dot(decomps.QRDecomp(farray)[0],decomps.QRDecomp(farray)[0].T))
#a1 = np.array([[1,0,0],[0,1,0],[0,0,1]])
#a2 = np.array([[1,2,3],[2,4,6],[7,8,9]])
#print(np.dot(a1,a2))
'''
print(decomps.SVDDecomp(farray)[1])
print(np.linalg.matrix_rank(farray,1.0e-20))

Q = decomps.approxGivenMat(farray,4.0e-7,0)
print(Q)
print(decomps.findError(farray,Q))
'''


'''
X = np.dot(Q,Q.T)
X = np.dot(X,farray)
E = farray-X
print(np.linalg.norm(E))
'''
#QR = decomps.SVDDecomp(farray)
#rank = np.linalg.matrix_rank(farray, 1.0e-10)
#print(rank)
#print(decomps.EigDecomp(farray))




#structure score reflects how much error is required to reduce the amount of information within a matrix. The more random,
#the less reduction is required to remove information. 
#Take the amount of error needed to reduce the rank by 1
#find the relitive percent of information that rank holds. 1/total ranks of original matrix
#That percentage of the matrixes total information is stored in the information lost: ie, the error represents a loss of that much of the total information. 
n = decomps.erInFirstRank(farray,1.0e-15,0,100)

