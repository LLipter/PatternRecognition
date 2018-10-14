import numpy as np

def getSimpleTestData():
    data = [[1,3,4],
            [2,3,5],
            [1,2,3,5],
            [2,5]]
    return data

def getRandomData():
    data_no = 10000
    total_product_no = 100
    threshold = 0.50

    possibility1 = np.random.rand(total_product_no)
    possibility2 = np.random.rand(total_product_no)
    data = []
    for _ in range(data_no):
        itemset = []
        possibility_first = np.random.rand()
        possibility_other = np.random.rand(total_product_no)
        if possibility_first > threshold:
            itemset.append(0)
            for j in range(1,total_product_no):
                if possibility_other[j] > possibility1[j]:
                    itemset.append(j)
        else:
            for j in range(1,total_product_no):
                if possibility_other[j] > possibility2[j]:
                    itemset.append(j)
        data.append(itemset)
    return data

def preprocess(data):
    itemsets = []
    for i in range(len(data)):
        itemset = set(data[i])    # remove duplicate elements
        itemsets.append(itemset)
    return itemsets

