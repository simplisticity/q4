# q4
Quarter 4 Project - Hangman

I'm creating a text-based hangman game in Python.

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

print(none())
print(head())
print(body())
print(rightarm())
print(leftarm())
print(rightleg())
print(leftleg())
