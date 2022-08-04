
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
count = 0;  
text2 = open('input.txt', 'r').read()
for i in range (0, len (text2)):   
    #Checks whether given character is a punctuation mark  
    if text2[i] in punctuation:  
        count = count + 1;  
          
print ("Total number of punctuation characters exists in string: ");  
print (count);
  