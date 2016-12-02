def sentenceReverser(s):
    words = s.split(' ')            #Create a list of words
    i = len(words) - 1              #i is the index in the list
    sen = ""                        
    while i >= 0:
        sen += words[i] + " "       #Start adding into the string from the last element in the list
        i -= 1                      
    return sen                      
sentence = "This is awesome"
print (sentenceReverser(sentence))
