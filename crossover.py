import random
import numpy as np
from configs import *
def cross_over(gene1, gene2):
    gene = {'habit': [], 'habit_weight': 0, 'symptom': [], 'symptom_weight': 0}
    for i in range(num_habits):
        if random.random() < 0.5: gene['habit'].append(gene1['habit'][i])
        else: gene['habit'].append(gene2['habit'][i])

    if random.random() < 0.5: gene['habit_weight'] = gene1['habit_weight']
    else: gene['habit_weight'] = gene2['habit_weight']

    for i in range(num_symptoms):
        if random.random() < 0.5: gene['symptom'].append(gene1['symptom'][i])
        else: gene['symptom'].append(gene2['symptom'][i])

    if random.random() < 0.5: gene['symptom_weight'] = gene1['symptom_weight']
    else: gene['symptom_weight'] = gene2['symptom_weight']

    gene['habit'] = np.array(gene['habit'])
    gene['symptom'] = np.array(gene['symptom'])

    return gene