def find_substrings(seq1, seq2):
    uniques = [i for i in seq1 for el in seq2 if i in el]
    return sorted(set(uniques), key=uniques.index)


sequence1 = input().split(', ')
sequence2 = input().split(', ')
print((find_substrings(sequence1, sequence2)))
