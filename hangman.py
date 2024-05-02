# design the hangman/user interface

def none():
    return '''
 ________
 |/     |       Body Parts Remaining: 6
 |
 |
 |              NICE!
 |
 |
_|___
'''

def head():
    return '''
 ________
 |/     |       Body Parts Remaining: 5
 |     (_)
 |
 |              Only one wrong guess, it's okay!
 |
 |
_|___
'''

def body():
    return '''
 ________
 |/     |       Body Parts Remaining: 4
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
 |/     |       Body Parts Remaining: 3!
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
 |/     |       Body Parts Remaining: 2!
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
 |/     |       Body Parts Remaining: 1!!
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
 |/     |       Body Parts Remaining: 0
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
    'gate'
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
    word = ['__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__']

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
        print(length) # will delete, making sure letters = blank lines
        word = word[0:len(length)] # reduce amt of blank lines to equal amt of letters

        print('''
     Here is the secret word:
         ''')
        
        for blank in word:
            print(blank, end="  ")
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
