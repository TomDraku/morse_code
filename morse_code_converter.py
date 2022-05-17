import os
import time


# create a dictionary 
morse_alphabet = {'a':'·−','b':'−···','c':'−·−·','d':'−··','e':'·','f':'··−·','g':'−−·','h':'····',
'i':'··','j':'·−−−','k':'−·−','l':'·−··','m':'−−','n':'−·','o':'−−−','p':'·−−·','q':'−−·−','r':'·−·',
's':'···','t':'−','u':'··−','v':'···−','w':'·−−','x':'−··−','y':'−·−−','z':'−−··','0':'−−−−−','1':'·−−−−',
'2':'··−−−','3':'···−−','4':'····−','5':'·····','6':'−····','7':'−−···','8':'−−−··','9':'−−−−·',' ':'/'
}

# cerate a funcion to clear terminal
clear = lambda: os.system('cls')


# function to convert list of  morse code characters to string
def listToString(my_list):
    my_string = ''
    for element in my_list:
        my_string += element+ ' '
    return my_string
        


# creating a while loop to ensure the continuous operation of the program
find_characters = False
while find_characters == False:
    
    # welcome message, user input a text, 
    print('Morse Code Translator')
    word = input_text = input('Enter text to translate: ').lower()
    # replacing the entered sentence to a list of alphabetic and numeric characters
    processed_word = list(word)
    try:
        # I am trying to change alphabetic characters and numbers to a morse code characters using for loop and dictionary properties 
        new_word = []
        for letter in processed_word:
            new_word.append(morse_alphabet[letter])
    except KeyError:
        # exception when user give an invalid character
        print("Sorry, only letters in the alphabet, try again")
        time.sleep(3)       
        clear()
    else:
        # function to convert list of  morse code characters to string
        print(listToString(new_word))
        # asking the user for further action
        prog_continuation = input('Do you want to trnaslate another word: yes or no: ').lower()
        if prog_continuation == 'yes':
            find_characters = False
            time.sleep(0.2)       
            clear()
        elif prog_continuation == 'no':
            find_characters = True
        else:
            print('Wrong answer. The program will close')
            find_characters = True
            time.sleep(2)       
            clear()
            






