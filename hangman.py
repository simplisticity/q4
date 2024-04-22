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

words = [
    'place',
    'cabin',
    'color',
    'fountain'
    ]

#test cases

print(none())
print(head())
print(leftarm())
print(leftleg())

print(words)
