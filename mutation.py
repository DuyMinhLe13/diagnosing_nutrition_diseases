import random
import numpy as np
from configs import *
def mutation(gene):
    res = {'habit': [], 'habit_weight': 0, 'symptom': [], 'symptom_weight': 0}
    for i in range(num_habits):
        if random.random() < 0.1: res['habit'].append(random.random())
        else: res['habit'].append(gene['habit'][i])

    if random.random() < 0.1: res['habit_weight'] = np.array([random.random()])
    else: res['habit_weight'] = gene['habit_weight']

    for i in range(num_symptoms):
        if random.random() < 0.1: res['symptom'].append(random.random())
        else: res['symptom'].append(gene['symptom'][i])

    if random.random() < 0.1: res['symptom_weight'] = np.array([random.random()])
    else: res['symptom_weight'] = gene['symptom_weight']

    res['habit'] = np.array(res['habit'])
    res['symptom'] = np.array(res['symptom'])

    return res

def mutation_advance(parents, num_genes):
    habit_mean = [sum([parent['habit'][i] for parent in parents])/len(parents) for i in range(23)]
    habit_weight_mean = sum([parent['habit_weight'] for parent in parents])/len(parents)
    symptom_mean = [sum([parent['symptom'][i] for parent in parents])/len(parents) for i in range(27)]
    symptom_weight_mean = sum([parent['symptom_weight'] for parent in parents])/len(parents)

    genes = []
    for i in range(num_genes):
        genes.append({'habit': np.round(np.clip(np.random.normal(habit_mean, 0.25), 0, 1), 5),
                      'habit_weight': np.round(np.clip(np.random.normal(habit_weight_mean, 0.25), 0, 1), 5),
                      'symptom': np.round(np.clip(np.random.normal(symptom_mean, 0.25), 0, 1), 5),
                      'symptom_weight': np.round(np.clip(np.random.normal(symptom_weight_mean, 0.25), 0, 1), 5)})
    return genes