import logging
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

logging.debug('Start of program')

guess = '' 
logging.debug(f'Your guess is {guess}')
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input()
    logging.debug(f'Your guess is {guess}')

toss = random.randint(0, 1)     # 0 is tails, 1 is heads
logging.debug(f'toss is {toss}')

if toss == guess:
    print('You got it!')
    logging.debug(f'{toss} == {guess}')

else:
    print('Nope! Guess again!')
    logging.debug(f'{toss} != {guess}')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this.')

# Correct program
import logging
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

logging.debug('Start of program')

guess = ''

while guess not in ('heads', 'tails'):

    print('Guess the coin toss! Enter heads or tails: ')
    guess = input().lower()
    logging.debug(f'Your guess is {guess}')

# 0 is tails, 1 is heads
toss = 'heads' if random.randint(0, 1) == 1 else 'tails'
logging.debug(f'toss is {toss}')

if toss == guess:
    print('You got it!')
    logging.debug(f'{toss} == {guess}')

else:
    print('Nope! Guess again!')
    logging.debug(f'{toss} != {guess}')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this.')

