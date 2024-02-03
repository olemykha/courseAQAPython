"""
HOMEWORK5.

Task Description:
-----------------
HOMEWORK5, involves the following tasks:
Given list of tuples (people list > name, surname, age, profession, location)

Task 1. Need to add a new record
        with similar random data at the beginning of the given list.

Task 2. Need to swap elements with indexes 1 and 5
        (1<->5) in the modified list and print result.

Task 3. Need to check the condition that all people
        in the modified list with records indexes 6, 10, 13
        have age >=30 and print result
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
)

# Tuple from teacher
initial_people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix'),
]

# Task 1. Adding a new record at the beginning of the given list
modif_people_rec = initial_people_records.copy()  # creating a copy
modif_people_rec.insert(0, ('Alex', 'Alexovich', 30, 'QA', 'Kharkiv'))
logging.info('\n' + '\n'.join(map(str, modif_people_rec)))

# Task 2. Swapping elements with indexes 0 to 4
swap_people_records = modif_people_rec.copy()
length_of_tuple = len(swap_people_records)
if len(swap_people_records) >= length_of_tuple:
    swap_people_records[0], swap_people_records[4] = (
        swap_people_records[4],
        swap_people_records[0],
    )
    logging.info('\n' + '\n'.join(map(str, swap_people_records)))
else:
    logging.info('Tuple does not have enough elements.')

# Task 3. Checking conditions that all people
# with records indexes 6, 10, 13 have age >=30
indexes_to_check = [6, 10, 13]
conditions_met = all(
    modif_people_rec[i][-1].isdigit() and int(modif_people_rec[i][-1]) >= 30
    for i in indexes_to_check
)
if conditions_met:
    logging.info(
        'All people with records at indexes 6, 10, and 13 have age >= 30',
    )
else:
    logging.info(
        'Not all people with records at indexes 6, 10, and 13 have age >= 30',
    )
