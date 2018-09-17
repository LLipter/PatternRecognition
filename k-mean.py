import numpy as np

'''
The choice of initial center points will affect the final result of K-mean algorithm.
'''

# define parameters
dimension = 2 # dimension of data points
n = 10 # number of data points
K = 3 # number of classes

# generate data points
X = np.array([
    [0,0],
    [7,3],
    [4,6],
    [1,1],
    [2,2],
    [3,7],
    [3,6],
    [5,7],
    [6,3],
    [7,4]
])
# generate random data
# X = np.random.rand(n,dimension)

# initialize center point Z
Z_pre = np.zeros((K,dimension))
Z = X[:K].copy()

# main iteration
group = []
while (Z == Z_pre).all() != True:
    Z_pre = Z.copy()
    Z = Z.reshape((K,1,dimension))
    dist = np.sum((Z - X) ** 2, axis=2)
    group = np.argmin(dist, axis=0)
    Z = Z.reshape((K,dimension))
    for k in range(K):
        k_data = X[np.where(group == k)]
        Z[k] = np.average(k_data, axis=0)
    


# print result
for k in range(K):
    k_result = np.where(group == k)[0]
    print('group %i' % k)
    print(k_result)
