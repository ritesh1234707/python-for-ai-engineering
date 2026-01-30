# x = int(input("what's x "))

# if x % 2 == 0: 
#     print("Even")

# else: 
#     print("Odd")


def main(): 
    x = int(input("What's x "))
    
    if is_even(x):
        print("even")

    else:
        print("odd")


# def is_even(n):
#     if n % 2 == 0:
#         return True
    
#     else:
#         return False

'''Crazy thing that only happens in python
instead of writing the code up there 👆
we can just simply do this 👇'''

# def is_even(n):

#     return True if n % 2 == 0 else False

'''We can further shorten this code, '''

def is_even(n):
    return n % 2 == 0 

    
main()