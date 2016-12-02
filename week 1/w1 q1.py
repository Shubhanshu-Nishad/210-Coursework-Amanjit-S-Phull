import random
def numberShuffler(li):                         #li is the parameter  
    for i in range(len(li)):
        position = random.randrange(i+1)        #gets a random number in the range of i+1
        toSwap = li[position]                   #store the variable to swap
        li[position] = li[i]                    #give random position the value in current loop
        li[i] = toSwap                          #give the position in the loop, random position value
    shufList = li
    return (shufList)

origArray = [1,2,5,6,7,8,9]
print(numberShuffler(origArray))
