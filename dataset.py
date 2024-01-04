import pandas as pd
import re

dataframe1 = pd.read_excel('data/data.xlsx')

datasets = dict()
datasets['habits'] = []
datasets['symptoms'] = []
datasets['disease'] = []
for habit in dataframe1.habit:
    try: datasets['habits'].append(list(map(int, re.findall(r'\d+', habit))))
    except: datasets['habits'].append([])

for symptom in dataframe1.symptom:
    try: datasets['symptoms'].append(list(map(int, re.findall(r'\d+', symptom))))
    except: datasets['symptoms'].append([])

for disease in dataframe1.disease:
    datasets['disease'].append(list(map(int, re.findall(r'\d+', disease)))[0])
