"""
HOMEWORK4.

Task Description:
-----------------
HOMEWORK4, involves the following tasks:

Task 1. Need to count each vowel occurrence in the text
(total sum of lower and capital cases).
List of vowels: A, E, I, O, and U.
The text from the teacher is provided in the poem_text variable.

Task 2. Need to modify the text (which is specified in the poem_text variable),
where each vowel is replaced with:
A->À,a->à; E->É,e->é; I->Í,i->í; O->Ó,o->ó; U->Ú,u->ú.
and print it.

"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
)

# Text from teacher
initial_poem_text = """
I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance.
"""

poem_text = initial_poem_text.lower()
vowels = ['a', 'e', 'i', 'o', 'u']  # list of vowels

separator_number = 18
logging.info('-' * separator_number)
logging.info(f"| {'Vowel':^2} | {'Count':^6} |")
logging.info('-' * separator_number)

# Task 1. Counting the number of vowels in a text
for vowel in vowels:
    count = poem_text.count(vowel)
    logging.info(f'| {vowel:^6}|  {count:^5} |')

logging.info('-' * separator_number)
logging.info('The table output is complete.')

# Task 2. Changing all the vowels to those provided by the teacher.
new_symbols_for_replacement = str.maketrans({
    'A': 'À', 'a': 'à',
    'E': 'É', 'e': 'é',
    'I': 'Í', 'i': 'í',
    'O': 'Ó', 'o': 'ó',
    'U': 'Ú', 'u': 'ú',
})
modified_poem_text = initial_poem_text.translate(new_symbols_for_replacement)
logging.info(f'Modified text of the poem: {modified_poem_text}')
