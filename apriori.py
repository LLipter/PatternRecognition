import matplotlib.pyplot as plt

def preprocess(data):
    itemsets = []
    for i in range(len(data)):
        itemset = set(data[i])    # remove duplicate elements
        itemsets.append(itemset)
    return itemsets

def getSupport(itemsets, keys, minSupport):
    support = {}
    for itemset in itemsets:
        for key in keys:
            tupleKey = tuple(key)
            if key.issubset(itemset):
                support[tupleKey] = support.get(tupleKey,0) + 1
    return {key:count for key,count in support.items() if count >= minSupport}

def printSets(L):
    for s in L:
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


def apriori(data, minSupportRatio):
    data = preprocess(data)
    keys = set()
    for itemset in data:
        keys |= itemset
    keys = [set([key,]) for key in keys]
    minSupport = int(minSupportRatio * len(data))
    L = getSupport(data, keys, minSupport)  # L1
    while True:
        printSets(L)
        keys = []
        for set1 in L.keys():
            for set2 in L.keys():
                if isJoinable(set1, set2):
                    keys.append(set(set1) | set(set2))
        L = getSupport(data, keys, minSupport)
        if len(L.items()) == 0: 
            break

    



if __name__ =='__main__':
    data = [[1,3,4],
            [2,3,5],
            [1,2,3,5],
            [2,5]]

    apriori(data,0.5)