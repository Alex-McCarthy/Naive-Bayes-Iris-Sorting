vw -i iris.model -t -p ./predictions.txt < test_data.vw
python accuracy.py
