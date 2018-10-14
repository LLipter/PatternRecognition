import matplotlib.pyplot as plt

def preprocess(data):
    itemsets = []
    for i in range(len(data)):
        itemset = set(data[i])    # remove duplicate elements
        itemsets.append(itemset)
    return itemsets

def getSupport(dataset, itemsets, minSupport):
    support = {}
    for data in dataset:
        for itemset in itemsets:
            tupleItemset = tuple(itemset)
            if itemset.issubset(data):
                support[tupleItemset] = support.get(tupleItemset,0) + 1
    return {itemset:count for itemset,count in support.items() if count >= minSupport}

def printResult(result):
    for s in result:
        setstr = ''
        for item in s:
            setstr += str(item) + ' '
        print(setstr)

def isJoinable(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) == 0:
        return False
    for i in range(len(s1)-1):
        if s1[i] != s2[i]:
            return False
    if s1[-1] >= s2[-1]:
        return False
    return True


def apriori(dataset, minSupportRatio):
    dataset = preprocess(dataset)
    itemsets = set()
    result = []
    for data in dataset:
        itemsets |= data
    itemsets = [set([itemset,]) for itemset in itemsets]
    minSupport = int(minSupportRatio * len(dataset))
    while True:
        L = getSupport(dataset, itemsets, minSupport)
        if len(L.items()) == 0: 
            break
        result.extend(L)
        itemsets = []
        for set1 in L.keys():
            for set2 in L.keys():
                if isJoinable(set1, set2):
                    itemsets.append(set(set1) | set(set2))
    return result


def getSimpleTestData():
    data = [[1,3,4],
            [2,3,5],
            [1,2,3,5],
            [2,5]]
    return data




if __name__ =='__main__':

    result = apriori(data,0.5)
    printResult(result)