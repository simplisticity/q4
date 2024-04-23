# design the hangman/user interface

def none():
    return '''
 ________
 |/     |
 |
 |
 |
 |
 |
_|___
'''

def head():
    return '''
 ________
 |/     |
 |     (_)
 |
 |
 |
 |
_|___
'''

def body():
    return '''
 ________
 |/     |
 |     (_)
 |      |
 |      |
 |
 |
_|___
'''

def rightarm():
    return '''
 ________
 |/     |
 |     (_)
 |      |/
 |      |
 |
 |
_|___
'''

def leftarm():
    return '''
 ________
 |/     |
 |     (_)
 |     \|/
 |      |
 |
 |
_|___
'''

def rightleg():
    return '''
 ________
 |/     |
 |     (_)
 |     \|/
 |      |
 |       \_
 |
_|___
'''

def leftleg():
    return '''
 ________
 |/     |
 |     (_)
 |     \|/
 |      |
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

choice = input(
      '''
      Welcome to Hangman! Here are the options.
      
      1: Solo (Player VS Computer)
      2: Multiplayer (Player VS Player)
      3: How To Play
      4: End Game
      
      Type the number of your choice here: 
      '''
      )

#test cases

print(none())
print(head())
print(leftarm())
print(leftleg())

print(words)
