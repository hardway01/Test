a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [even for even in a if even %2 == 0]
c = [neven for neven in a if neven %2 == 1]

print (a)
print (b)
print(c)