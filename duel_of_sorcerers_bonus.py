# Assign spell power lists to variables
POWER = {
    'Fireball': 50,
    'Lightning bolt': 40,
    'Magic arrow': 10,
    'Black Tentacles': 25,
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball',
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles',
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']

# 2. A sorcerer wins if he succeeds in winning 3 spell clashes in a row.
# Execution of spell clashes
# check for 3 wins in a row
# check the winner
gandalf_won = False
saruman_won = False

for i in range(1, len(gandalf)-1):
    if (POWER[gandalf[i]] > POWER[saruman[i]]) & (POWER[gandalf[i-1]] > POWER[saruman[i-1]]) & (POWER[gandalf[i+1]] > POWER[saruman[i+1]]):
        print("Gandalf won")
        gandalf_won = True
        break
    elif (POWER[gandalf[i]] < POWER[saruman[i]]) & (POWER[gandalf[i-1]] < POWER[saruman[i-1]]) & (POWER[gandalf[i+1]] < POWER[saruman[i+1]]):
        print("Saruman won")
        saruman_won = True
        break

if saruman_won | gandalf_won == 0:
   print("Nobody won")

# 3. Average of each of the spell lists.
add = 0
for i in range(len(gandalf)):
    add += POWER[gandalf[i]]
    average_gandalf = add/len(gandalf)

print("The Gandalf average is", average_gandalf)

add = 0
for i in range(len(saruman)):
    add += POWER[saruman[i]]
    average_saruman = add/len(saruman)

print("The Saruman average is", average_saruman)

# 4. Standard deviation of each of the spell lists.

add = 0
dif = 0
square = 0
for i in range(len(gandalf)):
    dif = POWER[gandalf[i]] - average_gandalf
    square = dif ** 2
    add = add + square
    i += 1

standard_deviation_calculated = (add / (len(gandalf)-1)) ** (1/2)

print("The Gandalf standard deviation is",standard_deviation_calculated)

add = 0
dif = 0
square = 0
for i in range(len(saruman)):
    dif = POWER[saruman[i]] - average_saruman
    square = dif ** 2
    add = add + square
    i += 1

standard_deviation_calculated = (add / (len(saruman)-1)) ** (1/2)

print("The Saruman standard deviation is",standard_deviation_calculated)


