import random
import queue

import numpy as np

from sortedcontainers import SortedList

from genetic_algorithm.Individual import Individual


class Genetic_algorithm(object):

    def __init__(self,
                 goal_score : int,
                 max_number_of_children: int,
                 population_limit: int,
                 crossover_chromosoma_probability: float,
                 tournament_size: int,
                 mutation_probability : float,
                 mutation_chromosoma_probability: float,
                 max_pixel_value: int,
                 strongest_rate = 0.2
                 ):
        self.__goal_score = goal_score
        self.__population = SortedList()
        self.__new_population = queue.deque()
        self.__population_limit = population_limit
        self.__tournament_size = tournament_size
        self.__crossover_chromosoma_probability = crossover_chromosoma_probability
        self.__mutation_probability = mutation_probability
        self.__mutation_chromosoma_probability = mutation_chromosoma_probability
        self.__strongest_limit = int(strongest_rate * population_limit)
        self.__max_number_of_children = max_number_of_children
        self.__high_boundary_of_pixel = max_pixel_value + 1

    def reset(self):
        self.__goal = None
        self.__population = SortedList()
        self.__new_population = queue.deque()
        self.__number_of_chromosomes = 0

    def setGoal(self, goal : object):
        self.__goal = goal
        self.__number_of_chromosomes = len(goal)


    def run_algorithm(self):
        self.__generate_initial_population()
        self.__recombination()
        first_best_solution = self.__population[0]
        is_solved = self.__evaluate()
        while not is_solved:
            winners = self.__selection_tournament()
            self.__new_population = queue.deque(self.__crossover(winners))
            self.__mutation()
            self.__recombination()
            is_solved = self.__evaluate()
        return self.__population[0],first_best_solution

    def __selection_tournament(self):
        selected_individuals = queue.deque(random.sample(self.__population[self.__strongest_limit:], self.__tournament_size))
        winners = queue.Queue()
        while(len(selected_individuals) > 1):
            individual_A = selected_individuals.pop()
            individual_B = selected_individuals.pop()

            if(individual_A < individual_B):
                winners.put(individual_A)
            else:
                winners.put(individual_B)
        return winners

    def __crossover(self,winners):
        winners_shuffle = queue.deque(random.sample(self.__population[:self.__strongest_limit], self.__tournament_size))
        children = list()
        while (len(winners_shuffle) > 1):
            individual_A = winners_shuffle.pop()
            individual_B = winners_shuffle.pop()

            number_of_children = int(random.uniform(0, self.__max_number_of_children))

            [children.append(self.__crossover_individuals(individual_A,individual_B)) in range(number_of_children)]
        return children

    def __crossover_individuals(self, individual_A, individual_B):
        children_list = list()
        for chromosoma_A, chromosoma_B in zip(individual_A.get_dna(),individual_B.get_dna()):
            is_crossover = random.uniform(0, 1) < self.__crossover_chromosoma_probability

            if is_crossover:
                new_chromosoma = int((chromosoma_A + chromosoma_B) * 0.5)
                children_list.append(new_chromosoma)
            else:
                chromosoma_to_add = chromosoma_A if random.uniform(0, 1) < 0.5 else chromosoma_B
                children_list.append(chromosoma_to_add)
        return Individual(np.array(np.array(children_list)))

    def __mutation(self):
        for individual in self.__population:
            is_mutation = random.uniform(0, self.__high_boundary_of_pixel) < self.__mutation_probability

            if is_mutation:
                mutated = self.__mutate_individual(individual)
                self.__new_population.append(mutated)

    def __mutate_individual(self, individual):
        mutated_individual = list()
        for chromosoma in individual.get_dna():
            is_mutation_chromosoma = random.uniform(0, 1) < self.__mutation_chromosoma_probability

            if is_mutation_chromosoma:
                new_chromosoma = int(random.uniform(0, self.__high_boundary_of_pixel))
                mutated_individual.append(new_chromosoma)
            else:
                mutated_individual.append(chromosoma)
        return Individual(np.array(mutated_individual))

    def __recombination(self):
        while len(self.__new_population) > 0:
            new_individual = self.__new_population.pop()
            new_individual.set_score(self.__evaluate_individual(new_individual))
            self.__population.add(new_individual)

        self.__population = SortedList(self.__population[:self.__population_limit])

    def __evaluate_individual(self, individual):
        return np.sum(np.abs(np.subtract(individual.get_dna(),self.__goal)))

    def __evaluate(self):
        return self.__population[0].get_score() < self.__goal_score

    def __generate_initial_population(self):
        for i in range(self.__population_limit):
            new_dna = np.random.randint(self.__high_boundary_of_pixel, size=len(self.__goal))
            new_individual = Individual(new_dna)
            self.__new_population.append(new_individual)

















