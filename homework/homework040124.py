"""
HOMEWORK7.

Task Description:
-----------------
HOMEWORK7, involves the following task.
given values w, x, y, z = 100, 200, 40, 300
need to write if-elif-else statement that will search minimum value
and print smth aka "'y' is min value'" where 'y' is variable name (not value)

Task. Need to find the minimum value and print it.

"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
)
SEPARATOR_NUMBER = 56
w, x, y, z = 100, 200, 40, 300

logging.info('Solving the task using the standard if-elif-else method:')
if w <= x and w <= y and w <= z:
    logging.info(f'Variable "w" has the minimum value.')
elif x <= y and x <= z and x <= w:
    logging.info(f'Variable "x" has the minimum value.')
elif y <= z and y <= w and y <= x:
    logging.info(f'Variable "y" has the minimum value.')
else:
    logging.info(f'Variable "z" has the minimum value.')

logging.info(f'-' * SEPARATOR_NUMBER)

logging.info('Solving the task using the min function:')
min_value = min(w, x, y, z)
if w == min_value:
    logging.info(f'Variable "w" has the minimum value.')
elif x == min_value:
    logging.info(f'Variable "x" has the minimum value.')
elif y == min_value:
    logging.info(f'Variable "y" has the minimum value.')
else:
    logging.info(f'Variable "z" has the minimum value.')
