"""
HOMEWORK6.

Task Description:
-----------------
HOMEWORK6, involves the following tasks.
    Given a list of tuples. Each tuple represents:
    name, age, sum, last name, sex.

Task 1. Need to sort the list by age and sex fields.

Task 2. Need to get a new list as an old one without
        the first two elements and the last two elements.
        Print this new list.

Task 3. Need to calculate total numbers of "female" and "male"
        in new list and print it as small table.
"""
import logging
from operator import itemgetter

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
)

SEPARATOR_NUMBER = 19

# People list from teacher.
init_people_list = [
    ('Alice', 32, 100, 'Johnson', 'female'),
    ('Bob', 41, 200, 'Smith', 'male'),
    ('Charlie', 27, 150, 'Jones', 'male'),
    ('David', 52, 75, 'Williams', 'male'),
    ('Eve', 18, 300, 'Davis', 'female'),
    ('Frank', 33, 50, 'Taylor', 'male'),
    ('Grace', 42, 125, 'Clark', 'female'),
    ('Henry', 26, 225, 'Lewis', 'male'),
    ('Ivy', 38, 175, 'Moore', 'female'),
    ('Jack', 20, 140, 'Harris', 'male'),
    ('Kate', 37, 110, 'Miller', 'female'),
    ('Leo', 44, 90, 'Wilson', 'male'),
    ('Mae', 29, 180, 'Brown', 'female'),
    ('Nick', 51, 70, 'Davies', 'male'),
    ('Oliver', 18, 250, 'Collins', 'male'),
    ('Pete', 36, 160, 'Green', 'male'),
    ('Quinn', 20, 230, 'Bell', 'female'),
    ('Remy', 30, 120, 'Foster', 'male'),
    ('Sara', 28, 140, 'Baker', 'female'),
    ('Tom', 47, 80, 'Scott', 'male'),
    ('Ursula', 39, 135, 'Adams', 'female'),
    ('Vivian', 25, 190, 'Ross', 'female'),
    ('Wendy', 46, 90, 'Wright', 'female'),
    ('Xavier', 31, 105, 'Reed', 'male'),
    ('Yuliana', 22, 200, 'Lopez', 'female'),
    ('Zack', 48, 60, 'Mitchell', 'male'),
    ('Adam', 35, 75, 'Davis', 'male'),
    ('Bella', 27, 125, 'Smith', 'female'),
    ('Charlie', 44, 115, 'Johnson', 'male'),
    ('Daisy', 20, 215, 'Miller', 'female'),
    ('Ethan', 33, 100, 'Taylor', 'male'),
    ('Fiona', 40, 150, 'Jones', 'female'),
    ('George', 24, 180, 'Lewis', 'male'),
    ('Hannah', 22, 200, 'Williams', 'female'),
    ('Ivan', 29, 160, 'Brown', 'male'),
    ('Julie', 55, 90, 'Clark', 'female'),
    ('Kenny', 38, 140, 'Harris', 'male'),
    ('Luna', 55, 170, 'Smith', 'female'),
    ('Mike', 55, 55, 'Johnson', 'male'),
]

# Task 1. Sorting the list by age and sex fields.
sorted_people_list = sorted(init_people_list, key=itemgetter(1, 4))
logging.info('\n' + '\n'.join(map(str, sorted_people_list)))

# Task 2. A new list without the first two elements and the last two elements
people_list_cut = init_people_list[2:-2]
logging.info('\n' + '\n'.join(map(str, people_list_cut)))

# Task 3. Calculating total numbers of "female" and "male".
male_count = sum(1 for *_, gender in init_people_list if gender == 'male')
female_count = sum(1 for *_, gender in init_people_list if gender == 'female')
logging.info('-' * SEPARATOR_NUMBER)
logging.info(f'| {"Sex":^6} | {"Count":^6} |')
logging.info('-' * SEPARATOR_NUMBER)
logging.info(f'| {"Male":^6} | {male_count:^6} |')
logging.info(f'| {"Female":^5} | {female_count:^6} |')
logging.info('-' * SEPARATOR_NUMBER)
