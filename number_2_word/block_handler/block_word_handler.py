"""Block word handler is responsible for manipulating the sentence of each block by adding the connectors to the words
of each digit"""


class BlockWordHandler:
    def __init__(self, separated_words) -> None:
        super().__init__()
        self.separated_words = separated_words

    def define_sentence(self):
        units = self.separated_words[2]
        tens = self.separated_words[1]
        hundreds = self.separated_words[0]
        # "E" after hundreds
        if ((hundreds != '') and (tens != '')) or ((hundreds != '') and (tens == '') and units != ''):
            hundreds = hundreds + " e "
        # "E" after tens
        if tens != '' and units != '':
            tens = tens + " e "
        word = hundreds + tens + units
        return word
