import random

from models.chromosome import Chromosome
from geneticAlgorithm.fitness import calculate_fitness


def generate_population(population_size, number_of_courses, number_of_slots):
    population = []
    for _ in range(population_size):
        genes = []
        for _ in range(number_of_courses):
            slot = random.randint(1, number_of_slots)
            genes.append(slot)
        chromosome = Chromosome(genes)
        population.append(chromosome)
    return population


def select_parent(population):

    total_fitness = 0

    for chromosome in population:

        total_fitness += chromosome.fitness

    random_point = random.uniform(0, total_fitness)

    current_sum = 0

    for chromosome in population:

        current_sum += chromosome.fitness

        if current_sum >= random_point:

            return chromosome


def crossover(parent1, parent2):

    crossover_point = random.randint(1, len(parent1.genes) - 1)

    child1_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]

    child2_genes = parent2.genes[:crossover_point] + parent1.genes[crossover_point:]

    child1 = Chromosome(child1_genes)

    child2 = Chromosome(child2_genes)

    return child1, child2


def mutate(chromosome, mutation_rate, number_of_slots):

    for index in range(len(chromosome.genes)):

        if random.random() < mutation_rate:

            chromosome.genes[index] = random.randint(1, number_of_slots)

    return chromosome


def run_genetic_algorithm(
    students, courses, slots, population_size, generations, mutation_rate
):

    population = generate_population(population_size, len(courses), len(slots))

    best_chromosome = None

    best_fitness_history = []

    for generation in range(generations):

        for chromosome in population:

            calculate_fitness(chromosome, students, courses, slots)

        current_best = max(population, key=lambda chromosome: chromosome.fitness)

        best_fitness_history.append(current_best.fitness)

        if best_chromosome is None or current_best.fitness > best_chromosome.fitness:

            best_chromosome = current_best

        new_population = []

        while len(new_population) < population_size:

            parent1 = select_parent(population)

            parent2 = select_parent(population)

            child1, child2 = crossover(parent1, parent2)

            mutate(child1, mutation_rate, len(slots))

            mutate(child2, mutation_rate, len(slots))

            new_population.append(child1)

            if len(new_population) < population_size:

                new_population.append(child2)

        population = new_population

    return best_chromosome, best_fitness_history
