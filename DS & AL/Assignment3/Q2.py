def swap(x, y):
    return y, x


a = input("Enter first number: ")
b = input("Enter second number: ")

print("Before Swap a = ", a , " , b = " , b)

a , b = swap(a, b)

print("After Swap a = ", a , " , b = " , b)
