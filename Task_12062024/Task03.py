# Program for Factorial Series

n = int(input("Enter the number: "))
factorial = 1
if n < 0:
    print("Factorial for negative number does not exist")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, n+1):      # 1, 2, 3, 4, 5, 6
        factorial = factorial*i
    print("The factorial of", n , "is", factorial)

