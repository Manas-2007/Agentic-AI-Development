info={
    "Id":101,
    "Name":"Manas Patidar",
    "Roll":"BTIR25O1029",
    "IsPass":True,
    "Subjects":{
        "Maths":56,
        "Science":100,
        "Hindi":52,
        "Grades":['C','A','C']
    }
}

print(info)
print(info["Subjects"])
print(info["Subjects"]["Grades"])
print(info["Subjects"]["Grades"][1])

# .keys() method (print all the keys)
print("\nTesting .keys() Method : ")
print(info.keys())

# .values() method (print values)
print("\nTesting .values() method : ")
print(info.values())

# .items() method (print key,value pairs)
print("\nTesting .items() Method : ")
print(info.items())
for key,value in info.items():
    print(key,":",value)

# .update() method (insert key-values pairs in the dictionary)
print("\nTesting the update() method : ")
print("Original Dict :",info)
info.update({"City":"Khargone","CGPA":9})
info["Surname"]="Patidar"
print("New Dict :",info)


