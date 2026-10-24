str1="this is a dummy string."
str2="But let me verify it first...."

# .concate() : Used to join the true strings
result=str1+" "+str2
print("Final String :",result)

# .capitalize() : first letter uppercase of string
print(str1.capitalize())
print("Original String :",str1)

# .replace(old,new) : replace the string characters
print(str1.replace('t','*'))
print("Original String :",str1)

# .count() : print the occurance of the given string
print(str2.count('e'))
print(str1.count('dummy'))

# .join() : used to join multiple strings with SEPARATOR (list->string)
lists=["Manas","Pooja","Muskan"]
result="-".join(lists)
print(result)

# .split() : divide the single string into list of strings (string->list)
string="Hello I am Manas Patidar"
list_data=string.split()
print(list_data)
d2=" ".join(list_data)
print("Restored original data :",d2)