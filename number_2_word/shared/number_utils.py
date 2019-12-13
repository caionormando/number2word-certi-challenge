""" A set of useful methods for number and string manipulation """
import re
from number_2_word.shared.definitions import range_dict
from number_2_word.shared.word_numbers import hundreds_dict, tens_dict, out_of_pattern_dict, units_dict


def regex_string(string):
    return string.replace('.', '')


def is_number_negative(number) -> bool:
    if number < 0:
        return True
    return False


def number_inside_range(number) -> bool:
    if range_dict["minimumRange"] <= number <= range_dict["maximumRange"]:
        return True
    return False


def arrange_number(string_number) -> str:
    if len(string_number) % 3 == 0:
        return string_number
    else:
        return '0' * (3 - len(string_number) % 3) + string_number


def concat_numbers_in_blocks(number_string):
    number_string = arrange_number(number_string)
    number_string = [number_string[i:i + 3] for i in range(len(number_string), -1, -3)]
    return number_string


def strip_negative_symbol(number_string):
    number_string = number_string.strip('-')
    return number_string


def check_if_number_is_zero(number_blocks):
    pass


def block_is_one_hundred(number_blocks):
    if number_blocks == '100':
        return True
    return False


def tens_is_out_of_pattern(number_blocks):
    if number_blocks[1] == '1':
        return True
    return False


def tens_without_units(number_blocks):
    if (not number_blocks[1] == '0') and number_blocks[2] == '0':
        return True
    return False


def hundreds_without_tens_and_units(number_blocks):
    if (not number_blocks[0] == '0') and (number_blocks[1] == '0') and (number_blocks[2] == '0'):
        return True
    return False


# This method checks for tens without unit and hundreds without tens and units
def units_is_out_of_pattern(number_blocks):
    if (tens_without_units(number_blocks)) or (hundreds_without_tens_and_units(number_blocks)):
        return True
    return False


def define_block_hundreds(block_hundreds):
    if block_hundreds is not '':
        return hundreds_dict[block_hundreds]


def define_block_tens(block_tens):
    if block_tens is not '':
        return tens_dict[block_tens]


def define_block_tens_out_of_pattern(number_blocks):
    return out_of_pattern_dict[number_blocks[1] + number_blocks[2]]


def define_block_units(block_units):
    if block_units is not '':
        return units_dict[block_units]
