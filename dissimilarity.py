import numpy as np

'''
    age: numeric
    height: numeric
    weight: numeric
    salary: numeric
    sex: binary, 1 represents male, 0 represents female
    is_married: binary
    ethnic: nominal
    hair_color: nominal
    eye_color: nominal
    education_background: ordinal
'''

if __name__ == '__main__':
    education_background_map = {}
    education_background_map['high school'] = 1
    education_background_map["bachelor's degree"] = 2
    education_background_map["master's degree"] = 3
    education_background_map["doctor's degree"] = 4
    M = 4

    person1 = [18,170,60,1000,1,0,'Asian','silver','black','high school']
    person2 = [32,175,80,90000,0,1,'African American','black','brown',"bachelor's degree"]
    person3 = [25,180,70,100000,1,0,'Asian','silver','blue',"master's degree"]
    attr_no = len(person1)

    persons = [person1, person2, person3]
    persons = np.array(persons)
    person_no = len(persons)

    dissimilarity = np.zeros(shape=(person_no,person_no))

    # compute distance of numeric attribute
    numeric_attr = np.array(persons[:,:4],dtype=float)
    minimal = np.min(numeric_attr, axis=0)
    maximal = np.max(numeric_attr, axis=0)
    diff = maximal - minimal
    for i in range(person_no):
        for j in range(i+1,person_no):
            distance = abs(numeric_attr[i] - numeric_attr[j])
            distance = distance / diff
            distance = np.sum(distance)
            dissimilarity[i,j] += distance
            dissimilarity[j,i] += distance

    # compute binary attribute and nominal
    for i in range(person_no):
        for j in range(i+1,person_no):
            distance = 0
            for k in range(4,9):
                if persons[i,k] != persons[j,k]:
                    distance += 1
            dissimilarity[i,j] += distance
            dissimilarity[j,i] += distance

    # compute ordinal attribute
    numeric_bg = np.zeros(shape=(person_no,))
    for i in range(person_no):
        bg = persons[i,9]
        numeric_bg[i] =  (education_background_map[bg] - 1) / (M - 1)
    max_bg = np.max(numeric_bg)
    min_bg = np.min(numeric_bg)
    diff = max_bg - min_bg
    for i in range(person_no):
        for j in range(i+1,person_no):
            distance = abs(numeric_bg[i] - numeric_bg[j])
            distance = distance / diff
            dissimilarity[i,j] += distance
            dissimilarity[j,i] += distance

    dissimilarity = dissimilarity / attr_no
    print(dissimilarity)