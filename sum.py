num1=int(input("First Number:"))           #To the Point
num2=int(input("Second Number:"))
num3=num1+num2
print(f"The Sum of {num1} and {num2} is {num3}")
#Instead above method we can create one function

def sums(a,b):
  return a+b

c=sums(2,3)
print(c)
