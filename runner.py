import readCSV
import numpy.linalg


array = readCSV.readCSV('test.csv')
a = np.random.randn(9, 6)
q, r = np.linalg.qr(array)
np.allclose(a, np.dot(q, r))
