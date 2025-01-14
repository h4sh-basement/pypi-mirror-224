"""
    QuaO Project json_parser_utils.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
from datetime import datetime
from enum import Enum

import numpy as np


class JsonParserUtils:

    @staticmethod
    def parse(unparsed_input):
        if isinstance(unparsed_input, (complex, datetime)):
            return unparsed_input.__str__()

        if isinstance(unparsed_input, (str, int, float, bool, Enum)) or unparsed_input is None:
            return unparsed_input

        if isinstance(unparsed_input, (set, tuple)):
            return JsonParserUtils.parse(list(unparsed_input))

        if isinstance(unparsed_input, np.ndarray):
            return JsonParserUtils.parse(unparsed_input.tolist())

        if isinstance(unparsed_input, dict):
            data_holder = {}
            for key, value in unparsed_input.items():
                data_holder[key] = JsonParserUtils.parse(value)
            return data_holder

        if isinstance(unparsed_input, (list,)):
            data_list_holder = []
            for data in unparsed_input:
                data = JsonParserUtils.__resolve_type(data)
                if isinstance(data, dict):
                    data_list_holder.append(JsonParserUtils.parse(data))
                else:
                    data_list_holder.append(data)
            return data_list_holder

        dir_obj = dir(unparsed_input)

        if dir_obj.__contains__('to_dict'):
            return JsonParserUtils.parse(unparsed_input.to_dict())

        if dir_obj.__contains__('__dict__'):
            return JsonParserUtils.parse(unparsed_input.__dict__)

        return unparsed_input.__str__()

    @staticmethod
    def __resolve_type(element):
        if isinstance(element, (complex, datetime)):
            return element.__str__()
        if isinstance(element, (dict, str, int, float, bool, Enum)) or element is None:
            return element
        if isinstance(element, np.ndarray):
            return JsonParserUtils.__resolve_type(element.tolist())
        if isinstance(element, (list,)):
            data_holder = []
            for data in element:
                data_holder.append(JsonParserUtils.__resolve_type(data))
            return data_holder
        return element.__dict__
