# Write a Python program to print all Prime numbers in an Interval.

lower = int(input("Input lower limit : "))
upper = int(input("Input upper limit : "))

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
