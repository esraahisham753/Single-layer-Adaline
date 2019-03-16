import matplotlib.pyplot as plot
import numpy as np
import tkinter
import Functions

filepath = "IrisData.txt"
with open(filepath, 'r') as fr:
    Lines = fr.readlines()

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

plot.figure('X1 X2')
plot.scatter(Class1_X1_features, Class1_X2_features)
plot.scatter(Class2_X1_features, Class2_X2_features)
plot.scatter(Class3_X1_features, Class3_X2_features)
plot.xlabel('X1')
plot.ylabel('X2')
#plot.show()

plot.figure('X1 X3')
plot.scatter(Class1_X1_features, Class1_X3_features)
plot.scatter(Class2_X1_features, Class2_X3_features)
plot.scatter(Class3_X1_features, Class3_X3_features)
plot.xlabel('X1')
plot.ylabel('X3')
#plot.show()

plot.figure('X1 X4')
plot.scatter(Class1_X1_features, Class1_X4_features)
plot.scatter(Class2_X1_features, Class2_X4_features)
plot.scatter(Class3_X1_features, Class3_X4_features)
plot.xlabel('X1')
plot.ylabel('X4')
#plot.show()

plot.figure('X2 X3')
plot.scatter(Class1_X2_features, Class1_X3_features)
plot.scatter(Class2_X2_features, Class2_X3_features)
plot.scatter(Class3_X2_features, Class3_X3_features)
plot.xlabel('X2')
plot.ylabel('X3')
#plot.show()

plot.figure('X2 X4')
plot.scatter(Class1_X2_features, Class1_X4_features)
plot.scatter(Class2_X2_features, Class2_X4_features)
plot.scatter(Class3_X2_features, Class3_X4_features)
plot.xlabel('X2')
plot.ylabel('X4')
#plot.show()

plot.figure('X3 X4')
plot.scatter(Class1_X3_features, Class1_X4_features)
plot.scatter(Class2_X3_features, Class2_X4_features)
plot.scatter(Class3_X3_features, Class3_X4_features)
plot.xlabel('X3')
plot.ylabel('X4')
#plot.show()

#bngrab
#X3 X4
#C1 C2
Class1_Class2_feature3 = Class1_X3_features[0:30] + Class2_X3_features[0:30]
Class1_Class2_feature4 = Class1_X4_features[0:30] + Class2_X4_features[0:30]

Final_weights = Functions.Perceptron_Learning_Algorithm(Class1_Class2_feature3, Class1_Class2_feature4, 1, 2, 0)

Functions.Show_Learned_Classes(Final_weights, Class1_Class2_feature3, Class1_Class2_feature4)
