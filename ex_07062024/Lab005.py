num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
result = int(num1) + int(num2)      # type conversion str to int
print(result)
print(type(result))

# format of string
first_name = "Harry"
last_name = "Porter"
print(first_name+ " "+ last_name)
print(first_name, last_name)
# f is for formatting. It will replace the values of variables in the string.
print(f"Your full name is {first_name} {last_name}")
