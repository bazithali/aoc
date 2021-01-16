"""
Created on 23-12-2020

@author: Basit
"""

xmas_code = list(map(int, open('2020/data/9.txt').readlines()))


def find_first_error(xmas_codes):
    start = 0
    end = 25
    while end < len(xmas_codes):
        current_window = xmas_codes[start:end]

        i = 0
        while i < 25:
            flag = 0
            if (xmas_codes[end] - current_window[i]) not in current_window[i + 1:]:
                pass
            else:
                flag = 1
                break
            i = i + 1

        if flag == 0:
            return xmas_codes[end]

        start = start + 1
        end = end + 1


def find_contiguous_numbers(xmas_codes, error_num):
    pair_count = 2
    while pair_count < len(xmas_codes):
        start = 0
        end = start + pair_count
        while end < len(xmas_codes):
            pair_sum = sum(xmas_codes[start:end])
            if error_num == pair_sum:
                return min(xmas_codes[start:end]) + max(xmas_codes[start:end])
            start = start + 1
            end = end + 1
        pair_count = pair_count + 1
    return "not found"


solution_1 = find_first_error(xmas_code)
print('Puzzle 1 : ', solution_1)
solution_2 = find_contiguous_numbers(xmas_code, solution_1)
print('Puzzle 2 : ', solution_2)

# Puzzle 1 :  1124361034
# Puzzle 2 :  129444555
