class Sum:

    def findsum(self, a, b):
        s = a + b
        return s


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

obj = Sum()
s = obj.findsum(a, b)

print("Sum is:", s)
