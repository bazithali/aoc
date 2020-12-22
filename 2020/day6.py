"""
Created on 06-12-2020

@author: Basit
"""

answer_list = open('2020/data/6.txt').read().split('\n\n')

sol1 = sum([len(set(x.replace('\n', ''))) for x in answer_list])
sol2 = sum([len(set.intersection(*map(set, z))) for z in
            [[set(y) for y in x.split('\n')] for x in
             answer_list]])

print('Puzzle 1 : ', sol1)
print('Puzzle 2 : ', sol2)
# Puzzle 1 :  7110
# Puzzle 2 :  3628
