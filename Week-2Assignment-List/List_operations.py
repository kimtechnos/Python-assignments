# 1:creat and empty list
my_list = []
# 2:Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3: Insert 15 at the second position
my_list.insert(1,15)

# 4: Extend the lsit with another list [50,60,70]
my_list.extend([50,60,70])

# 5:Remove the last element
my_list.pop()
# 6: Sort the list in ascending order 
my_list.sort()
# 7:Find the index of value 30
index_30 = my_list.index(30)
print(f"The index of 30 in my list is:{index_30}")

print("Final my_list",my_list)