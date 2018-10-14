from dataset import getSimpleTestData
from dataset import getRandomData
from dataset import preprocess
from dataset import print_rules
from dataset import print_frequent_itemset
from fpnode import Fpnode

def compute_frequency(dataset):
    frequency = {}
    for data in dataset:
        for item in data[0]:
            frequency[item] = frequency.get(item,0) + data[1]
    return frequency

def sort_data(dataset, frequency):
    result = []
    for i in range(len(dataset)):
        data = dataset[i]
        data[0].sort(key=lambda item : frequency[item], reverse=True)
        result.append(data)
    return result

def prune(dataset, frequency, minSupport):
    result = []
    for i in range(len(dataset)):
        data = dataset[i]
        listdata = [item for item in data[0] if frequency[item] >= minSupport]
        result.append((listdata,data[1]))
    return result

def insert_data(data, root, header):
    for item in data[0]:
        if item not in root.child.keys():
            newnode = Fpnode(item)
            newnode.pa = root
            root.child[item] = newnode
            if item not in header.keys():
                header[item] = None
            header[item] = (newnode, header[item])
        root = root.child[item]
        root.count = root.count + data[1]
        

def build_fptree(dataset, minSupport):
    root = Fpnode()
    header = {}
    frequency = compute_frequency(dataset)
    dataset = prune(dataset, frequency, minSupport)
    dataset = sort_data(dataset, frequency)
    for data in dataset:
        insert_data(data, root, header)
    


def fpgrowth(dataset, minSupportRatio, minConfidenceRatio):
    dataset = preprocess(dataset)
    dataset = [(list(data),1) for data in dataset]
    minSupport = int(minSupportRatio * len(dataset))
    build_fptree(dataset, minSupport)


    return 1,1




if __name__ =='__main__':
    dataset = getSimpleTestData()
    # data = getRandomData()
    frequent_itemset, rules = fpgrowth(dataset,0.5,0.5)
    
    # print_frequent_itemset(frequent_itemset)
    # print_rules(rules)
    # print(len(frequent_itemset))
    # print(len(rules))
