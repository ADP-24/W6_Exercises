import random
import math
import statistics

vals1_100 = range(1,100) 
vals_sample = random.sample(vals1_100, 75) 
vals_choices = random.choices(vals1_100, k = 200)
radius = random.randint(3,10)  
pi = math.pi 

radius_up = random.randint(3, 10)
radius_down = random.randint(3, 10)

area_up = math.pi * (radius_up ** 2)
area_down = math.pi * (radius_down ** 2)

area_up_rounded = math.ceil(area_up)
area_down_rounded = math.ceil(area_down)

sum_sample = sum(vals_sample)
average_sample = sum_sample / len(vals_sample)
median_sample = statistics.median(vals_sample)

average_choices = sum(vals_choices) / len(vals_choices)
median_choices = statistics.median(vals_choices)
mode_choices = statistics.mode(vals_choices)
std_dev_choices = statistics.stdev(vals_choices)
variance_choices = statistics.variance(vals_choices)

print("\nExperimenting with a subset of integers 1-100:")
print("Sum of 75 sample values from 1 to 100:", sum_sample)
print("Average of 75 sample values:", average_sample)
print("Median of 75 sample values:", median_sample)

print("\nExperimenting with a superset of 200 values, integers 1-100:")
print("Average of 200 values:", average_choices)
print("Median of 200 values:", median_choices)
print("Mode of 200 values:", mode_choices)
print("Standard deviation of 200 values:", std_dev_choices)
print("Variance of 200 values:", variance_choices)

print("\nModeling a random circle:")
print(f"Radius = {radius_up}, area = {area_up_rounded}")
print(f"Radius = {radius_down}, area = {area_down_rounded}")