from random import random, shuffle, sample, seed, choice, randint
from icecream import ic

N = 10
seed(42)

OBJECTS = {n for n in range(N)}
SETS = tuple(frozenset(sample(range(N), k=s+1)) for s in range(N))
COSTS = tuple(10*random()+(s+random())**2 for s in range(N))


ic(OBJECTS)
ic(SETS)
ic(COSTS)

XCOSTS={SETS[i]: COSTS[i] for i in range(N)}

def fitness_sos(solution: set[frozenset]) -> float:
    weight=sum(XCOSTS[s] for s in solution)
    check= frozenset.union(*solution)
    assert check== frozenset(range(N))
    return -weight

def tweak(solution: set[frozenset]) -> set[frozenset]:
    new = solution.copy()
    if len(new) == len(SETS):
        return new
    for _ in range(randint(1, 5)):
        old = choice(tuple(new))
        replacement = choice(tuple(set(SETS) - new))
        new.remove(old)
        new.add(replacement)
    if set().union(*new) == OBJECTS:
        return new
    return solution

solution_best = {SETS[-1]}
for _ in range(50):
    solution = {SETS[-1]}
    solution.update(sample(SETS[:-1], randint(1, N-2)))
    for _ in range(1000):
        new_solution = tweak(solution)

        if fitness_sos(new_solution) > fitness_sos(solution):
            solution = new_solution
    if fitness_sos(solution) > fitness_sos(solution_best):
        solution_best = solution.copy()
ic(solution_best)
ic(-fitness_sos(solution_best))