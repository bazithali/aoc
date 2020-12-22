"""
Created on 19-12-2020

@author: Basit
"""

import re

input_data = [re.split(', | contain ', x) for x in open('2020/data/7.txt').read().replace('.', '').split('\n') if x]
parsed_rules = [[''.join(re.split(' ', x[0])[:2]), [''.join(re.split(' ', y)[1:3]) for y in x[1:]]] for x in input_data]
parsed_rules_without_count = dict(parsed_rules)

parsed_rules = [[''.join(re.split(' ', x[0])[:2]), [[int(y[0]), ''.join(re.split(' ', y)[1:3])] if y != 'no other bags'
                                                    else None
                                                    for y in x[1:]]]
                for x in input_data]
parsed_rules_with_count = dict(parsed_rules)


def check_for_shiny_gold(bag_name, bag_dict):
    try:
        if "shinygold" in bag_dict[bag_name]:
            return 1
        else:
            for sub_bag in bag_dict[bag_name]:
                if check_for_shiny_gold(sub_bag, bag_dict):
                    return check_for_shiny_gold(sub_bag, bag_dict)
            return 0
    except KeyError:
        return 0


def count_sub_bags(main_bag, bag_dict):
    try:
        bag_count = 1
        for sub_bag in bag_dict[main_bag]:
            bag_count = bag_count + (sub_bag[0] * count_sub_bags(sub_bag[1], bag_dict))
        return bag_count
    except TypeError:
        return 1


print('Puzzle 1 : ', sum([check_for_shiny_gold(bag_name, parsed_rules_without_count) for
                          bag_name in parsed_rules_without_count.keys()]))
print('Puzzle 2 : ', count_sub_bags('shinygold', parsed_rules_with_count) - 1)
# Puzzle 1 :  148
# Puzzle 2 :  24867
