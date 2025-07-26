# this is zigzag sequence 
# Chapter 4: Functions
# author: diablo010

import time, sys

indent = 0         # Spaces to indent at start
indent_increasing = True

try: 
    while True:
        print(' ' * indent, end=' ')
        print('*****')
        time.sleep(0.5)     # Pause for 0.5s

        if indent_increasing:
            indent = indent + 1

            if indent == 5:
                indent_increasing = False
            
        else:
            indent = indent - 1

            if indent == 0:
                indent_increasing = True

except KeyboardInterrupt:
    sys.exit()
