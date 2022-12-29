import random

def bogosort(list):
    for i in range(len(list)):
        if i < len(list) - 1:
            if list[i] <= list[i + 1]:
                pass
            else:
                print("list not sorted, reshuffle:", list)
                return False
        else:
            return True


a = list(random.randint(1, 1000) for i in range(8))
#creating loop, until find the sorted shuffle
while True:
    #shuffle it
    random.shuffle(a)
    #creating control mechanism to check whether it's sorted or not
    #if our function returned False (not sorted), it will keep shuffling it
    if bogosort(a) == False:
        continue
    #if it's returned True, print the result and break the loop
    else:
        print("list sorted!")
        print(a)
        break
