# variables

stops = [(5, 0), (3, 4), (2, 1), (2, 4)]

# 1. Calculate the number of stops.

number_stop = len(stops)
print("The number of stops is", number_stop)

# 2. Assign a variable a list whose elements are the number of passengers in each stop:
# Each item depends on the previous item in the list + in - out.

list_passenger = [0, 0, 0, 0]
passengers=0
for i in range(len(stops)):
    passengers += stops[i][0] - stops[i][1]
    list_passenger[i] = passengers

print("The list of passenger is", list_passenger)

# 3. Find the maximum occupation of the bus.
print ("The maximum occupation of the bus is", max(list_passenger))


# 4. Calculate the average occupation. And the standard deviation.

average = sum(list_passenger)/len(list_passenger)
print("The average is", average)

i = 0
add = 0
dif = 0
square = 0
while i < len(list_passenger):
    dif = list_passenger[i] - average
    square = dif ** 2
    add = add + square
    i += 1

standard_deviation_calculated = (add / (len(list_passenger)-1)) ** (1/2)

print("The standard deviation is", standard_deviation_calculated)





