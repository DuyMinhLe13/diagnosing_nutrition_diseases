import math
from configs import *
import numpy as np
def entropy(x, data, mode='habit'):
    counts = [0 for i in range(8 + 1)]
    for i in range(datasets_size):
        if mode == 'habit' and x in data['habits'][i]: counts[data['disease'][i]] += 1
        elif mode == 'symptom' and x in data['symptoms'][i]: counts[data['disease'][i]] += 1
    probs = [i / sum(counts) for i in counts]
    res = 0
    for prob in probs:
        if prob > 0: res -= prob * math.log(prob)
    return round(res, 3) + 0.1

def min_max_norm(lst):
    return [(i - min(lst))/(max(lst) - min(lst)) for i in lst]

def bayes_ran_gene():
    bayes_gene = {'habit': np.array(min_max_norm([1/entropy(i + 1, datasets) for i in range(num_habits)])),
                  'habit_weight': np.array([0.5]),
                  'symptom' : np.array(min_max_norm([1/entropy(i + 1, datasets, mode='symptom') for i in range(num_symptoms)])),
                  'symptom_weight': np.array([0.5])}
    return {'habit': np.round(np.clip(np.random.normal(bayes_gene['habit'], 0.25), 0, 1), 5),
            'habit_weight': np.round(np.clip(np.random.normal(bayes_gene['habit_weight'], 0.25), 0, 1), 5),
            'symptom': np.round(np.clip(np.random.normal(bayes_gene['symptom'], 0.25), 0, 1), 5),
            'symptom_weight': np.round(np.clip(np.random.normal(bayes_gene['symptom_weight'], 0.25), 0, 1), 5)}


def equal_ran_gene():
    equal_gene = {'habit': np.ones(num_habits)*0.5,
                  'habit_weight': np.array([0.5]),
                  'symptom': np.ones(num_symptoms)*0.5,
                  'symptom_weight': np.array([0.5])}
    return {'habit': np.round(np.clip(np.random.normal(equal_gene['habit'], 0.025), 0, 1), 5),
            'habit_weight': np.round(np.clip(np.random.normal(equal_gene['habit_weight'], 0.25), 0, 1), 5),
            'symptom': np.round(np.clip(np.random.normal(equal_gene['symptom'], 0.025), 0, 1), 5),
            'symptom_weight': np.round(np.clip(np.random.normal(equal_gene['symptom_weight'], 0.25), 0, 1), 5)}