import time

def collatz(number):

    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    
    print(result)
    return result

print('Welcome to Collatz!')
time.sleep(0.5)

print('Enter an integer')
integer = int(input('>'))

while integer != 1:
    integer = collatz(integer)

print('Collatz complete!')
    