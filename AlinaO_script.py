from AlinaO_Class import Sequence  # user-defined array class
from AlinaO_Class import file_read
from AlinaO_Class import task8_split
import re
import matplotlib.pyplot as plt
import sys
sys.path.append( "path to include directory")


def task1():
    print('---- Task 1 ----')
    string = "ACGTACGTTTCGTGTGTG"
    sequence = Sequence(string=string)
    print(sequence.string)

def task2():
    print('---- Task 2 ----')
    string = "ACGTACGTTTCGTGTGTG"
    sequence = Sequence(string)

    b_string = "ACGTACGTT"
    b_sequence = Sequence(b_string)
    #print(b_sequence.bases())
    print(sequence.bases())

def task3():
    print('---- Task 3 ----')
    string1 = "ACGT183681CGTCGryNaGT"
    string2 = "TTATTACGTCGAGATCG"
    sequence1 = Sequence(string1)
    sequence2 = Sequence(string2)
    DNA = '[*AaCcGgTt]+$'

    print("Test " + sequence1.string + " contains only ACG or T ")
    print(Sequence.is_dna(sequence1))
    assert all(c in DNA for c in sequence1.string) == Sequence.is_dna(sequence1)

    print("Test " + sequence2.string + " contains only ACG or T ")
    print(Sequence.is_dna(sequence2))
    assert (all(c in DNA for c in sequence2.string) == Sequence.is_dna(sequence2))

def task4():
    print('---- Task 4-----')
    stringa = "ACGtACGTTCGTGTGTG"
    stringb = "ACGTACGTtcGTGTGTG"
    stringc = "AGTACGTTCGTGTGTG"
    stringd = "TACGTGATCGTACTTATTT"
    stringe = "TACGTGATCGTACTTATTT"

    sequence_a = Sequence(stringa)
    sequence_b = Sequence(stringb)
    sequence_c = Sequence(stringc)
    sequence_d = Sequence(stringd)
    sequence_e = Sequence(stringe)

    assert (sequence_a == sequence_b)
    assert (sequence_d == sequence_e)

    assert sequence_a != sequence_c

def task5():
    print('---- Task 5 ----')
    string = "ACGTACGTTCGTGTGTG"
    seq = Sequence(string)

    print(string)
    print(Sequence.complement(seq))

def task6():
    print('---- Task 6 ----')
    stringa = "ACGTGCG"
    stringb = "ACgtGCG"
    stringc = "AGTTCGTGGTGCCCCC"
    stringd = "ACGTTCG"

    sequence_a = Sequence(stringa)
    sequence_b = Sequence(stringb)
    sequence_c = Sequence(stringc)
    sequence_d = Sequence(stringd)

    print(Sequence.non_match(sequence_a, sequence_b))
    print(Sequence.non_match(sequence_a, sequence_d))
    return Sequence.non_match(sequence_a, sequence_c)



def task7():
    print('---- Task 7 ----')
    filename = input("Enter file to count bases: ")
    return file_read(filename)
    genefile =  input("Enter file to verify: ")
    with open(genefile) as myfile:
        data = myfile.read().replace('\n', '')
    data = data.split()[-1]
    sequence = re.sub("[^ACGTacgt]", "", data)
    return len(sequence)

def task8():
    print('---- Task 8 ----')
    filename = input("Enter file to find first sequence length: ")
    task8_dict = task8_split(filename)
    dict_lengths = {k: len(v) for k, v in task8_dict.items()}
    print(dict_lengths["seq0"])

def task9():
    print('---- Task 9 ----')
    filename = input("Enter file to get histogram of lengths: ")
    my_task9 = task8_split(filename)
    dict_lengths = {k: len(v) for k, v in my_task9.items()}
    plt.hist( dict_lengths.values())
    plt.xlabel('Base Length')
    plt.ylabel('Gene Sequences')
    plt.title('Histogram of Gene Lengths')
    plt.show()
    #plt.savefig('Hist.png')

def task10():
        print('---- Task 10 ----')
        filename = input("Enter a first file to compare swaps: ")
        first_file = task8_split(filename)

        second_filename = input("Enter a second file to compare swaps: ")
        second_file = task8_split(second_filename)

        print("Number of swaps per individual gene length: ")
        print(Sequence.swap_method(first_file, second_file))

        plot_dict = Sequence.swap_method(first_file, second_file)

        x = plot_dict.keys()
        y = plot_dict.values()
        plt.scatter(x, y)
        plt.xlabel('Gene Length')
        plt.ylabel('Number of swap mutations')
        plt.title('Swaps per gene')
        plt.show()
        #plt.savefig('Last.png')

#task1()
#task2()
#task3()
#task4()
#task5()
#task6()
#task7()
task8()
#task9()
#task10()