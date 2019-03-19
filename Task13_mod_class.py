import re
import itertools
import string
from typing import List
from collections import defaultdict
from collections import Counter

class Sequence:
    """sequence class.
    It has the attribute string.

    Attributes:
    string: a string of characters representing a sequence.
    """

    def __init__(self,type, string):
        """Task 11: automotically changed all chars in string to lowercase."""
        self.string = string.lower()
        self.type = type.lower()

    def bases(self):
        """ Task 2: method to return number of DNA bases"""
        print(len(self.string))

    def is_valid(self, type):
        for i in range(len(self.string)):
            if self.type == "dna":
                if all(c in "acgt" for c in self.string):
                    match = True
                    return match
                else:
                    match = False
                    return False
            if self.type == "rna":
                if all(c in "acgu" for c in self.string):
                    match = True
                    return match
                else:
                    match = False
                    return False


    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Sequence):
            return self.string == other.string.lower()

    def complement(self, type):
            if self.type == "dna":
                basecomplement = {'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
                letters = list(self.string)
                letters = [basecomplement[base] for base in letters]
                return ''.join(letters)
            if self.type == "rna":
                basecomplement = {'a': 'u', 'c': 'g', 'g': 'c', 'u': 'a'}
                letters = list(self.string)
                letters = [basecomplement[base] for base in letters]
                return ''.join(letters)
            else:
                return False

    def non_match(self, other):
        List1 = list(self.string)
        List2 = list(other.string.lower())

        if len(List1) == len(List2):
            if sorted(List1) == sorted(List2):
                print("Strings are identical")
            else:
                index = [i for i in range(len(List1) - 1) if List1[i] != List2[i]]
                print(index)
            return -1
        # else:
        #   raise Exception('cannot compare sequences of different lengths')

    def swap_method(dict1, dict2):
        my_list1 = []
        my_list2 = []
        key_list = []
        swaps = []

        for key in dict1:
            if dict1[key] != dict2[key]:
                my_list1.append(dict1[key])
                my_list2.append(dict2[key])
                key_list.append(key)

        swap_dict = dict(zip(my_list1, my_list2))
        for k, v in swap_dict.items():
            lengths = len([i for i, c in enumerate(k) if c != v[i]])
            swaps.append(lengths)

        dict_lengths = {key: len(val) for key, val in swap_dict.items()}
        values_list = list(dict_lengths.values())

        mapped_values = dict(zip(values_list,swaps))

        return mapped_values
