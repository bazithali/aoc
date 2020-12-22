"""
Created on 22-12-2020

@author: Basit
"""

boot_code = [[x[:3], x[4], int(x[4:])] for x in open('2020/data/8.txt').read().split('\n') if x]


def find_loop_point(instructions):
    run_list = {}
    accumulator = 0
    i = 0
    while i < len(instructions):
        if i in run_list.keys():
            return accumulator

        instruction = instructions[i]
        run_list[i] = True

        if instruction[0] == "acc":
            accumulator = accumulator + instruction[2]
            i = i + 1

        elif instruction[0] == "jmp":
            i = i + instruction[2]

        elif instruction[0] == "nop":
            i = i + 1

        else:
            raise ValueError("invalid instruction")
    return accumulator


def find_correct_accumulator(instructions):
    run_list = {}
    changed = {}
    accumulator = 0
    i = 0
    flag = False

    while i < len(instructions):
        if i in run_list.keys():
            accumulator = 0
            i = 0
            flag = False
            run_list = {}

        instruction = instructions[i]
        run_list[i] = True

        if instruction[0] == "acc":
            accumulator = accumulator + instruction[2]
            i = i + 1

        elif instruction[0] == "jmp":
            if i not in changed.keys() and flag is False:
                changed[i] = True
                i = i + 1
                flag = True
            else:
                i = i + instruction[2]

        elif instruction[0] == "nop":
            if i not in changed.keys() and flag is False:
                changed[i] = True
                i = i + instruction[2]
                flag = True
            else:
                i = i + 1

        else:
            raise ValueError("invalid instruction")
    return accumulator


print('Puzzle 1 : ', find_loop_point(boot_code))
print('Puzzle 2 : ', find_correct_accumulator(boot_code))
# Puzzle 1 :  1749
# Puzzle 2 :  515
