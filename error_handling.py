# try:
#     x = int(input("What's x?"))
#     print(f"x is {x}")
# except ValueError:
#     print("X is not an interger")

''' It is good but it is a good practice to 
put as low line of code as possible. In this 
case it is two but try to reduce it.'''

# while True:
#     try:
#         x = int(input("What's x?"))     
#     except ValueError:
#         print("X is not an interger")
#     else:
#         break

# print(f"X is {x}")

''' We can do this as well'''

# while True:
#     try:
#         x = int(input("What's x?"))
#         break     
#     except ValueError:
#         print("X is not an interger")

# print(f"X is {x}")

''' Using functuion'''

# def main(): 
#     x = get_int()
#     print(f"X is {x}")


# def get_int():
#     while True: 
#         try: 
#             x = int(input("What's x? "))
#         except ValueError: 
#             print("x is not an integer.")
#         else: 
#             return x
    

# main()

''' So in here we are using break to break from the loop 
and then returning the value of x, but it turns out that 
return is stronger than break it will not only return the 
value of x but it'll also break you out of the loop 
so instead of using the break we can directely use the return 
and then shorten our code.'''

''' In down here is a more compact and short code 
but 'it can' be a little complicated so the code up there
is also fine.'''

# def main(): 
#     x = get_int()
#     print(f"X is {x}")


# def get_int():
#     while True: 
#         try: 
#             return int(input("What's x? "))
#         except ValueError: 
#             print("x is not an integer.")
       
    

# main()

''' There is an another keyword called pass so insted 
of print 'x is not an integer' after the user inputs a string 
instead of an integer we can just use the keywork "pass" to ignore the 
wrong input.'''

# def main(): 
#     x = get_int()
#     print(f"X is {x}")


# def get_int():
#     while True: 
#         try: 
#             return int(input("What's x? "))
#         except ValueError: 
#             pass
       
    

# main()

''' Now let's use parameters.'''

def main(): 
    x = get_int("What's x? ")
    print(f"X is {x}")


def get_int(promt):
    while True: 
        try: 
            return int(input(promt))
        except ValueError: 
            pass
       
    

main()

