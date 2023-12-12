"""HOMEWORK4."""
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
)

# Text from teacher
poem_text = """
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

poem_text.lower()
vowels = ['a', 'e', 'i', 'o', 'u']  # list of vowels

separator_number = 18
logging.info('-' * separator_number)
logging.info(f"| {'Vowel':^2} | {'Count':^6} |")
logging.info('-' * separator_number)

# Counting the number of vowels in a text
for vowel in vowels:
    count = poem_text.count(vowel)
    logging.info(f'| {vowel:^6}|  {count:^5} |')

logging.info('-' * separator_number)
logging.info('The table output is complete.')

# The second task is to change all the vowels to those provided by the teacher.
modified_poem_text = (
    poem_text
    .replace('A', 'À').replace('a', 'à')
    .replace('E', 'É').replace('e', 'é')
    .replace('I', 'Í').replace('i', 'í')
    .replace('O', 'Ó').replace('o', 'ó')
    .replace('U', 'Ú').replace('u', 'ú')
)
logging.info(f'Modified text of the poem: {modified_poem_text}')
