# names = []


# for _ in range(3)  : 
#     names.append(input("what's your name? "))

''' So first we created an empty list and then we 
assigned the names in that empty list using loops.'''

''' Now we're sorting them alpabetically.'''

# names = []

# for _ in range(3)  : 
#     names.append(input("what's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")

''' So if i run this program again the names that i just saved will be lost 
so that's why we use file i/o'''

''' open function'''

# name = input("what's your name? ")  

# file = open("file.txt", "w")
# file.write(name)
# file.close

''' So in this code the open function allows us to store the data 
in a file named file.txt and the work for w is to give permission to 
create and write in that file, So it'll store the data.'''

''' But there's a problem in this, while "w" can create the file it'll also 
recreate the files again and again everytime we'll run the code, so instead we'll 
use "a" for append so it'll apand the names in the file and store all of them.'''


# name = input("what's your name? ")  

# file = open("file.txt", "a",)
# file.write(f"{name}\n")
# file.close

''' With function'''

name = input("what's your name? ")  

with open("file.txt", "a",) as file:
    file.write(f"{name}\n")
