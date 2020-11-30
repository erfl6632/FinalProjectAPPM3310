import readCSV
import numpy.linalg


array = readCSV.readCSV('test.csv')
q, r = np.linalg.qr(array)
np.allclose(a, np.dot(q, r))
