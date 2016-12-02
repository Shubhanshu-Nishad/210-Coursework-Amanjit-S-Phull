def perfectSquare(n):
    for i in range(n):
        if(i*i > n):                   #excutes when the square of i is greater than the number
            n = (i-1) *(i-1)           #Gets the previous square value of i
            break                      #Exists the loop
    return(n)
print(perfectSquare(5)) 
