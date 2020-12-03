import readCSV
import decomps
import numpy as np


array = readCSV.readCSV('test2.csv')
farray = decomps.strgToFloat(array)
#print(farray)

k = decomps.approxDim(farray,99,0)
print(k)



'''
Y = decomps.randApprox(farray, k)
print(Y)
'''


#QR = decomps.SVDDecomp(farray)
#rank = np.linalg.matrix_rank(farray, 1.0e-10)
#print(rank)
#print(decomps.EigDecomp(farray))

'''
print(q)
print(r)
print(np.dot(q,r)) 
'''

'''
ranks = np.linalg.matrix_rank(farray)
for i in range(ranks):
    e = np.linalg.matrix_rank(farray)-1-i
    newRank = decomps.approxDim(farray,e,0)
    #print(ranks)
    #print(newRank)
    if(newRank != ranks):
        print(str(newRank) + " , " + str(e))
        rank = newRank
'''
