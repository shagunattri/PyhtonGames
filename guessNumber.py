#!/usr/bin/python3

import random

print('Hello. What is your Name?')
name = input()

secretNo = random.randint(1,30)
print('Well, ' + name + ' I am thinking of a Number between 1 to 30.')
print('You Get 10 Chances!')
for guesstaken in range(10):
    print('Take a Guess.')
    guess = int(input())
    if guess < secretNo:
        print('Your guess is too low')
    elif guess > secretNo:
        print('Your guess is too high')
    else:
        break

if guess == secretNo:
    print('Great Job, You guessed my number in ' + str(guesstaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNo))

