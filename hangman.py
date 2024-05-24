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

def hangman():
        if wrong == 0:
            print(none())
            for blank in word:
                print(blank, end = "  ") # print the updated board
        elif wrong == 1:
            print(stand())
            for blank in word:
                print(blank, end = "  ") # print the updated board
        elif wrong == 2:
            print(upper())
            for blank in word:
                print(blank, end = "  ") # print the updated board
        elif wrong == 3:
            print(string())
            for blank in word:
                print(blank, end = "  ") # print the updated board
        elif wrong == 4:
            print(head())
            for blank in word:
                print(blank, end = "  ") # print the updated board
        elif wrong == 5:
            print(body())
            for blank in word:
                print(blank, end = "  ") # print the updated board
        elif wrong == 6:
            print(rightarm())
            for blank in word:
                print(blank, end = "  ") # print the updated board
        elif wrong == 7:
            print(leftarm())
            for blank in word:
                print(blank, end = "  ") # print the updated board
        elif wrong == 8:
            print(rightleg())
            for blank in word:
                print(blank, end = "  ") # print the updated board

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
        
        chosen_word = random.choice(words) # get the chosen_word of the randomly chosen word
        #print(chosen_word) # will delete, making sure letters = blank lines
        word = word * len(chosen_word) # multiply to make it equal amt of letters in word
        wrong = 0 # keep track of how many wrong guesses they have
        wrongGuesses = [] # keep track of the wrong guesses

        print('''
     You have 9 lives left! Here is the secret word:
         ''' + none())
        
        for blank in word:
            print(blank, end="  ")

        while choice == "1":
        
            guess = input("Guess a letter: ")
            
            if guess.lower() in chosen_word:
                for letter in range(len(chosen_word)):
                    if guess.lower() == chosen_word[letter]:
                        word[letter] = guess.lower()

                if "__" not in word:
                    print('''
     You've guessed the word! The word was "''' + chosen_word + '''".
     
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ''')
                    break

                hangman()
                                
            elif guess not in chosen_word:
                
                if guess in wrongGuesses:
                    print("You already guessed this!")
                    continue
                    
                wrong += 1
                wrongGuesses.append(guess)
                
                if wrong == 9:
                    print(leftleg())
                    print('''
     Oh no, you couldn't guess the word! The word was "''' + chosen_word + '''".
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ''')
                    break
                    
                hangman()
      
    elif choice == "2":

        wrong = 0
        wrongGuesses = []
        
        print('''
      Make sure you have a friend with you! Once you do, decide which
      one of you wants to be Player 1 and who'll be Player 2. 
      
      Player 1 will choose the word
      Player 2 has to guess the word
      
      Have you decided? Enter your names below!
      (You don't have to enter your real name, this is just to make it
      easier to keep track of whose turn it is.)''')
      
        player1 = input('''
      Player 1: ''')
        player2 = input('''
      Player 2: ''')
      
        chosen_word = input('''
      Okay ''' + player1 +  ''', turn the device towards you and make sure ''' + player2 + '''
      can't see what you're typing! Once you've done that, enter your 
      secret word here: ''')
        word = word * len(chosen_word)
        
        print('''
      |    |    |    |    |    |    |    |    |    |    |    |  
      `._  `.__.'  _.'    `.__.'  _.'    `.__.'  _.'    `.__.'  
    "-.  "-.    ,-"  ,-""-.    ,-"  ,-""-.    ,-"  ,-""-.    ,-"
      |    |    |    |    |    |    |    |    |    |    |    |  
      |    |    |    |    |    |    |    |    |    |    |    |  
    _.'    `.__.'  _.'  _.'  _.'    `.__.'  _.'    `.__.'  _.'  
      ,-""-.    ,-"  ,-"  ,-"  ,-""-.    ,-"  ,-""-.    ,-"  ,-"
      |    |    |    |    |    |    |    |    |    |    |    |  
      |    |    |    |    |    |    |    |    |    |    |    |  
    _.'  _.'    `.__.'    `.__.'  _.'    `.__.'  _.'  _.'  _.'  
      ,-"  ,-""-.    ,-""-.    ,-"  ,-""-.    ,-"  ,-"  ,-"  ,-"
      |    |    |    |    |    |    |    |    |    |    |    |  
      |    |    |    |    |    |    |    |    |    |    |    |  
    _.'    `.__.'  _.'    `.__.'  _.'  _.'    `.__.'  _.'    `._
      ,-""-.    ,-"  ,-""-.    ,-"  ,-"  ,-""-.    ,-"  ,-""-.  
      |    |    |    |    |    |    |    |    |    |    |    |  
      |    |    |    |    |    |    |    |    |    |    |    |  
    _.'  _.'  _.'    `.__.'  _.'    `.__.'  _.'    `.__.'  _.'  
      ,-"  ,-"  ,-""-.    ,-"  ,-""-.    ,-"  ,-""-.    ,-"  ,-"
      |    |    |    |    |    |    |    |    |    |    |    |  
      |    |    |    |    |    |    |    |    |    |    |    |  
      `.__.'  _.'  _.'  _.'    `.__.'  _.'  _.'    `.__.'  _.'
    "-.    ,-"  ,-"  ,-"  ,-""-.    ,-"  ,-"  ,-""-.    ,-"  ,-"
      |    |    |    |    |    |    |    |    |    |    |    |
              
              
      Goood choice! Now turn the device back towards ''' + player2 + '''.
      Make sure they DON'T scroll up and see your secret word!
      
      Now it's your turn, ''' + player2 + '''. Guess your partner's word! And
      don't cheat, that would be so lame.''')

        print('''
      You have 9 lives left! Here is the secret word:
         ''' + none())
        
        for blank in word:
            print(blank, end = "  ")

        while choice == "2":
            guess = input("Guess a letter: ")

            if guess.lower() in chosen_word:
                for letter in range(len(chosen_word)):
                    if guess.lower() == chosen_word[letter]:
                        word[letter] = guess.lower()
                        
                if "__" not in word:
                    print('''
     Looks like ''' + player2.upper() + ''' WINS! The word was "''' + chosen_word + '''".
     
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ''')
                    break
                
                hangman()
                    
            elif guess not in chosen_word:
                
                if guess in wrongGuesses:
                    print("You already guessed this!")
                    continue
                                
                wrong += 1
                wrongGuesses.append(guess)
                
                if wrong == 9:
                    print(leftleg())
                    print('''
     Looks like ''' + player2 + ''' couldn't guess the word so... ''' + player1.upper() + ''' WINS.
     The word was "''' + chosen_word + '''".
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ''')
                    break

                hangman()
      
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
