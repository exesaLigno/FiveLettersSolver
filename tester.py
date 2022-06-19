from FiveLetters import *
from random import choice
from pprint import pprint
from matplotlib import pyplot as plt

results = {}

for _ in range(100000):
    word = choice(list(FiveLetters.all_words.keys()))
    #print(f'Guessed word {word}')

    solver = FiveLetters(word_length=len(word))
    suggestion = None
    steps_count = 0

    while suggestion != word:
        steps_count += 1
        suggestion = solver.nextWord()

        pattern = ''

        for s_letter, letter in zip(suggestion, word):
            if s_letter == letter: pattern += '+'
            elif s_letter in word: pattern += '?'
            else: pattern += '-'

        #print(f'Suggested word {suggestion}, result is {pattern}')

        solver.setInfo(suggestion, pattern)

    #print(f'Solved the task in {steps_count} steps')
    if f'{len(word)} letters' not in results:
        tries = 1
        average_steps = steps_count
        minimum_steps = steps_count
        maximum_steps = steps_count
        wins = 1 if steps_count <= 6 else 0
        fails = 1 if steps_count > 6 else 0
    else:
        tries = results[f'{len(word)} letters']['tries'] + 1
        average_steps = (results[f'{len(word)} letters']['average_steps'] * (tries - 1) + steps_count) / tries
        minimum_steps = results[f'{len(word)} letters']['minimum_steps']
        if steps_count < minimum_steps: minimum_steps = steps_count
        maximum_steps = results[f'{len(word)} letters']['maximum_steps']
        if steps_count > maximum_steps: maximum_steps = steps_count
        wins = results[f'{len(word)} letters']['wins'] + (1 if steps_count <= 6 else 0)
        fails = results[f'{len(word)} letters']['fails'] + (1 if steps_count > 6 else 0)

    results[f'{len(word)} letters'] = {
        'tries': tries,
        'average_steps': average_steps,
        'minimum_steps': minimum_steps,
        'maximum_steps': maximum_steps,
        'wins': wins,
        'fails': fails
    }

pprint(results)

letters_count_band = sorted(map(lambda x: int(x[:-8]), results.keys()))
win_rates_band = []
average_steps_band = []
max_steps_band = []
min_steps_band = []

for letters_count in letters_count_band:
    wins = results[f'{letters_count} letters']['wins']
    fails = results[f'{letters_count} letters']['fails']
    win_rates_band.append(wins / (wins + fails) * 100)

    average_steps_band.append(results[f'{letters_count} letters']['average_steps'])
    
    max_steps_band.append(results[f'{letters_count} letters']['maximum_steps'])
    min_steps_band.append(results[f'{letters_count} letters']['minimum_steps'])




plt.figure(figsize=[10,7])
plt.plot(letters_count_band, win_rates_band, color='blue', label='Win rate')
plt.plot(letters_count_band, [100 for _ in range(len(letters_count_band))], ':', color='green', label='Ideal win rate')
plt.ylim(-10, 110)
plt.xlabel('Count of letters')
plt.ylabel('Win rate, %')
plt.legend()
plt.grid()
plt.savefig('wins_rate.png')

plt.figure(figsize=[10,7])
plt.plot(letters_count_band, max_steps_band, color='red', label='Maximum steps')
plt.plot(letters_count_band, min_steps_band, color='green', label='Minimum steps')
plt.plot(letters_count_band, average_steps_band, color='orange', label='Average steps')
plt.plot(letters_count_band, [6 for _ in range(len(letters_count_band))], ':', color='red', label='Maximum avaliable steps')
plt.xlabel('Count of letters')
plt.ylabel('Steps')
plt.legend()
plt.grid()
plt.savefig('steps.png')
