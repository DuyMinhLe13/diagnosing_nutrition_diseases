from configs import *
from collect_data import *
from cbr import *
import numpy as np
best_gene = {'habit': np.array([0.09447, 0.03031, 0.10995, 0.09319, 0.04454, 0.00077, 0.02783,
                                0.09535, 0.04079, 0.0353 , 0.01487, 0.04108, 0.04906, 0.03645,
                                0.02507, 0.08733, 0.03268, 0.06411, 0.0673 , 0.06052, 0.07131,
                                0.05664, 0.03934]),
             'habit_weight': np.array([0.50692]),
             'symptom': np.array([0.06071   , 0.08637   , 0.08025   , 0.05714   , 0.08171   ,
                                  0.02815   , 0.02206   , 0.04111   , 0.03868   , 0.01836   ,
                                  0.02835   , 0.05447   , 0.0407    , 0.0337    , 0.81825995,
                                  0.08821   , 0.03134   , 0.0435    , 0.07683   , 0.08029   ,
                                  0.0147    , 0.03528   , 0.06829   , 0.04641   , 0.023     ,
                                  0.07554   , 0.03267   ]),
             'symptom_weight': np.array([0.35408])} # 0.88 acc


data = collect_data()
if len(data[0]) < 1 and len(data[1]) < 1: print('Bạn không có bệnh dinh dưỡng')
else:
    predict_disease = matching_case(data, best_gene)
    solution(predict_disease)