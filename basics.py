#This is a comment in python
#

x = 15
print("Exercise 1")
if x % 5 == 0 and x % 3 == 0:
    print ("Rock Star")
elif x % 3 == 0:
    print ("Rock")
elif x % 5 == 0:
    print("Star")

print("Exercise 2")

x = [1,2,3,4,5]
l = len(x)
print("length: ",l)
print("last num: ",x[-1])
for i in range(l):
    print(x[i])

print("Exercise 3")

print("Begin: ",x)
x.append(6)
print("Append 6: ",x)
x.remove(4)
print("Remove 4: ",x)
x.extend([7,8,9])
print("Extend [7,8,9]",x)
x.insert(0,0)
print("Insert 0 at index 0: ",x)
