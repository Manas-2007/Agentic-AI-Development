# Accepts any number of positional arguments and pack them into a TUPLE......
def add(*args):
    print(f"Tuple Result : {args}")      
    total=0
    for x in args:
        total=total+x
    print(total)
    
add(10,20)
add(10,20,30,40,50)

# Accepts any number of keyword arguments and pack them into a DICTIONARY......
def Student_Info(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f"{key} : {value}")
        
Student_Info(Name="Manas",Class="10th",CGPA=9.5)
