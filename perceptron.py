import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d 

def getData():
    data = [[0,0,0,1],
            [1,0,0,1],
            [1,0,1,1],
            [1,1,0,1],
            [0,0,-1,-1],
            [0,-1,-1,-1],
            [0,-1,0,-1],
            [-1,-1,-1,-1]]
    return np.array(data)


if __name__ == '__main__':
    W = np.array([-1,-2,-2,0])
    X = getData()
    c = 1

    # training
    converge = False
    counter = 1
    while not converge:
        converge = True
        for i in range(X.shape[0]):
            Xi = X[i]
            dot_product = np.sum(Xi * W)
            if dot_product <= 0:
                converge = False
                W += Xi
            print('W(%d) = %s' % (counter,W))
            counter += 1

    # visiualize result
    fig = plt.figure() 
    ax = plt.axes(projection='3d') 
    X = np.linspace(-10,10,50)
    Y = np.linspace(-10,10,50)
    X,Y = np.meshgrid(X, Y)
    Z = (-W[0]/W[2])*X + (-W[1]/W[2])*Y + (-W[3]/W[2])
    surf = ax.plot_surface(X, Y, Z)
    plt.title('decision boundary')
    plt.savefig('assets/perceptron_decision_boundary')
    plt.show()
