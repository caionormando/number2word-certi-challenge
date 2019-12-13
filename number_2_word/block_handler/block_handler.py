"""The Block Handler class is responsible for deciding which will be the word associated to each digit. It checks each
one of them and associates a word to it. In the end, having the word specified for each digit, it calls
Block Word Handler to define if any change in the block sentence is necessary (e.g. applying "e")"""

from number_2_word.block_handler.block_word_handler import BlockWordHandler
from number_2_word.shared.number_utils import block_is_one_hundred, define_block_hundreds, tens_is_out_of_pattern, \
    define_block_tens_out_of_pattern, define_block_tens, units_is_out_of_pattern, define_block_units
from number_2_word.shared.word_numbers import out_of_pattern_dict


def define_digits_words(number_blocks):
    block_separated_words = []
    block_units_word = ''
    is_number_tens_out_of_pattern = False
    block_digits = list(number_blocks)

    # Hundreds name exception: 100 (cem)
    if block_is_one_hundred(number_blocks):
        block_separated_words = out_of_pattern_dict['100']
        return block_separated_words
    block_hundreds = block_digits[0]
    block_hundreds_word = define_block_hundreds(block_hundreds)
    block_separated_words.append(block_hundreds_word)

    # Tens name exception: from 10 to 19
    if tens_is_out_of_pattern(number_blocks):
        is_number_tens_out_of_pattern = True
        block_tens_word = define_block_tens_out_of_pattern(number_blocks)
    else:
        block_tens = block_digits[1]
        block_tens_word = define_block_tens(block_tens)
    block_separated_words.append(block_tens_word)

    # Units only exception is 0, but it also depends on tens and hundreds exceptions
    if (not is_number_tens_out_of_pattern) and (not units_is_out_of_pattern(number_blocks)):
        block_units = block_digits[2]
        block_units_word = define_block_units(block_units)
    block_separated_words.append(block_units_word)
    return block_separated_words


class BlockHandler:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_block_sentence(number_blocks):
        separated_words = define_digits_words(number_blocks)
        block_word_handler = BlockWordHandler(separated_words)
        if separated_words == out_of_pattern_dict["100"]:
            return out_of_pattern_dict["100"]
        block_sentence = block_word_handler.define_sentence()
        return block_sentence
