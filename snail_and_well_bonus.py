# Assign problem data to variables with representative names
# well height, daily advance, night retreat, accumulated distance

import statistics

well_height = 125
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
night_retreat = 20

# Assign 0 to the variable that represents the solution
accumulated_distance = 0
days = 0
max_displacement = 0
avg_progress = 0

# Write the code that solves the problem
while accumulated_distance < well_height:
    accumulated_distance += advance_cm[days]
    days += 1
    if accumulated_distance < well_height:
        accumulated_distance -= night_retreat

# Print the result with print('Days =', days)

print("Days =", days)


# What is its maximum displacement in a day? And its minimum?

max_displacement = max(advance_cm)
print(max_displacement)

# What is its average progress?

avg_progress = sum(advance_cm)/len(advance_cm)
print(avg_progress)

# What is the standard deviation of your displacement during the day?
# Using Statistics

standard_deviation = statistics.stdev(advance_cm)
print(standard_deviation)

# Calculating
i = 0
add = 0
dif = 0
square = 0
while i < len(advance_cm):
    dif = advance_cm[i] - avg_progress
    square = dif ** 2
    add = add + square
    i += 1

standard_deviation_calculated = (add / (len(advance_cm)-1)) ** (1/2)

print(standard_deviation_calculated)
