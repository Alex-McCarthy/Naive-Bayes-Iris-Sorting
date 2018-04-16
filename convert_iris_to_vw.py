import csv
import sys
from collections import defaultdict
label_map = defaultdict(int)
features = ['a','b','c','d']
num_classes = 0;
with open("bezdekIris.data") as csvfile:
    iris_csv = csv.reader(csvfile, delimiter=',')
    for row in iris_csv:
        if len(row) == 0:
            break
        true_label = row[4].split("-")[1]
        if label_map[true_label] == 0:
            num_classes += 1
            label_map[true_label] = str(num_classes)
        sys.stdout.write(label_map[true_label])
        #sys.stdout.write(" " + true_label)
        sys.stdout.write(" | ")
        for k in range(0,4):
            sys.stdout.write(features[k] + ":" + row[k] + " ")
            #sys.stdout.write(row[k] + ":1 ")
        sys.stdout.write("\n")
