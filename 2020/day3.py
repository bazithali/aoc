"""
Created on 03-12-2020

@author: Basit
"""


def check_tree_count(right, down, grid):
    width = len(grid[0]) - 1
    no_of_trees = 0
    l_pos = 0
    i = down
    while i < len(grid):
        l_pos = l_pos + right
        if l_pos > width:
            l_pos = (l_pos - 1) % width
        no_of_trees = no_of_trees + (grid[i][l_pos] == "#")
        i = i + down
    return no_of_trees


full_grid = open('2020/data/3.txt').read().splitlines()

print('Puzzle 1 : ', check_tree_count(3, 1, full_grid))
print('Puzzle 2 : ',
      check_tree_count(1, 1, full_grid) *
      check_tree_count(3, 1, full_grid) *
      check_tree_count(5, 1, full_grid) *
      check_tree_count(7, 1, full_grid) *
      check_tree_count(1, 2, full_grid))

# Puzzle 1 :  274
# Puzzle 2 :  6050183040
