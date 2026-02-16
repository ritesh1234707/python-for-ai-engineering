with open("file2.csv") as file: 
    for line in file: 
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")


''' EAsier version '''

''' In this split is returning a list with two variables so 
we don't have to then store it in a another list called 
"row" instead we can do this:'''

with open("file2.csv") as file: 
    for line in file: 
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

''' Now let's sort it '''

characters = []

with open("file2.csv") as file:
    for line in file: 
        name, house = line.rstrip().split(",")
        characters.append(f"{name} is in {house}") 
    
for character in sorted(characters, reverse=True): 
    print(character)



        
