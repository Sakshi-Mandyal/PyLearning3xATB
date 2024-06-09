# List
my_list = [1, 2, 3, "Four", "Hi", 2.0]
print(my_list)
print(my_list[0])
print(my_list[-1])
print(type(my_list))

my_list.append("True")
print(my_list)

my_list.insert(1,5)
print(my_list)

my_list.extend(["Name", 5])    # extends a list by adding multiple elements
print(my_list)

my_list.remove(5)
print(my_list)

print(my_list.pop())
print(my_list.index(1))
my_list.reverse()
print(my_list)
#my_list.sort()

my_list[3] = "Five"
print(my_list)