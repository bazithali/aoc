"""
Created on 02-12-2020

@author: Basit
"""


def check_first_policy(password_data):
    min_c, max_c = map(int, password_data[0].split('-'))
    alphabet = password_data[1][0]
    alph_count = password_data[2].count(alphabet)
    return min_c <= alph_count <= max_c


def check_current_policy(password_data):
    pos1, pos2 = map(int, password_data[0].split('-'))
    alphabet = password_data[1][0]
    return bool(password_data[2][pos1-1] == alphabet) ^ bool(password_data[2][pos2-1] == alphabet)


entries = [x.split(' ') for x in open('2020/data/2.txt').readlines()]
print("Puzzle 1 : valid passwords : {} ".format(sum([check_first_policy(entry) for entry in entries])))
print("Puzzle 2 : valid passwords : {} ".format(sum([check_current_policy(entry) for entry in entries])))
# Puzzle 1 : valid passwords : 620
# Puzzle 2 : valid passwords : 727
