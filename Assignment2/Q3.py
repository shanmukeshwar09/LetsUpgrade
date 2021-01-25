from collections import Counter 

s = "Python is best for Machine Learning and Artificial Intelligence"
print(s);

count = Counter(s) 

print ("Count of e in the String is : " + str(count['e'])) 
