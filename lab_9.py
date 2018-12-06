#Lab 9
#1. Remember your Palindrome function from a homework problem before, I want you to enhance your
#program so it now can check to see if a phrase is a palindrome.
#Please note that these following phrases are palindromes
#- Are we not drawn onward, we few, drawn onward to new era? ...
#- Never odd or even. ...
#- Stressed desserts. ...
#- Maps, DNA, and spam. ...
#- Lonely Tylenol. ...
#- A man, a plan, a canal: Panama. ...
#- A nut for a jar of tuna.
#Program flow:
#1. Ask for a phrase
#2. Preprocess this phrase to get rid of spaces and punctuations
#3. Run your Palindrome function to determine if the phrase is a palindrome
#def Palindrome ...
#def PreProcess ...
#...
#phrase=input("Please enter a phrase:")
#new_phrase=PreProcess(phrase)
#Palindrome(new_phrase)

def palindrome():
    
    new_string = ""
    initial_phrase = input("Please enter a phrase: ")
    print("Intial Phrase: {}".format(initial_phrase))
    phrase = initial_phrase

    initial_phrase = initial_phrase.lower()

    for i in range(0, len(initial_phrase)):
        if ord(initial_phrase[i]) in range(97,123):
            new_string += initial_phrase[i]
        else:
            pass

    print("NEW STRING: {}".format(new_string))

    length = len(new_string)
    print("NEW STRING IS {} LETTERS LONG!".format(length))
    first = 0
    print("First: {}".format(first))
    last = length - 1
    print("Last: {}".format(last))

    for i in range(0, length - 1):
        if new_string[first] == new_string[last]:
            first += 1
            last -= 1
        else:
            print("The phrase is NOT a palindrone - sorry!")
            break

    print("Congratulations - Your phrase IS a palindrome!")

palindrome()


#2. Write a recursive function that accepts an integer, n, and prints the numbers 1 up through n.
#Rec_print(5)
#1
#2
#3
#4
#5

def rec_print(n):
    if n != 1:
        rec_print(n-1)
        print("n = {}".format(n))
    else:
        print("n = {}".format(n))
    
rec_print(5)

#3. Write a recursive function that accepts an integer argument, n. The function should display n lines of
#asterisks on the screen, with the first line showing 1 asterisk, the second line showing 2, up to the nth
#line showing n.
#Recur_asterisk(4)
#*
#**
#***
#****

def recur_asterisk(n):
    if n != 1:
        recur_asterisk(n - 1)
        print(n * "*")
    else:
        print(n * "*")
        return("n = {}".format(n))


recur_asterisk(4)