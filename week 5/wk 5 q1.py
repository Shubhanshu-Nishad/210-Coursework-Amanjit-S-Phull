seq = [1, 2,7,6,6,7, 4, 7, 5,7,8,9,91, 9, 4 ]
longestFirst = -1
length = 0
longestLength = 0
for i in range(len(seq)):
        if (i + 1 == len(seq)):                                  #Checking if the next value is the end of the sequence
                if (length > longestLength):
                        longestLength = length                   #Store the current longest sequence length
                        longestFirst = i - longestLength         #Select the index to start searching through sequence 
                        break
        elif (seq[i] < seq[i+1]):
                length += 1                                      #increase length if it is ascending
        elif (length >= longestLength):
                longestLength = length
                longestFirst = i - length                        #Store the current longest sequence length
                length = 0                                       #Continue checking the sequence
for i in range(longestFirst, longestFirst + longestLength+1):    #Print the sub-sequence based on where it starts
        print(seq[i])
