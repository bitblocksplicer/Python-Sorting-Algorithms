from random import randint

#creating a list that contains random numbers of specified range
a= [randint(1,1000) for i in range(20)]
print(a)
#create a copy of this list to compare at the end
b = a.copy()
#the comparison will take place for every element of the list, so we will set the range equals to the length of the list
for i in range(len(a)):
    #we need another loop for every element comparison cycle. Since we should get the negative index of comparing element, It
    #must start from the number "1"
    for j in range(1, len(a)):
        #if current number is lower than its previous one, swap will begin.
        if a[-(j)] < a[-(j+1)]:
            #create a temporary list
            temp = []
            #define the current element
            currentelement = a[-(j)]
            #define the new element
            willbeswappedelement = a[-(j+1)]
            temp.append(currentelement)
            #added current element to our temporary list, so we can safely remove it from the main list now.
            a.pop(-j)
            #time to insert removed element into the other element's index
            a.insert(a.index(willbeswappedelement), currentelement)
            #clearing the temporary list
            temp.clear
            print("swapped!")
            print(a)
        else:
            # if it's not lower, then do nothing
            pass
            print("passed!")
            print(a)
            
print("-"*5)  
print("First status of the list: ", b)          
print("Last status of the list: ", a)
print("-"*5)            