from data_loader import *
import matplotlib.pyplot as plt

from geneticAlgorithm.genetic_algorithm import run_genetic_algorithm

students = load_students()
courses = load_courses()
slots = load_slots()

best_solution, history = run_genetic_algorithm(
    students, courses, slots, population_size=100, generations=200, mutation_rate=0.05
)

print("\nBest Fitness:")
print(best_solution.fitness)

print("\nBest Genes:")
print(best_solution.genes)


print("\nFinal Schedule")

for index, course in enumerate(courses):

    slot_number = best_solution.genes[index]

    slot = slots[slot_number - 1]

    print(course.course_code, "->", slot.slot_id)

plt.plot(history)

plt.title("GA Convergence")

plt.xlabel("Generation")

plt.ylabel("Fitness")

plt.grid(True)

plt.show()
