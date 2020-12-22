"""
Created on 05-12-2020

@author: Basit
"""


# Initial function
def selector_v1(text, upper):
    min_pos = 0
    max_pos = 2 ** len(text) - 1
    i = 0
    while i < len(text)-1:
        if text[i] == upper:
            min_pos = (min_pos + max_pos + 1) // 2
        else:
            max_pos = (min_pos + max_pos) // 2
        i = i + 1
    if text[i] == upper:
        return max_pos
    else:
        return min_pos


# Re worked function
def selector_v2(text):
    seat = text.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return int(seat[:7],2) * 8 + int(seat[-3:],2)


b_passes = open('2020/data/5.txt').read().splitlines()
seat_ids = list(map(lambda x: selector_v1(x[:7], 'B') * 8 + selector_v1(x[-3:], 'R'), b_passes))
sol1 = max(seat_ids)
sol2 = sum(range(min(seat_ids), sol1+1)) - sum(seat_ids)
print('Puzzle 1 : ', sol1)
print('Puzzle 2 : ', sol2)

seat_ids = list(map(selector_v2, b_passes))
sol1 = max(seat_ids)
sol2 = sum(range(min(seat_ids), sol1+1)) - sum(seat_ids)
print('Puzzle 1 : ', sol1)
print('Puzzle 2 : ', sol2)


# Puzzle 1 :  625
# Puzzle 2 :  892
