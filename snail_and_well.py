# Assign problem data to variables with representative names
# well height, daily advance, night retreat, accumulated distance

well_height = 125
daily_advance = 30
night_retreat = 20

# Assign 0 to the variable that represents the solution
accumulated_distance = 0
days = 0

# Write the code that solves the problem
while accumulated_distance < well_height:
    accumulated_distance += daily_advance
    days += 1
    if accumulated_distance < well_height:
        accumulated_distance -= night_retreat

# Print the result with print('Days =', days)

print("Days =", days)


