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

def qr_fact(A): # becuase QRDecomp wasnt working...
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = A[:, j]

        for i in range(j - 1):
            q = Q[:, i]
            R[i, j] = q.dot(v)
            v = v - R[i, j] * q

        norm = np.linalg.norm(v)
        Q[:, j] = v / norm
        R[j, j] = norm
    return Q, R

def SVDDecomp(array): #expected input: a ndarray class array, what is returned from a readCSV call
    svd = np.linalg.svd(array)
    return svd
    ##returns the U array, the S array, and the V array in a single array (3d array)

def EigDecomp(array):  #expected input: a ndarray class array, what is returned from a readCSV call
    eig = np.linalg.eig(array)
    return eig
    #returns the Q array, and the R array in a single array (3d array)


    #gen plan:
    #part A = find the Q: inputs: mxn mat A, int l, outputs approximation of A as matrix Y

    #follows Algorithm 4.1
def randApprox(A, l): #A = input matrix to be approximated, l = # of samples to take
    m = A.shape[0]
    n = A.shape[1]
    Om = []
    for i in range(n):
        row = []
        for j in range(l): # make w
             row.append(np.random.normal())
        Om.append(row)
    Om = np.array(Om)
    Y = np.dot(A,Om)
    Q = QRDecomp(Y)[0]
    return Q
 
def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

def makeRedI(n, a): # n is the original size of the matrix, a is the size of the I matrix to have within the big matrix
    I = np.identity(n)
    for i in range(n):
        if i > a :
            I[i][i] = 0
    return I


#find the number of columns to approximate with depending on error tolerence and oversampling value
#follows 4.2
#uses SVD method
def approxDim(A,e,o): #A = matrix to be approximated, E = error tolerence (suggested: .05 (95% confidence)), o = oversampling value(suggested: between 5 and 10 depending on sample size)
    svd = SVDDecomp(A)
    k=0
    for i in range(len(svd[1])): 
        #print(svd[1][i])
        if(svd[1][i] > e):
            k = k+1
    return k+o


#second method. uses ||(I-QQ*)A|| < E to minimize
def approxDimMin(A,e,o): # A = matrix to be approximated
    i = np.linalg.matrix_rank(A,1.0e-10)
    trigger = False
    while trigger == False:
        a = randApprox(A,i)
        ei = findError(A,a)
        print(ei)
        if(ei<e):
            i = i-1
        else:
            trigger = True
    return i+o


def findError(A,a): #finds the error between an original matrix and a reduced matrix
    I = np.identity(a.shape[0])
    X = I - np.dot(a,a.transpose())
    X = np.dot(X,A)
    return np.linalg.norm(X)


def approxGivenMat(A,e,o):
    l = approxDim(A,e,o)
    oRank = np.linalg.matrix_rank(A,1.0e-15)
    Q = randApprox(A,l)
    nRank = np.linalg.matrix_rank(Q,1.0e-15)
    print("Original rank: "+str(oRank)+". New rank: "+str(nRank))
    return Q


def erInFirstRank(A,e,o,increments): #A is the matrix, e is the error to find the rank/start with, o is HOW MANY TIMES you want to increment the error. 
    inc = increments
    n = (.1-e)/inc
    oRank = np.linalg.matrix_rank(A,e)
    curEr = e + n
    trigger = False
    while trigger == False:
        if(curEr >= .1):
            print("Ya done h*cked up")
            break
        l = approxDim(A,curEr,o)
        Q = randApprox(A,l)
        nRank = np.linalg.matrix_rank(Q)
        print("curEr: "+str(curEr)+". nRank: "+str(nRank))
        if(nRank < oRank):
            trigger = True
            print('correct')
            break
        else:
            curEr = curEr + n
    print("Percent of information lost: " + str(1/oRank) + ". Error correlated to info lost: "+str(curEr))
    return n
