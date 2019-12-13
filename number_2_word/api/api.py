"""The APIServer class is responsible for generating the endpoints regarding the information retrieved. It calls the
Factory in order to start the number-to-word conversion process. In this part, some problems are treated, such as
dots after thousands (e.g. "3.000") and number which are out of the defined range (-99999, 99999)"""

import flask
import flask_cors
from flask import jsonify
from flask_cors import CORS

from number_2_word.number_separators.number_separator_factory import NumberSeparatorFactory
from number_2_word.shared.definitions import out_of_range_message
from number_2_word.shared.number_utils import number_inside_range, regex_string
from number_2_word.shared.word_numbers import out_of_pattern_dict


class APIServer:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def start_server():
        app = flask.Flask(__name__)
        cors = CORS(app)
        app.config["DEBUG"] = False
        app.config['JSON_AS_ASCII'] = False

        @app.route('/', methods=['GET'])
        def home():
            return "<h1>Code challenge</h1><p>by Caio Normando</p>"

        @app.route('/<number>', methods=['GET'])
        def convert_number(number):
            number = regex_string(str(number))
            if int(number) == 0:
                number_word = out_of_pattern_dict["0"]
            else:
                if number_inside_range(int(number)):
                    separator = NumberSeparatorFactory(int(number))
                    number_word = separator.create_separator().create_collection(int(number)).iterator.full_number
                else:
                    number_word = out_of_range_message

            return jsonify(extenso=number_word)

        app.run(host='0.0.0.0')
