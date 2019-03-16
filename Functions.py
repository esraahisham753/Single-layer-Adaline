import numpy as np
import matplotlib.pyplot as plot
import Edited
import pickle


def Perceptron_Learning_Algorithm(feature1, feature2, no_epochs, eta, bias_or_not, mse):
    bias_input = 0
    input_list = []
    labels_list = []
    for i in range(60):
        if i < 30:
            labels_list.append(1)
        else:
            labels_list.append(-1)

    if bias_or_not != 0:
        random_weights = np.random.uniform(low = 0, high = 1, size = (3, 1))
    else:
        random_weights = np.random.uniform(low = 0, high = 1, size = (2, 1))

    for i in range(no_epochs):
        squared_error = 0
        for j in range(60):
            input_list = []
            if bias_or_not != 0:
                bias_input = 1
                input_list.append(bias_input)
                input_list.append(feature1[j])
                input_list.append(feature2[j])
            else:
                input_list.append(feature1[j])
                input_list.append(feature2[j])
            net_weight = np.dot(input_list, random_weights)
            signum_output = signum(net_weight)
            if signum_output != labels_list[j]: #update weight
                loss = labels_list[j] - signum_output
                dot_product_result = np.dot((eta * loss), input_list)
                if bias_or_not != 0 :
                    dot_product_result = dot_product_result.reshape(3, 1)
                else :
                    dot_product_result = dot_product_result.reshape(2, 1)
                new_weight = random_weights + dot_product_result
                random_weights = new_weight
        for j in range(60):
            input_list = []
            if bias_or_not != 0:
                bias_input = 1
                input_list.append(bias_input)
                input_list.append(feature1[j])
                input_list.append(feature2[j])
            else:
                input_list.append(feature1[j])
                input_list.append(feature2[j])
            net_weight = np.dot(input_list, random_weights)
            signum_output = signum(net_weight)
            loss = labels_list[j] - signum_output
            squared_error = squared_error + (loss * loss)
        mse_error = (1/120) * squared_error
        print(mse_error)
        if(mse_error < mse):
            break
    return random_weights

def signum(value):
    if value > 0:
        return 1
    if value < 0:
        return -1
    if value == 0:
        return 0


def Show_Learned_Classes(weights, feature1, feature2):
    plot.figure('Learned classes')
    plot.scatter(feature1[0:50], feature2[0:50])
    plot.scatter(feature1[50:100], feature2[50:100])
    plot.xlabel('X3')
    plot.ylabel('X4')
    x_max_1 = max(feature1[0:50])
    x_max_2 = max(feature1[50:100])
    x1 = max(x_max_1, x_max_2)
    x_min_1 = min(feature2[0:50])
    x_min_2 = min(feature2[50:100])
    x2 = min(x_min_1, x_min_2)
    y1 = ((-(weights[1] * x1) - weights[0])) / (weights[2])
    y2 = ((-(weights[1] * x2) - weights[0])) / (weights[2])
    plot.plot([x2, x1], [y2, y1])
    plot.show()
    return 1


def display_plot(c1, c2, f1, f2):
    weights = []
    feature11, feature12, feature21, feature22 = Edited.Main(c1, c2, f1, f2)
    with open('learnedweight.tmp', 'rb') as rw:
        weights = pickle.load(rw)
    feature1 = feature11 + feature21
    feature2 = feature12 + feature22
    Show_Learned_Classes(weights, feature1, feature2)

def train(c1, c2, f1, f2, m, eta, b, mse ):
    feature11, feature12, feature21, feature22 = Edited.Main(c1, c2, f1, f2)
    slic_f1 = feature11[0:30] + feature21[0:30]
    slic_f2 = feature12[0:30] + feature22[0:30]
    learned_weights = Perceptron_Learning_Algorithm(slic_f1, slic_f2, m, eta, b, mse)
    with open('learnedweight.tmp', 'wb') as w:
        pickle.dump(learned_weights, w)

def test(c1, c2, f1, f2, b):
    feature11, feature12, feature21, feature22 = Edited.Main(c1, c2, f1, f2)
    slic_f1 = feature11[30:50] + feature21[30:50]
    slic_f2 = feature12[30:50] + feature22[30:50]
    weights = []
    with open('learnedweight.tmp', 'rb') as w:
        weights = pickle.load(w)
    labels_list = []
    for i in range(40):
        if i < 20:
            labels_list.append(1)
        else:
            labels_list.append(-1)
    accuracy = 0
    c1_c1 = 0
    c1_c2 = 0
    c2_c1 = 0
    c2_c2 = 0
    for i in range(0, 20):
        input_list = []
        if b != 0:
            bias_input = 1
            input_list.append(bias_input)
            input_list.append(slic_f1[i])
            input_list.append(slic_f2[i])
        else:
            input_list.append(slic_f1[i])
            input_list.append(slic_f2[i])
        net_weight = np.dot(input_list, weights)
        signum_output = signum(net_weight)
        if(signum_output == labels_list[i]):
            accuracy += 1
            c1_c1 += 1
        else:
            c1_c2 += 1
    for i in range(20, 40):
        input_list = []
        if b != 0:
            bias_input = 1
            input_list.append(bias_input)
            input_list.append(slic_f1[i])
            input_list.append(slic_f2[i])
        else:
            input_list.append(slic_f1[i])
            input_list.append(slic_f2[i])
        net_weight = np.dot(input_list, weights)
        signum_output = signum(net_weight)
        if(signum_output == labels_list[i]):
            accuracy += 1
            c2_c2 += 1
        else:
            c2_c1 += 1
    accuracy = (accuracy / 40) * 100
    confusion = [
        [c1_c1, c1_c2],
        [c2_c1, c2_c2]
    ]
    print(accuracy)
    print(confusion)



