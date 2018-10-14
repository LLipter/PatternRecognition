from dataset import getSimpleTestData
from dataset import getRandomData
from dataset import preprocess
from dataset import print_rules
from dataset import print_frequent_itemset

def compute_frequency(dataset):
    frequency = {}
    for data in dataset:
        for item in data:
            frequency[item] = frequency.get(item,0) + 1
    return frequency

def sort_data(dataset, frequency):
    result = []
    for i in range(len(dataset)):
        listdata = list(dataset[i])
        listdata.sort(key=lambda item : frequency[item], reverse=True)
        result.append(listdata)
    return result

def prune(dataset, frequency, minSupport):
    result = []
    for i in range(len(dataset)):
        result.append([item for item in dataset[i] if frequency[item] >= minSupport])
    return result

def fpgrowth(dataset, minSupportRatio, minConfidenceRatio):
    dataset = preprocess(dataset)
    minSupport = int(minSupportRatio * len(dataset))
    frequency = compute_frequency(dataset)
    dataset = sort_data(dataset, frequency)
    dataset = prune(dataset,frequency,minSupport)
    print(dataset)


    return 1,1




if __name__ =='__main__':
    dataset = getSimpleTestData()
    # data = getRandomData()
    frequent_itemset, rules = fpgrowth(dataset,0.5,0.5)
    
    # print_frequent_itemset(frequent_itemset)
    # print_rules(rules)
    # print(len(frequent_itemset))
    # print(len(rules))
