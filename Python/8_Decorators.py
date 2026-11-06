#---------DECORATOR PROTOTYPE------------
def calculation_decorator(func):
    def wrapper(num):
        print("Calculation Started.....")
        result=func(num)
        print(result)
        print("Calculation Finished.....")
    return wrapper

#---------FUNCTION 1 -------------
@calculation_decorator
def square(num):
    return num**2

#--------FUNCTION 2 -------------
@calculation_decorator
def even_odd(num):
    if(num%2==0):
        return "Even"
    else:
        return "Odd"

#----------------CALLING OF THE DECORATORS-----------
square(5)
print("\n\n")
even_odd(45)
    