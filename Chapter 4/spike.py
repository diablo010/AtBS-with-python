import time, sys

try:
    while True:

        # Draw lines with increasing length
        for i in range(1, 5):
            print('-' * (i * i))
            time.sleep(0.5)

        # Draw lines with decreasing length:
        for i in range(5, 1, -1):
            print('-' * (i * i))
            time.sleep(0.5)
except KeyboardInterrupt:
    sys.exit()