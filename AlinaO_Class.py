import re
import itertools
import string
from typing import List
from collections import defaultdict


class Sequence:
    """sequence class.
    It has the attribute string.

    Attributes:
    string: a string of characters representing a sequence.
    """

    def __init__(self, string):
        """Task 11: automotically changed all chars in string to lowercase."""
        self.string = string.lower()

    def bases(self):
        """ Task 2: method to return number of DNA bases"""
        print(len(self.string))

    def is_dna(self):
        """Task 3: method that validates all the characters as a base."""
        for i in range(len(self.string)):
            if all(c in "acgt" for c in self.string):
                match = True
                return match
            else:
                no_match = False
                return no_match

    def __eq__(self, other):
        """Task 4: Overrides the default implementation"""
        if isinstance(other, Sequence):
            return self.string == other.string.lower()

    def complement(self):
        """ Task 5: returns the complement of the Sequence"""
        basecomplement = {'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
        letters = list(self.string)
        letters = [basecomplement[base] for base in letters]
        return ''.join(letters)

    def non_match(self, other):
        """ Task 6: method that finds the first pair of non-matching bases"""
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
        """Task 10: method which compares the sequence with
        another and returns the number of bases which do
        not match"""
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

def file_read(filename):
    """Task 7: function that reads in ASCII-format files
    and returns an instance of Sequence"""
    with open(filename) as myfile:
        data = myfile.read().replace('\n', '')
    data = data.split()[-1]
    sequence = re.sub("[^ACGTacgt]", "", data)
    my_seq = Sequence(sequence)
    return my_seq.bases()

def task8_split(file):
    """Task 8: method which splits the sequence into genes, returning
    each as a new Sequence instance discarding the separators"""
    with open(file) as myfile:
        data = myfile.read().replace('\n', '')
    data = data.split()[-1]
    sequence2 = re.sub("[^ACGTacgt]", "", data)
    new = [m[0] for m in re.sub(r'(?:(.)(a{10}t{10}))', ' ', sequence2.lower())]
    result = [list(v) for k, v in itertools.groupby(new, key=str.isspace) if not k]
    sublist_sum = sum(isinstance(i, list) for i in result)
    list_of_lists = [''.join(item) for item in result]

    li = {}
    for j in range(sublist_sum):
        li["seq%s" % j] = []

    my_dict = dict(zip(li, list_of_lists))

    d2 = {k: Sequence(v) for k, v in my_dict.items()}
    dict_of_classobj = {k: (v).string for k, v in d2.items()}

    return dict_of_classobj
