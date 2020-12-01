import numpy as np

def strgToFloat(array):
    floats = []
    for i in range(len(array)):
        row = []
        for j in range(len(array[i])):
            row.append(float(array[i][j]))
        floats.append(row)
    floats = np.array(floats)
    return floats

def QRDecomp(array):  #expected input: a ndarray class array, what is returned from a readCSV call
    qr = np.linalg.qr(array)
    return qr
    #returns the Q array, and the R array in a single array (3d array)

def SVDDecomp(array): #expected input: a ndarray class array, what is returned from a readCSV call
    svd = np.linalg.svd(array)
    return svd
    ##returns the U array, the S array, and the V array in a single array (3d array)

def EigDecomp(array):  #expected input: a ndarray class array, what is returned from a readCSV call
    print(array)
    eig = np.linalg.eig(array)
    return eig
    #returns the Q array, and the R array in a single array (3d array)