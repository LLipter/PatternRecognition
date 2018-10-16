import numpy as np
import matplotlib.pyplot as plt

# function to compute skewness of given data
def skewness(data):
    mu =  np.mean(data)
    sigma = np.std(data)
    skew = (data - mu) / sigma
    skew = skew ** 3
    skew = np.sum(skew) / len(data)
    return skew

if __name__ =='__main__':
    np.random.seed(0)
    # symmetric data
    data = np.random.normal(0,1,size=100000)
    skew = skewness(data)
    plt.hist(data,bins=500, density=1)
    plt.text(1,0.3,'skewness = 0.00',fontsize=12)
    plt.title("symmetric distribution")
    plt.savefig("assets/symmetric")
    plt.show()


    # positively skewed
    data = np.random.normal(0,1,size=10000)
    data = np.append(data,np.random.normal(-3,1,90000))
    skew = skewness(data)
    plt.hist(data,bins=500, density=1)
    plt.text(-1,0.3,'skewness = %.2f' % skew,fontsize=12)
    plt.title("positively skewed distribution")
    plt.savefig("assets/ps")
    plt.show()
    

    # negatively skewed
    data = np.random.normal(0,1,size=10000)
    data = np.append(data,np.random.normal(3,1,90000))
    skew = skewness(data)
    plt.hist(data,bins=500, density=1)
    plt.text(-2,0.3,'skewness = %.2f' % skew,fontsize=12)
    plt.title("negatively skewed distribution")
    plt.savefig("assets/ns")
    plt.show()
