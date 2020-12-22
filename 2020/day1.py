"""
Created on 01-12-2020

@author: Basit
"""

expense_entries = [int(x) for x in open('2020/data/1.txt').read().strip().split('\n')]


def func1(entries):
    for i in range(0, len(entries)):
        for j in range(0, len(entries)):
            if entries[i] + entries[j] == 2020:
                return entries[i] * entries[j]


def func2(entries):
    for i in range(0, len(entries)):
        for j in range(0, len(entries)):
            for k in range(0, len(entries)):
                if entries[i] + entries[j] + entries[k] == 2020:
                    return entries[i] * entries[j] * entries[k]


print('Puzzle 1 : ', func1(expense_entries))
print('Puzzle 2 : ', func2(expense_entries))
# Puzzle 1 :  41979
# Puzzle 2 :  193416912
