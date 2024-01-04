from configs import *
from dataset import *
def fitness_function(gene):
    accuracy = 0
    for i in range(8, datasets_size):
        max_score = 0
        patient = 0
        for j in range(datasets_size):
            if i == j: continue
            habit_score = 0
            for habit in datasets['habits'][i]:
                if habit in datasets['habits'][j]: habit_score += gene['habit'][habit - 1]
            symptom_score = 0
            for symptom in datasets['symptoms'][i]:
                if symptom in datasets['symptoms'][j]: symptom_score += gene['symptom'][symptom - 1]
            score = gene['habit_weight'].item() * habit_score + gene['symptom_weight'].item() * symptom_score
            if score > max_score:
                max_score = score
                patient = j
        predict = datasets['disease'][patient]
        if predict == datasets['disease'][i]: accuracy += 1
    accuracy = accuracy / (datasets_size - 8)
    return accuracy