"""
HOMEWORK10_Regexp.

Task Description:
-----------------
HOMEWORK10 involves the following task.
Open input.txt file and find all small english letters that match conditions:
Target small letter round exactly with three capital english letters
on the left and on the right.
Examples:

sdTRYaUVKn -> matches "a" because 'TRY' on the left (3 capital letters)
and 'UVK' on the right (3 capital letters)

NTRSjARTb -> no match
(not exactly 3 capital letters on the left ('NTRS' = 4 letters))

zDFGbOPNq -> matches "b"

Print Output as : "Result: "string of found letters">
"""

import re

with open("input.txt", "r") as input_file:
    content = input_file.read()

characters = re.findall(r'(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])', content)
result = f'Result: "{''.join(characters)}"'
print(result)
