# using slicing
def reverse_slicing(func):
    return func[:: -1]

input_str = "Sakshi"
print("Reverse using Slicing = ", reverse_slicing(input_str))


#using loop
def reverse_loop(func):
    new_list = ""
    for i in func:
        new_list = i + new_list
    return new_list

input_str1 = "Ram"
print("Reverse using Slicing = ", reverse_loop(input_str1))

#using Reverse
def reverse_list(func):
    temp_list = list(func)
    temp_list.reverse()
    return ''.join(temp_list)


input_str2 = "RaM"
print("Reverse using Slicing = ", reverse_list(input_str2))
