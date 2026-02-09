# def hello():
#     print("hello")


# name = input("what's your name? ")
# hello()
# print(name)

# so up there 👆 is use of function but there was no use of parameters in there. 

# def hello(to):
#     print("hello,", to)

# name = input("what's your name? ")

# hello(name)

#up there 👆 we used parameters or arguments in the code which is "to" and in to the name is assisined.

def hello(to="world"): 
    print("hello, ",to)

hello()

name = input("What's your name? ")   

hello(name)
hello(name)
hello(name)
hello(name)
hello(name)

#up there 👆 is the same code but in this we have a default value set for "to" which is World.

# def main():
#     name = input ("What's your name? ")
#     hello(name)


# def hello(to):
#     print("hello, ", to)


# main()