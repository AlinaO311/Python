from cp_project import Sequence  # user-defined array class
import matplotlib.pyplot as plt
import sys
sys.path.append( "path to include directory")

def task13():
    print('---- Task 13 ----')
    dna_or_rna = input("Is the input DNA or RNA? ")
    string = input("Type the sequence: ")
    seq = Sequence(dna_or_rna, string)

    print("Valid sequence? ", Sequence.is_valid(seq, dna_or_rna))
    print(Sequence.complement(seq, dna_or_rna))

    another_type = input("Is the input DNA or RNA? ")
    string2 = input("Type the sequence: ")
    seq2 = Sequence(another_type, string2)

    print("Valid sequence? ", Sequence.is_valid(seq2, another_type))
    print(Sequence.complement(seq2, another_type))


task13()