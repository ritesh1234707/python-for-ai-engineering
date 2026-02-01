# import sys

# print("hello, my name is", sys.argv[1])

''' In the code yp there we can give input in the terminal 
itself so if we try to execute this code in terminal
by typing this: "python using_sys.py Ritesh", It would 
pirnt "hello, my name is Ritesh". '''

''' But there's a cache here if you don't give any 
argument in this case Ritesh along with the file name
it would thourgh Indexerror. '''


''' So we can solve this by using except or if else function.'''

# import sys

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError: 
#     print("Too few arguments")

''' But in this case if the user doesn't give any 
argument then it will show "too few arguments" 
but if the user gives more than one argumetn then it 
will just show one argument because in the list of array
we past [1] so in the [0]th index we have the file name
and in the [1]st index we have our argument. That's why 
it's only showing one argument.'''

''' In order to fix this we can use If else. '''

import sys 

# Check for error
# if len(sys.argv) < 2:
#     print("Too few arguments")

# elif len(sys.argv) > 2: 
#     print("Too many arguments")

# # Print name tags
# print("hello, my name is", sys.argv[1])

''' It'll show error '''

''' Let's see what we can do to fix this'''

''' There's a function called sys.exit in sys we'll use that'''

# import sys

# if len(sys.argv) < 2: 
#     sys.exit("Too few arguments")

# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")   

# print("hello, my name is", sys.argv[1])

''' So what sys.exit did is, if it matches the requirments
then it'll print and exit then and there so it'll not 
run the full code below that so we will not get an 
IndexError because of the too few arguments or many arguments.'''

# import sys

# if len(sys.argv) < 2: 
#     sys.exit("Too few arguments") 
     
# for arg in sys.argv: 
#     print("hello, my name is", arg)

''' It is ok but it also prints the first argument 
that is the file name itself, so have to cut that.'''

''' We'll do this by using Slice function.'''

# import sys

# if len(sys.argv) < 2: 
#     sys.exit("Too few arguments") 
     
# for arg in sys.argv[1:]: 
#     print("hello, my name is", arg)

''' By adding 1: it'll give us the arrgument starting form 
number 1 not 0 it'll slice off and start from number 1 and 
then the rest. ''' 

''' And if we want to remove one from the last we can
just simply add -1 at the last: [1:-1]'''

import sys

if len(sys.argv) < 2: 
    sys.exit("Too few arguments") 
     
for arg in sys.argv[1:-1]: 
    print("hello, my name is", arg)



 