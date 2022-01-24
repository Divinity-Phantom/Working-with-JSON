import json
import csv
from pprint import pprint
from collections import OrderedDict
from operator import getitem
import pandas as pd

with open("assignment.json") as file:
    data=json.load(file)

fname="output.csv"

with open(fname, "w") as file:
    csv_file=csv.writer(file)
    csv_file.writerow(["subcategory","title","price","popularity"])
        
    for key,value in data['products'].items():

        
        csv_file.writerow([value['subcategory'],value['title'],value['price'],value['popularity']])
        

csvData=pd.read_csv('output.csv')
csvData.sort_values(['popularity'],axis=0,ascending=False,inplace=True)

print(csvData[['title','price']])


