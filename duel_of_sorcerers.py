# Assign spell power lists to variables
gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]


# Assign 0 to each variable that stores the victories

gandalf_clashes_won = 0
saruman_clashes_won = 0

# Execution of spell clashes

for i in range(len(gandalf)):
    if gandalf[i] > saruman[i]:
        gandalf_clashes_won += 1
    else:
        saruman_clashes_won += 1

# We check who has won, do not forget the possibility of a draw.
# Print the result based on the winner.

if gandalf_clashes_won > saruman_clashes_won:
    print("Gandalf won")
elif gandalf_clashes_won < saruman_clashes_won:
    print("Saruman won")
else:
    print("Tie")
