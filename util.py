def print_rules(rules):
    print('Association Rules:')
    for rule in rules:
        print('%s ==> %s' % (rule[0], rule[1]))

def print_frequent_itemset(result):
    print('Frequent Itemset:')
    for s in result:
        setstr = ''
        for item in s:
            setstr += str(item) + ' '
        print(setstr)

def getAllSubsets(itemset):
    if len(itemset) == 0:
        return []
    result = [[]]
    for item in itemset:
        newSet = [ oldSet + [item] for oldSet in result]
        result.extend(newSet)
    result = result[1:-1] # remove empty subset and itemset itself
    for i in range(len(result)):
        result[i].sort()
    return result
