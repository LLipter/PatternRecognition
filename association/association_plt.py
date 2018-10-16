import matplotlib.pyplot as plt
import numpy as np
from fpgrowth import fpgrowth
from dataset import getRandomData

if __name__ == '__main__':
    np.random.seed(0)
    dataset = getRandomData()

    x = np.linspace(0.30,0.50,30)
    y = []
    for support_ratio in x:
        _, rules = fpgrowth(dataset, support_ratio, 0.8)
        y.append(len(rules))
        print('graph 1, support = %.2f, confidence = 0.8, number of rules = %i' % (support_ratio, len(rules)))
    print(y)
    plt.plot(x,y)
    plt.title('Given Confidence = 80%')
    plt.xlabel('Support Ratio')
    plt.ylabel('Number of Association Rules')
    plt.savefig('../assets/confidence80')
    plt.show()

    # x = np.linspace(0.5,0.8,30)
    # y = []
    # for confidence in x:
    #     _, rules = fpgrowth(dataset, 0.3, confidence)
    #     y.append(len(rules))
    #     print('graph 2, support = 0.3, confidence = %.2f, number of rules = %i' % (confidence,len(rules)))
    # print(y)
    # plt.plot(x,y)
    # plt.title('Given Support Ratio = 30%')
    # plt.xlabel('Confidence')
    # plt.ylabel('Number of Association Rules')
    # plt.savefig('../assets/support30')
    # plt.show()
