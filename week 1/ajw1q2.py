def countTrailing(x):
    numZeros=0                      #variable storing 0s count
    while x > 0:                    
        x = x/5                     #floor division 
        numZeros = numZeros + x     #count floor division of x and 5

    return numZeros
print(countTrailing(10))
 
