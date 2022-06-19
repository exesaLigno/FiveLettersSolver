# FiveLetters Game Solver

## Initial setup

In your terminal type 
```bash
git clone git@github.com:exesaLigno/FiveLettersSolver.git
```
or download this repo as zip-file.

## Usage 

In terminal type 
```bash
python3 solver.py {count_of_letters}
```
If you don't specify count of letters, it will be setted up by default _(5 letters)_

At first the program will offer some word to write in the game. When you write this word, type result in the program with symbols `-` if letter __not in the word__, `+` if letter __in the word and placed correctly__ or `?` if letter __in the word, but displaced__.

Here is example of usage
```
Try this word: вепрь
What result? > ?--++

Try this word: хворь
What result? > _____
```

If game doesn't accept suggested word, you can skip it with typing command `next`. If you want to reset solver to initial state, type `reset`. Also programm can give explanations of words with command `meaning`. If you want to exit, just type command `exit`.

If program gives correct answer, it will be resetted to initial state.

## Tests

Program doesn't guarantee 100% win chance. You can check out plots of __win rate__ and __steps count__ for different word lengths. For five letters win rate is __about 95.4%__ and average steps count is __4.48 steps for win__
