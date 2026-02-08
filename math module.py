import math
def sqaure(a):
    return math.sqrt(a)
def log(a):
    return math.log(a)
def sin(a):
     b=math.sin(a)
     return math.radians(b)
num=int(input("Enter a number"))
print(f"Square of {num} is {sqaure(num)}")
print(f"Logarithm of {num} is {log(num)}")
print(f"Sin of {num} is {sin(num)}")
