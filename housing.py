import numpy as np
import matplotlib.pyplot as plt

def load_data():
    data = []
    with open('HousePriceLinearRegressionData.txt', 'r') as file:
        for line in file.readlines():
            line = line[:-1]
            data.append(line.split(', '))
    data = np.array(data,dtype=float)
    return data[:,0], data[:,1]

if __name__ == '__main__':
    # data preprocess
    X,Y = load_data()
    Y = Y.reshape((len(Y),1))
    X = X.reshape((len(X),1))
    one = np.ones(len(X))
    X = np.column_stack((X,one))
    W = np.random.randn(2,1)
    learning_rate = 0.00005
    
    # start training
    for i in range(1000):
        y_predict = X.dot(W)
        diff = y_predict - Y
        loss = np.sum(diff ** 2)
        gradient = learning_rate * X * diff
        gradient = np.sum(gradient,axis=0) / gradient.shape[0]
        gradient = gradient.reshape((2,1))
        W = W - gradient
        if i % 10 == 0:
            print('step %d, loss = %.2f' % (i,loss))

    # visiualize result
    X,Y = load_data()
    plt.scatter(X,Y,s=6,c='red')
    x = np.linspace(30,210,500)
    one = np.ones(len(x))
    X = x.reshape((len(x),1))
    X = np.column_stack((X,one))
    y_predict = X.dot(W)
    plt.plot(x,y_predict)
    plt.xlabel('Size of House')
    plt.ylabel('Price')
    plt.title('Linear Regression Model on House Price Problem')
    plt.savefig('house')
    plt.show()




