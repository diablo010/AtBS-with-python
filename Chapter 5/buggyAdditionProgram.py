import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

logging.debug('Start of program')

print('Enter 1st number to add: ')
first = input('>')
logging.debug(f'1st no is {type(first)}')

print('Enter 2nd number: ')
second = input('>')
logging.debug(f'2nd no is {type(second)}')

print('Enter 3rd number: ')
third = input('>')
logging.debug(f'3rd no is {type(third)}')

print(f'Sum is {first + second + third}')

logging.debug('End of program')

# Correct program
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

logging.debug('Start of program')

print('Enter 1st number to add: ')
first = int(input('>'))
logging.debug(f'1st no is {type(first)}')

print('Enter 2nd number: ')
second = int(input('>'))
logging.debug(f'2nd no is {type(second)}')

print('Enter 3rd number: ')
third = int(input('>'))
logging.debug(f'3rd no is {type(third)}')

print(f'Sum is {first + second + third}')

logging.debug('End of program')
