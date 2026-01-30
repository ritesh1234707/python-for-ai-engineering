#integer 
#x = int(input ("what's x? "))
#y = int(input ("what's Y? "))

#print(x+y)

#float
#x = float(input ("what's x? "))
#y = float(input ("what's Y? "))

#z= round(x+y)

#print(f"{z:,}")

#print(round(x+y))

# x = float(input ("what's x? "))
# y = float(input ("what's Y? "))

# #z= round(x/y,2)

# #print(round(x/y,2))

# z = x/y

# print(f"{z:.5f}")

def main(): 
    x = int(input("what's x? "))
    print("x squard is ", square(x))

def square(n):
    return n*n

main()    
