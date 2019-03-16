import numpy as np

def Main(class1, class2, feature1, feature2):
    filepath = "IrisData.txt"
    with open(filepath, 'r') as fr:
        Lines = fr.readlines()
    first_feature = []
    first_feature_1 = []
    second_feature = []
    second_feature_1 = []

    labels = []
    X1_features = []
    X2_features = []
    X3_features = []
    X4_features = []

    Lines.remove(Lines[0])

    for line in Lines:
        splitted_line = line.split(',')
        X1_features.append(float(splitted_line[0]))
        X2_features.append(float(splitted_line[1]))
        X3_features.append(float(splitted_line[2]))
        X4_features.append(float(splitted_line[3]))
        labels.append(splitted_line[4])

    Class1_X1_features = []
    Class1_X2_features = []
    Class1_X3_features = []
    Class1_X4_features = []
    Class2_X1_features = []
    Class2_X2_features = []
    Class2_X3_features = []
    Class2_X4_features = []
    Class3_X1_features = []
    Class3_X2_features = []
    Class3_X3_features = []
    Class3_X4_features = []

    for i in range(150):
        if i < 50:
            Class1_X1_features.append(X1_features[i])
            Class1_X2_features.append(X2_features[i])
            Class1_X3_features.append(X3_features[i])
            Class1_X4_features.append(X4_features[i])
        if i < 100 and i > 49:
            Class2_X1_features.append(X1_features[i])
            Class2_X2_features.append(X2_features[i])
            Class2_X3_features.append(X3_features[i])
            Class2_X4_features.append(X4_features[i])
        if i > 99:
            Class3_X1_features.append(X1_features[i])
            Class3_X2_features.append(X2_features[i])
            Class3_X3_features.append(X3_features[i])
            Class3_X4_features.append(X4_features[i])

    if class1 == 'C1' :
        if feature1 == 'X1':
            first_feature = Class1_X1_features
        if feature1 == 'X2':
            first_feature = Class1_X2_features
        if feature1 == 'X3':
            first_feature = Class1_X3_features
        if feature1 == 'X4':
            first_feature = Class1_X3_features
        if feature2 == 'X1':
            second_feature = Class1_X1_features
        if feature2 == 'X2':
            second_feature = Class1_X2_features
        if feature2 == 'X3':
            second_feature = Class1_X3_features
        if feature2 == 'X4':
            second_feature = Class1_X3_features

    if class1 == 'C2' :
        if feature1 == 'X1':
            first_feature = Class2_X1_features
        if feature1 == 'X2':
            first_feature = Class2_X2_features
        if feature1 == 'X3':
            first_feature = Class2_X3_features
        if feature1 == 'X4':
            first_feature = Class2_X3_features
        if feature2 == 'X1':
            second_feature = Class2_X1_features
        if feature2 == 'X2':
            second_feature = Class2_X2_features
        if feature2 == 'X3':
            second_feature = Class2_X3_features
        if feature2 == 'X4':
            second_feature = Class2_X3_features

    if class1 == 'C3' :
        if feature1 == 'X1':
            first_feature = Class3_X1_features
        if feature1 == 'X2':
            first_feature = Class3_X2_features
        if feature1 == 'X3':
            first_feature = Class3_X3_features
        if feature1 == 'X4':
            first_feature = Class3_X3_features
        if feature2 == 'X1':
            second_feature = Class3_X1_features
        if feature2 == 'X2':
            second_feature = Class3_X2_features
        if feature2 == 'X3':
            second_feature = Class3_X3_features
        if feature2 == 'X4':
            second_feature = Class3_X3_features

    if class2 == 'C1' :
        if feature1 == 'X1':
            first_feature_1 = Class1_X1_features
        if feature1 == 'X2':
            first_feature_1 = Class1_X2_features
        if feature1 == 'X3':
            first_feature_1 = Class1_X3_features
        if feature1 == 'X4':
            first_feature_1 = Class1_X3_features
        if feature2 == 'X1':
            second_feature_1 = Class1_X1_features
        if feature2 == 'X2':
            second_feature_1 = Class1_X2_features
        if feature2 == 'X3':
            second_feature_1 = Class1_X3_features
        if feature2 == 'X4':
            second_feature_1 = Class1_X3_features

    if class2 == 'C2' :
        if feature1 == 'X1':
            first_feature_1 = Class2_X1_features
        if feature1 == 'X2':
            first_feature_1 = Class2_X2_features
        if feature1 == 'X3':
            first_feature_1 = Class2_X3_features
        if feature1 == 'X4':
            first_feature_1 = Class2_X3_features
        if feature2 == 'X1':
            second_feature_1 = Class2_X1_features
        if feature2 == 'X2':
            second_feature_1 = Class2_X2_features
        if feature2 == 'X3':
            second_feature_1 = Class2_X3_features
        if feature2 == 'X4':
            second_feature_1 = Class2_X3_features

    if class2 == 'C3' :
        if feature1 == 'X1':
            first_feature_1 = Class3_X1_features
        if feature1 == 'X2':
            first_feature_1 = Class3_X2_features
        if feature1 == 'X3':
            first_feature_1 = Class3_X3_features
        if feature1 == 'X4':
            first_feature_1 = Class3_X3_features
        if feature2 == 'X1':
            second_feature_1 = Class3_X1_features
        if feature2 == 'X2':
            second_feature_1 = Class3_X2_features
        if feature2 == 'X3':
            second_feature_1 = Class3_X3_features
        if feature2 == 'X4':
            second_feature_1 = Class3_X3_features



    return first_feature, second_feature, first_feature_1, second_feature_1
