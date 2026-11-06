#-------- NORMAL PYTHON FUNCTION ------------
def square(num):
    return num**2

number=int(input("Enter the Number : "))
print(square(number))

#-------- LAMBDA PYTHON FUNCTION -------------
square_result=lambda num: num*num
print(square_result(number))

product=lambda a,b: a+b
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
print(product(a,b))

cube_result=lambda num:num**3
print(f"Cube of {number} is {cube_result(number)}")

larger_result=lambda a,b: a if a>b else b
print("Larger number is",larger_result(a,b))

even_odd_result=lambda a : "Even" if a%2==0 else "Odd"
print(even_odd_result(number))