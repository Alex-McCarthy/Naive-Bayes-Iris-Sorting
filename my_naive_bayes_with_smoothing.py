import csv
import sys
from collections import defaultdict
training_dict = defaultdict(lambda:defaultdict(list))
num_classes = 0;
features = ['a','b','c','d']
#setosa = a | versicolor = b | virginica = c
a_setosa_count = 0
b_versicolor_count = 0
c_virginica_count = 0
prediction_list = []
predictions_made = -1
accuracy = 0
with open("training_data.txt") as csvfile:
    iris_csv = csv.reader(csvfile, delimiter=',')
    for row in iris_csv: #this loop splits the training data into 
        if len(row) == 0:
            break
        true_label = row[4].split("-")[1]
        if true_label == "setosa":
            a_setosa_count += 1
            for k in range(0,4):
                training_dict[features[0]][features[k]].append(float(row[k]))
        if true_label == "versicolor":
            b_versicolor_count += 1
            for k in range(0,4):
                training_dict[features[1]][features[k]].append(float(row[k]))
        if true_label == "virginica":
            c_virginica_count += 1
            for k in range(0,4):
                training_dict[features[2]][features[k]].append(float(row[k]))
                
total_count = a_setosa_count + b_versicolor_count + c_virginica_count


with open("test_data.txt") as csvfile: #opens training_test_data by default, this is different than the final test data.
    iris_csv = csv.reader(csvfile, delimiter=',')
    #this is iris type a, b, c
    for row in iris_csv:#splits test data
        f_c_a = [1, 1, 1, 1, 1, 1, 1, 1] #count of equal features for first 4 positions, count of total features for second for positions.
        f_c_b = [1, 1, 1, 1, 1, 1, 1, 1]
        f_c_c = [1, 1, 1, 1, 1, 1, 1, 1]
        bayes_percentage = [0.0, 0.0, 0.0]
        feature_list = [0.0, 0.0, 0.0, 0.0, "a"]
        if len(row) == 0:
            break
        for k in range(0,4):
            feature_list[k] = float(row[k])
        flower_type = "z"
        if row[4].split("-")[1] == "setosa":
            flower_type = "a"
        elif row[4].split("-")[1] == "versicolor":
            flower_type = "b"
        elif row[4].split("-")[1] == "virginica":
            flower_type = "c"
        feature_list[4] = flower_type
        for i in range(0,3): #this loop counts the number of times a feature occurs in a class
            for k in range(0,4):
                for z in training_dict[features[i]][features[k]]:
                    if feature_list[k] == z:
                        if i == 0:
                            f_c_a[k] += 1
                        if i == 1:
                            f_c_b[k] += 1
                        if i == 2:
                            f_c_c[k] += 1
                    if i == 0:
                        f_c_a[k+4] += 1
                    if i == 1:
                        f_c_b[k+4] += 1
                    if i == 2:
                        f_c_c[k+4] += 1
            if i==0:
                bayes_percentage[i]=(f_c_a[0]/f_c_a[4])*(f_c_a[1]/f_c_a[5])*(f_c_a[2]/f_c_a[6])*(f_c_a[3]/f_c_a[7])*(1/3)
            if i==1:
                bayes_percentage[i]=(f_c_b[0]/f_c_b[4])*(f_c_b[1]/f_c_b[5])*(f_c_b[2]/f_c_b[6])*(f_c_b[3]/f_c_b[7])*(1/3)
            if i==2:
                bayes_percentage[i]=(f_c_c[0]/f_c_c[4])*(f_c_c[1]/f_c_c[5])*(f_c_c[2]/f_c_c[6])*(f_c_c[3]/f_c_c[7])*(1/3)
        for i in range(0,3):
            if bayes_percentage[i] == max(bayes_percentage):
                prediction_list.append(features[i])
                predictions_made += 1
        if prediction_list[predictions_made] == feature_list[4]:
            accuracy += 1
total_accuracy = accuracy/(predictions_made+1)
sys.stdout.write(str(total_accuracy))
