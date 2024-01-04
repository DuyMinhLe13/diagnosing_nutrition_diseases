from configs import *
from dataset import *
def matching_case(data, gene):
    max_score = 0
    patient = 0
    for j in range(datasets_size):
        habit_score = 0
        for habit in data[0]:
            if habit in datasets['habits'][j]: habit_score += gene['habit'][habit - 1]
        symptom_score = 0
        for symptom in data[1]:
            if symptom in datasets['symptoms'][j]: symptom_score += gene['symptom'][symptom - 1]
        score = gene['habit_weight'].item() * habit_score + gene['symptom_weight'].item() * symptom_score
        if score > max_score:
            max_score = score
            patient = j
    predict = datasets['disease'][patient]
    return predict