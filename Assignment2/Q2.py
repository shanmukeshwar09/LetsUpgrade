# Program to remove duplicate words in a String

str = "LetsUpgrade is best for learning best Python"
l = str.split() 
k = []

for i in l: 
	if (str.count(i) > 1 and (i not in k) or str.count(i) == 1): 
		k.append(i)

print(' '.join(k))
