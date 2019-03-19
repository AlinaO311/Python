import numpy as np
import math
import timeit

def compute_norm(N, vect):
# function to compute the norm
    norm = 0
    for i in range(N):
        norm += vect[i] ** 2
    return math.sqrt(norm)

def dot_product(N, matrix, vector):
#function to compute dot product of matrix and vector
    mult_vect = np.empty_like(vector)
    for i in range(N):
        tmp = 0
        for j in range(N):
            tmp += matrix[i][j] * vector[j]
        mult_vect[i] = tmp
    return mult_vect
#input parameters
N = int( input('input dimension of matrix (N): '))
tol = float( input('input error tolerance (tol): '))
#number of iterations
iterations_M = 1000
np.random.seed(7)
#create matrixA size of NxN
matrixA = np.random.randint(10,size = (N,N))
#vector of all ones size of N
vector1 = np.ones(N)

### approach 1
start_time = timeit.default_timer()
for i in range(iterations_M):
    mult_vect = dot_product(N, matrixA, vector1)
    max = np.max(mult_vect)
    norm_vect = mult_vect / max
    vector1 = np.array(norm_vect)
elapsed_time1 = timeit.default_timer() - start_time

print('The maximum eigen value through approach 1 is: ', max)
print('The time elapsed is: ', elapsed_time1)

### approach 2
start_time = timeit.default_timer()
for i in range(iterations_M):
        app2_dot_product = np.dot(matrixA, vector1)
        max_eigval = np.max(app2_dot_product)
        eig_vector = app2_dot_product/max_eigval

        norm_app2 = np.linalg.norm(eig_vector)
        norm_app2_vector = np.linalg.norm(vector1)
        vector1 = np.array(eig_vector)
        if abs(norm_app2_vector - norm_app2 ) < float(tol):
            break
elapsed_time2 = timeit.default_timer() - start_time
print('The maximum eigen value through approach 2: ', max_eigval)
print('The time elapsed is: ', elapsed_time2)

### approach 3
start_time = timeit.default_timer()
eig_values,eig_vects = np.linalg.eig(matrixA)
Max_eigval_linAlg = np.max(eig_values.real)
elapsed_time3 = timeit.default_timer() - start_time
print('The maximum eigen value through approach 3 is: ', Max_eigval_linAlg)
print('The time elapsed is: ', elapsed_time3)
