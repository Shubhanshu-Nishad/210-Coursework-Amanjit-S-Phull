def PrimeChecker(n, divisor):
    if (divisor == n):                   #Base case when n is not divible by any number from 2 
        return "It is a prime number"
    if (n % divisor == 0):               #Checking if it has a remainder of any number
        return "It is not a prime number"
    return (PrimeChecker(n, divisor+1))  #Increase the divisor by one each call

print(PrimeChecker(11,2))
