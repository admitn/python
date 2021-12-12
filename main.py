import csv
import json

path = 'test.json'
path2 = 'test2.json'

arr = []
with open(path, 'r') as f:
    data = json.load(f)
arr.append(data.values())

with open(path2, 'r') as f:
    data2 = json.load(f)
arr.append(data2.values())

with open('test.csv', 'w') as f:
    csv_wr = csv.writer(f)
    csv_wr.writerow(data)
    for i in arr:
        csv_wr.writerow(i)