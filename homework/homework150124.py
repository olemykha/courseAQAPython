"""
HOMEWORK8.

Task Description:
-----------------
HOMEWORK8 involves the following task.
Given 0 < number(int) <= 11
Need to print multiplication table based on this number.
Output example for num 5:
1   2   3   4   5
2   4   6   8  10
3   6   9  12  15
4   8  12  16  20
5  10  15  20  25
"""


def processing_table(num):
    """
    Print a multiplication table for the given number.

    Parameters:
    - num (int): The number for which to generate the multiplication table.
    Should be between 1 and 11 (inclusive).
    """
    if 0 < num <= 11:
        print(f'Multiplication table based on number {num}:')
        for i in range(1, num + 1):
            for j in range(1, num + 1):
                print(f'{i * j:<4}', end='')
            print()
    else:
        print('Error: Please, enter a number between 1 and 11 inclusive.')


user_input = int(input('Please, enter a number between 1 and 11: '))
processing_table(user_input)
