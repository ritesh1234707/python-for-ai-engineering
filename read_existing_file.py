# with open("file.txt", "r") as file: 
#     lines = file.readlines()

# # for line in lines: 
# #     print(f"Hello,", line, end="")

''' Or'''

# for line in lines: 
#     print(f"Hello,", line.rstrip())

''' So in this code frist i'm opeing the file using the with function
and then reading the lines and storing them in the "lines" variable
and then iterating over each lines and then printing them.'''

''' Here is a simpler version'''

# with open("file.txt", "r") as file:
#     for line in file: 
#         print("hello,", line.rstrip())

''' So in python we can just simply first open the file and then 
in the for loop it'll atomatically read all the lines and then print it.'''

''' Now let's sort them '''

# names = []

# with open("file.txt", "r") as file:
#     lines = file.readlines()

# for line in lines: 
#     names.append(line)

# for line in sorted(names):
#     print("hello,", line.rstrip())

'''Practice'''
 

# names = []

# with open("file.txt",) as file: # deafult is "r"
#     lines = file.readlines()

# for line in lines:
#     names.append(line)

# for line in sorted(names): 
#     print("hello,", line.rstrip())

''' this is how David did it'''

# names = []

# with open("file.txt") as file: 
#     for line in file: 
#         names.append(line.rstrip())

# for name in sorted(names): 
#     print("hello,", name)

''' There's another way that we can do this with more 
compact manner.'''


# with open("file.txt") as file:
#     for line in sorted(file): 
#         print("hello,", line.rstrip()) 

''' now let's sort it in reverse order.'''

names = []

with open("file.txt") as file: 
    for line in file: 
        names.append(line.rstrip())

for name in sorted(names, reverse=True): 
    print("hello,", name) 



