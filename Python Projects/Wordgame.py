p1 = "akjhflkasjhdglkajhsdfa"
while len(p1) > 10:
    p1 = input("Enter a word with less that 10 letters: ")
print ("The number of letter input by player 1 is", len(p1))
for i in range (10):
    p2 = input("Enter a single letter: ")
    ltr_I = [i for i,n in enumerate(p1) if n == p2[0].lower()]
    if len(ltr_I)==0:
        print ("That letter is not in the word")
    #print (ltr_I)
    else:
        for j in range (len(ltr_I)):
            print ("It is letter numner {} in the word".format(ltr_I[j]+1))
            
        skip = input ("Do you want to enter the word now? [Y/N] ")
        if skip.upper() == 'Y':
            p2_word = input("What is the word entered by player 1? ")
            if (p2_word.lower()==p1):
                print ("That is the correct word. You win!")
                break
            else:
                print("Not quite")
                    
print ("You have now enteredd 10 letters")
p2_word = input("What is the word entered by player 1? ")
if (p2_word.lower()==p1):
    print ("That is the correct word. You win!")
else:
    print ("That is not the correct word. Player 1 win")

    

