data=[34,78,12,56,89]

# .append() (add element at the end of the array)
data.append(100)
print(f"After Append : {data}")

# .sort() (ascending sorting by default)
data.sort()
print("Ascending Sort :",data)

data.sort(reverse=True)
print("Descending sort :",data)

# .reverse() (reverse the array)
data=[34,78,12,56,89]
data.reverse()
print("Reversed array :",data)

# .insert(idx,element)
data.insert(1,"Manas")
print("After Insertion :",data)

# .remove(value) : (removes that specific value from Left Side)
print('\nBefore Removal :',data)
data.remove(78)
print("After Remove Method :",data)

# .pop(idx) : Remove a value at specific idx
data.pop(1)
print("\nAfter pop (Removing Manas):",data)