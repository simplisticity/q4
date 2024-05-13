# design the hangman/user interface

def none():
    return '''

                Lives Remaining: 9





_____
'''

def stand():
    return '''

 |              Lives Remaining: 8
 |
 |
 |              Only one wrong guess, it's okay!
 |
 |
_|___
'''

def upper():
    return '''
 ________
 |/             Lives Remaining: 7
 |     
 |
 |              Only two wrong guesses, it's okay!
 |
 |
_|___
'''

def string():
    return '''
 ________
 |/     |       Lives Remaining: 6
 |
 |
 |              There's still time to recover!
 |
 |
_|___
'''

def head():
    return '''
 ________
 |/     |       Lives Remaining: 5
 |     (_)
 |
 |              Five lives left!
 |
 |
_|___
'''

def body():
    return '''
 ________
 |/     |       Lives Remaining: 4
 |     (_)
 |      |
 |      |       It's fine, YOU CAN STILL SAVE HIM!
 |
 |
_|___
'''

def rightarm():
    return '''
 ________
 |/     |       Lives Remaining: 3!
 |     (_)
 |      |/
 |      |       It's fine, YOU CAN STILL SAVE HIM!
 |
 |
_|___
'''

def leftarm():
    return '''
 ________
 |/     |       Lives Remaining: 2!
 |     (_)
 |     \|/
 |      |       It's fine, YOU CAN STILL SAVE HIM!
 |
 |
_|___
'''

def rightleg():
    return '''
 ________
 |/     |       Lives Remaining: 1!
 |     (_)
 |     \|/
 |      |       You have ONE more life... or limb; make it count!
 |       \_
 |
_|___
'''

def leftleg():
    return '''
 ________
 |/     |       Lives Remaining: 0
 |     (_)
 |     \|/
 |      |       R.I.P.
 |    _/ \_
 |
_|___
'''

# stored words

words = [
    'cabin',
    'color',
    'fountain',
    'grandmother',
    'person',
    'highway',
    'baseball',
    'poetry',
    'shopping',
    'magazine',
    'hat',
    'gate',
    'computer',
    'glasses',
    'backpack',
    'mattress',
    'suitcase'
    ]

print('''
_________________________________________________________________________
.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.

   ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █  
  ▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
  ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
  ░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
  ░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
   ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
   ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
   ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ 
   ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      ''')

import random
while True:
    word = ['__']

    choice = input(
      '''                                                        ________
     Here are the options.                              |/     |
                                                        |     (_)
     1: Solo (Player VS Computer)                       |     \|/
     2: Multiplayer (Player VS Player)                  |      |
     3: How To Play                                     |    _/ \_
     4: End Game                                        |
                                                       _|___
     Type the number of your choice here: ''')     
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')

    if choice == "1":
        
        length = random.choice(words) # get the length of the randomly chosen word
        word = word * len(length) # multiply to make it equal amt of letters in word
        wrong = 0
        wrongGuesses = []

        print('''
     You have 10 lives left! Here is the secret word:
         ''')
        
        for blank in word:
            print(blank, end="  ")

        while choice == "1":
        
            guess = input("Guess a letter: ")
            
            if guess.lower() in length:
                for letter in range(len(length)):
                    if guess.lower() == length[letter]:
                        word[letter] = guess.lower()

                if "__" not in word:
                    print('''
     You've guessed the word! The word was "''' + length + '''".
     
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ''')
                    break
                        
                if wrong == 0:
                    print(none())
                elif wrong == 1:
                    print(stand())
                elif wrong == 2:
                    print(upper())
                elif wrong == 3:
                    print(string())
                elif wrong == 4:
                    print(head())
                elif wrong == 5:
                    print(body())
                elif wrong == 6:
                    print(rightarm())
                elif wrong == 7:
                    print(leftarm())
                elif wrong == 8:
                    print(rightleg())
                        
                for blank in word:
                    print(blank, end = "  ")
            
            elif guess not in length:
                
                if guess in wrongGuesses:
                    print("You already guessed this!")
                    continue
                    
                wrong += 1
                wrongGuesses.append(guess)
                if wrong == 1:
                    print(stand())
                    for blank in word:
                        print(blank, end = "  ")
                elif wrong == 2:
                    print(upper())
                    for blank in word:
                        print(blank, end = "  ")
                elif wrong == 3:
                    print(string())
                    for blank in word:
                        print(blank, end = "  ")
                elif wrong == 4:
                    print(head())
                    for blank in word:
                        print(blank, end = "  ")
                elif wrong == 5:
                    print(body())
                    for blank in word:
                        print(blank, end = "  ")
                elif wrong == 6:
                    print(rightarm())
                    for blank in word:
                        print(blank, end = "  ")
                elif wrong == 7:
                    print(leftarm())
                    for blank in word:
                        print(blank, end = "  ")
                elif wrong == 8:
                    print(rightleg())
                    for blank in word:
                        print(blank, end = "  ")
                elif wrong == 9:
                    print(leftleg())
                    print('''
     Oh no, you couldn't guess the word! The word was "''' + length + '''".
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ''')
                    break
      
    elif choice == "2":
        
        print('''
      multiplayer''')
        break
      
    elif choice == "3": # instructions
        
        print('''
                            INSTRUCTIONS
                             
     To WIN hangman, you must guess the chosen word before the stick 
                           figure is hung!
                           
     You must guess one letter at a time to slowly unlock the entire
     word. But be careful! Every time your guess is wrong, the stick
     figure's body parts will be added one at a time. Make sure to
     correctly guess the word before the entire stick figure is hung!''')
      
      
        goback = input('''
     Type 'Back' to go back: ''')
        print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ''')
        if goback == "Back" or goback == "back":
            continue
      
    elif choice == "4":
        break
