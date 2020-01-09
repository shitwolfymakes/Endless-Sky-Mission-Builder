""" FileItemParser.py
# Copyright (c) 2020 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""
import re
from abc import ABC, abstractmethod


class FileItemParser(ABC):
    """Contains methods common to the various file parsers"""
    @abstractmethod
    def run(self):
        pass
    #end run


    @staticmethod
    def strip_ending_whitespace(lines):
        while lines[-1] == "" or lines[-1] == "\n":
            del lines[-1]
    # end strip_ending_whitespace


    @staticmethod
    def tokenize(line):
        """Break the line into a list of tokens, saving anything inside quotes as a single token"""
        pattern = re.compile(r'((?:".*?")|(?:`.*?`)|[^\"\s]+)')
        tokens = re.findall(pattern, line)
        for i, token in enumerate(tokens):
            if token.startswith("`"):
                tokens[i] = token[1:-1]
            elif token.startswith("\""):
                tokens[i] = token[1:-1]
        return tokens
    # end tokenize


    @staticmethod
    def get_indent_level(line):
        tab_count = len(line) - len(line.lstrip('\t'))
        return tab_count
    # end get_indent_level


    @staticmethod
    def store_component_data(component, tokens):
        """
        Store the tokens in the given component

        :param component: The component the data will be stored in
        :param tokens: The tokens to store
        """
        for i, token in enumerate(tokens):
            if token is not None:
                component[i] = token
            else:
                break
            # end if/else
        # end for
    # end store_component_data
#end class FileItemParser
