def Greet(name):
    return name

def add_numbers(a,b):
    return a+b

def Greater_number(a,b):
    if(a>b):
        return a
    else:
        return b

def average(list_data):
    total=0
    for i in range(len(list_data)):
        total=total+list_data[i]

    average=total/len(list_data)
    return int(average)
#===========================FUNCTIONS CALLINGS====================================
username=input("Enter username :")
result=Greet(username)
print(f"Welcome, {result}! Welcome to Python functions..")

num1=int(input("Enter First Number : "))
num2=int(input("Enter second number : "))
result=add_numbers(num1,num2)
print(f"Sum :",result)

result=Greater_number(num1,num2)
print("Greater Number :",result)

marks_list=[]
marks=int(input("Enter number of marks : "))
for i in range(marks):
    score=int(input(f"Mark {i+1} : "))
    marks_list.append(score)

print("Original Mark List :",marks_list)
avg=average(marks_list)
print(f"The average marks are {avg}")
