def deleteVowel(i,word, noVowel):                           #i acts as the string index 
    vowels = ["a","e","i","o","u","A","E","I","O","U"]              
    isVowel = False
    for vowel in vowels:
        if vowel == word[i]:
            isVowel = True                                  #Stops the character from being added to noVowel
            break
    if isVowel == False:
        noVowel += word[i]                                  #adds the character to noVowel string if it is not a vowel
    if i == len(word)-1:                                    #When i has reached the end of the string
        return noVowel
    else:
        return deleteVowel(i+1, word, noVowel)              #increase the index each call
print(deleteVowel(0,"helloE",""))
