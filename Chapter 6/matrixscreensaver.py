import random, sys, time

width = 70      # No of columns

try:
    columns = [0] * width
    # For each column, when the counter is 0, no stream is shown
    # Otherwise, it acts as a counter for how many times a 1 or 0
    # should be displayed in that column

    while True:

        for i in range(width):
            if random.random() < 0.02:
                # The stream length is between 4 and 14 characters long
                columns[i] = random.randint(4, 14)

            # Print a character in this column
            if columns[i] == 0:
                print(' ', end='')
            else:
                # Print a 0 or 1:
                print(random.choice([0, 1]), end='')
                columns[i] -= 1     # Decrement the counter for this column

        print()
        time.sleep(0.1)

except KeyboardInterrupt:
    sys.exit()