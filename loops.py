# i = 3 
# while i != 0:
#     print("bark")
#     i = i - 1 

# i = 0 
# while i < 3:
#     print("bark")
#     i += 1

'''for loop'''

# for i in [0, 1, 2]:
#     print("meow")


# for _ in range(7):
#     print("bark")

'''This code is not practical, cause we're only 
printing three lines, what if we had to print thousands.

That's why our next approach will be to use a 
function.'''

def main():
    while True: 
        x = int(input("say your word "))
        if x > 0:
            break
        else:
            print("Give a positive integer")
    word(x)

def word(n):
   for _ in range(n):
       print("meow")


main()

'''The code up there 👆 is my approach of printing meow
how many times the user wants using "functions". 

Now let's see what david has done.'''

# def main(): 
#     number = get_number()
#     meow(number)

# def get_number(): 
#     while True: 
#         n = int(input("What's n? "))
#         if n > 0: 
#             break
#     return n
    
# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()


