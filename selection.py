from random import randint

a = [randint(1,1000) for i in range(20)]
#create new list
b = []
print("-"*5)
print("First status of the list: ", a)
while len(a) > 0:
    #find the minimum number
    minimum = 0
    for i in range(1,len(a)):
        if a[i] < a[minimum]:
            minimum = i
    #remove from the list, add it to a new list from low to high
    b.append(a.pop(minimum))
    

print("Last status of the list: ", b)
print("-"*5)