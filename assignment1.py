num = int(input("Enter a number to compute the factorial:"))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(num))