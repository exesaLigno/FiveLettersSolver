#!/usr/bin/python

from FiveLetters import *
import sys

word_length = 5 if len(sys.argv) < 2 else int(sys.argv[1])

game = FiveLetters(word_length=word_length)
commands_list = '          Commands: \x1b[1mnext\x1b[0m, \x1b[1mexit\x1b[0m, \x1b[1mreset\x1b[0m, \x1b[1mmeaning\x1b[0m'
greeting_string = 'What result? > ' + '_' * game.word_length + \
                  commands_list + '\b' * (game.word_length + 46) + '\x1b[1;33m'

print(f'Loaded {game.words_count} words of {game.word_length} words')

print('''
Instructions:
    1. If game didn't know suggested word, in result print 'next'
    2. If game know word, use syntax above to describe result:
        1) If letter not in the word, type '-' under it
        2) If letter in the word, but not in place, type '?'
        3) If letter on the right place, type '+'
    3. Enjoy!
    4. If you win, lose or want to exit, type 'exit'
    5. If you want to reset programm, type 'reset'
    6. If you want to learn about word meaning, type 'meaning'
''')

new_word_needed = True
prediction_generated = False

while True:
    if new_word_needed:
        if game.words_count <= 10 and prediction_generated == False:
            print(f'Only {game.words_count} words left, here they are:\n    ', end='')
            for word in game.words:
                print(f'\x1b[1;32m{word}\x1b[0m    ', end='')
            print('\n')
            prediction_generated = True

        suggested_word = game.nextWord()
        if suggested_word == None:
            print('Sorry, I don\'t know any other words :(')
            print('\x1b[1;31mResetting.....\n\x1b[0m')
            game.reset()
            continue
    new_word_needed = True

    print(f'Try this word: \x1b[1;32m{suggested_word}\x1b[0m          \x1b[3m({game.words_count} words left)\x1b[0m')
    
    pattern = input(greeting_string)
    print('\x1b[0m', end='')

    if pattern == '+' * game.word_length:
        print('I am very happy to help you!')
        print('\x1b[1;31mResetting.....\n\x1b[0m')
        game.reset()
        continue
    elif set(pattern) <= set('+-?') and len(pattern) == game.word_length:
        game.setInfo(suggested_word, pattern)
        continue

    elif pattern == 'meaning':
        print('\x1b[1mMeaning:\x1b[0m ' + game.getDefinition(suggested_word) + '\n')
        new_word_needed = False
        continue

    elif pattern == 'next':
        game.removeWord(suggested_word)
        continue
    elif pattern == 'reset':
        print('\x1b[1;31mResetting.....\n\x1b[0m')
        game.reset()
        continue
    elif pattern == 'exit':
        print('Thanks for using this program!')
        break
        
    else:
        print('Incorrect pattern or command, try again!\n')
        new_word_needed = False
        continue
