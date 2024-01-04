from configs import *
from funcs import *
from fitness import *
from crossover import *
from mutation import *


generation = []
# init first generation
bayes_gene = {'habit': np.array(min_max_norm([1/entropy(i + 1, datasets) for i in range(num_habits)])),
          'habit_weight': np.array([0.5]),
          'symptom' : np.array(min_max_norm([1/entropy(i + 1, datasets, mode='symptom') for i in range(num_symptoms)])),
          'symptom_weight': np.array([0.5])}
equal_gene = {'habit': np.ones(num_habits)*0.05,
          'habit_weight': np.array([0.5]),
          'symptom': np.ones(num_symptoms)*0.05,
          'symptom_weight': np.array([0.5])}
bayes_ran_genes = [bayes_ran_gene() for i in range(124)]
equal_ran_genes = [equal_ran_gene() for i in range(124)]
generation = [bayes_gene] + bayes_ran_genes + [equal_gene] + equal_ran_genes

num_loops = 10
for loop in range(num_loops):

    # Selection
    generation.sort(key=fitness_function, reverse=True)
    parents = generation[:10]
    print(f'loop {loop} : ', [round(fitness_function(gene), 3) for gene in parents])

    new_generation = []
    new_generation += parents

    # CrossOver
    for i in range(60):
        sample_parents = random.sample([i for i in range(10)], 2)
        new_generation.append(cross_over(parents[sample_parents[0]], parents[sample_parents[1]]))

    # Mutation
    for i in range(60):
        sample_parents = random.sample([i for i in range(10)], 1)
        new_generation.append(mutation(parents[sample_parents[0]]))

    # Mutation base parents
    new_generation += mutation_advance(parents, 60)

    new_generation += [equal_ran_gene() for i in range(60)]
    generation = new_generation

print(generation[0])