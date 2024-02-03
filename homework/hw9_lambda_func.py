"""
HOMEWORK9.

Task Description:
-----------------
HOMEWORK8 involves the following task.
Given list of ints/floats with lambda func as one of the element inside list.
Need to write function that will produce new list
by applying lambda to all integers and floats.

Input1: [lambda a: a + 2, 9, 3, 1, 0]
Output1: [11, 5, 3, 2]

Input2: [9, 2, 3, lambda a: a / 2.0, 1, 0]
Output2: [4.5, 1, 1.5, 0.5, 0.0]
"""

input1 = [lambda a: a + 2, 9, 3, 1, 0]
input2 = [9, 2, 3, lambda a: a / 2.0, 1, 0]


def apply_lambda_to_numbers(input_list):
    """
    Apply lambda functions to integers and floats in the input list.

    Parameters:
    - input_list (list): A list containing ints, floats, and lambda functions.

    Returns:
    - list: A new list with lambda functions applied to int and float elements.
    """
    input_list_copy = input_list.copy()
    for index, element in enumerate(input_list_copy):
        if not isinstance(element, (int, float)):
            lambda_func = input_list_copy.pop(index)
            return [lambda_func(value) for value in input_list_copy]


print(apply_lambda_to_numbers(input1))
print(apply_lambda_to_numbers(input2))
