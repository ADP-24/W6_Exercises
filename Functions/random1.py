import random

random.seed(1)

initialize_random = random.seed
initialize_random(1)

current_state = random.getstate
print("Current State:", current_state())

set_state = random.setstate
set_state(current_state())
print("State restored to initial state.")

get_random_bits = random.getrandbits
print("Random bits (10 bits):", get_random_bits(10))

random_range = random.randrange
print("Random number in range (1-10):", random_range(1,10))

random_integer = random.randint
print("Random integer between 5 and 15:", random_integer(5,15))

sequence = ["apple", "banana", "cherry", "peach", "plum", "watermelon"]
random_choice = random.choice
print("Random choice from list:", random_choice(sequence))

shuffle_sequence = random.shuffle
shuffle_sequence(sequence)
print("Shuffled list:", sequence)

random_sample = random.sample
print("Sample from list (k=3)", random_sample(sequence, k=3))

random_float = random.random
print("Random float between 0 and 1:", random_float())

random_uniform = random.uniform
print("Random float between 1.5 and 7.5:", random_uniform(1.5, 7.5))

random_triangular = random.triangular
print("Random triangular float (0, 5)", random_triangular(0, 5))

random_betavariate = random.betavariate
print("Random float based on Beta distribution:", random.betavariate(0.5, 0.5))

random_expovariate = random.expovariate
print("Random float based on Exponential distribution (ex=1.5):", random_expovariate(1.5))

random_gammavariate = random.gammavariate
print("Random float based on Gamma distribution (ex1=2, ex2=2):", random_gammavariate(2, 2))

random_gauss = random.gauss
print("Random float based on Gaussian distribution (ex1=0, ex2=1):", random_gauss(0, 1))

random_logormvariate = random.lognormvariate
print("Random float based on Log-Normal distibution (ex1=0, ex2=1)", random_logormvariate(0, 1))

random_normalvariate = random.normalvariate
print("Random float based on Normal distibution (ex1=0, ex2=1):", random.normalvariate(0,1))

random_vonmisesvariate = random.vonmisesvariate
print("Random float based on Von Mises distribution (ex1=0, ex2=1):", random_vonmisesvariate(0, 1))

random_paretovariate = random.paretovariate
print("Random float based on Pareto distribution (ex1=1):", random_paretovariate(1))

random_weibullarviate = random.weibullvariate
print("Random float based on Weibull distribution (ex1=1, ex2=1):", random_weibullarviate(1, 1))