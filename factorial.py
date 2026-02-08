def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
num=input("enter a number")
result=fact(int(num))
print(f"the factorial of {num} is {result}")