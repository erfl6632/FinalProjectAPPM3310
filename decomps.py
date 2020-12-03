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


    #gen plan:
    #part A = find the Q: inputs: mxn mat A, int l, outputs approximation of A as matrix Y

    #follows Algorithm 4.1
def randApprox(A, l): #A = input matrix to be approximated, l = int
    m = A.shape[0]
    n = A.shape[1]
    Omega = []
    for i in range(n):
        row = []
        for j in range(l):
             row.append(np.random.normal())
        Omega.append(row)
    Omega = np.array(Omega)
    Y = np.dot(A,Omega)
    return Y



def makeRedI(n, a): # n is the original size of the matrix, a is the size of the I matrix to have within the big matrix
    I = np.identity(n)
    for i in range(n):
        if i > a :
            I[i][i] = 0
    return I


#find the number of columns to approximate with depending on error tolerence and oversampling value
#follows 4.2
def approxDim(A,E,o): #A = matrix to be approximated, E = error tolerence (suggested: 5 (95% confidence)), o = oversampling value(suggested: between 5 and 10 depending on sample size)
    # i is the dimension to be found. Min dimension of reduction while maintaining target error tolerence. 
    maxDim = A.shape[0]
    print(maxDim)
    i = maxDim-1
    trigger = False
    I = np.identity(maxDim)
    while trigger == False:
        a = makeRedI(maxDim,i)
        redI = np.subtract(I,a) #reduced Identity matrix
        redA = np.dot(redI,A) #reduced A matrix
        if(np.linalg.norm(redA) > E):
            trigger = True
            #print("at error: " + str(np.linalg.norm(redA)) + " of allowed " +str(E) + ". Ranks reduced: " + str(maxDim-i))
        else:
            #print("not at error,"+str(np.linalg.norm(redA))+" reducing")
            i = i-1
    return i + 1 + o
    
