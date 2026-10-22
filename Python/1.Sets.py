# SET IS MUTABLE IN NATURE BUT ITS ELEMENTS ARE IMMUTABLE IN NATURE

my_set={1,2,3,4,5,1,2,3,4}
print("Original Set :",my_set)
print("Length of the Set",len(my_set))

# Concept
my_set1={}
my_set2=()
my_set3=set()
print(f"Type of set 1 : {type(my_set1)}")
print(f"Type of set 2 : {type(my_set2)}")
print(f"Type of set 3 : {type(my_set3)}")

# Add method (add exactly one element in the set)
my_set.add(56)
my_set.add((2,3,4,5))
print(f"Add Method : {my_set}")

# Update Method (used to add multiple elements in the set)
my_set.update((57,58))
my_set.update({67,43,89,23,45})
print(f"Update Method : {my_set}")

# Remove method ( used to remove the elements from the given set)
my_set.remove(56)
print(f"Remove Method : {my_set}")

# Clear method (used to empty the entire set)
my_set.clear()
print(f"Clear Method : {my_set}")

# Pop Method ( Used to remove a random element from the set)
my_set={1,2,3,4,5,6}
num=my_set.pop()
num2=my_set.pop()
print("Pop Method :",num,num2)

# Union Method (set1 | set2)
set1={1,2,3,4,5}
set2={"manas","gora",1,2}
union_result=set1.union(set2)
print("Union Result : ",union_result)

# Intersection Method (set1 & set2)
Intersection_result=set1.intersection(set2)
print("Intersection Result : ",Intersection_result)

# Difference (set - set2)
Difference=set1.difference(set2)
print("Difference (Set1 - Set2) : ",Difference)
print("Difference (Set2 - Set1) : ",set2-set1)


# isdisjoint() method (Checks is both sets are different or not)
x={45,22,89}
y={1,2,3}
print("Disjoint Status : ",x.isdisjoint(y))

# issubset() 
x={1,2,3,4}
y={1,2}
print("Subset Status : ")
print(y.issubset(x))
print(x.issubset(y))

# issuperset() 
print("Superset Status : ")
print(x.issuperset(y))
print(y.issuperset(x))