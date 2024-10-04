#exercise 1
list = [2,3,-5,1,2,55,23,22,-7]

print("The mean of the list is:")
print(sum(list)/len(list))


#exercise 2

poz=[]
neg=[]

for x in list:
    if x>=0:
        poz.append(x)
    else:
        neg.append(x)

print("Positive numbers:")
print(poz)
print("Negative numbers:")
print(neg)



#exercise 3

print("The sum of the first n-2 numbers is:")
print(sum(list[:-2]))


#exercise 4

print("The elements from odd positions are:")
print(list[1::2])


#exercise 5
list.sort()
print("The minimum of the list is:")
print(list[0])