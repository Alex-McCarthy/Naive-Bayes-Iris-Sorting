pred_file = open("./predictions.txt")
true_file = open("./test_data.vw")
correct = 0.0
total = 0.0
for pred_line in pred_file:
    true_line = true_file.readline()
    if pred_line[0] == true_line[0]:
        correct += 1
    total += 1
print(str(correct / total))
