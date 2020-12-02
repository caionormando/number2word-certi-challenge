"""The Composer Handler verifies both sentences: [hundreds, tens, units] and [thousand hundreds, thousand tens and
thousand units]. It sets the manipulation necessary in both of them (such as adding "mil" and spaces) in order to
generate the final word for the number"""
from number_2_word.shared.word_numbers import units_dict, thousands_dict


class ComposerHandler:
    def __init__(self, sentences) -> None:
        super().__init__()
        self.sentences = sentences

    def compose_number(self):
        simple_values_word = self.sentences[0]
        thousand_values_word = self.sentences[1]

        if thousand_values_word != '':
            if thousand_values_word == units_dict["1"]:
                thousand_values_word = ""
            thousand_values_word = thousand_values_word + thousands_dict['milhar']
        if thousand_values_word != '' and simple_values_word != '':
            thousand_values_word = thousand_values_word + 'e '

        full_number_word = thousand_values_word + simple_values_word
        return full_number_word
