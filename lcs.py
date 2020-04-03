import re
import sys
from itertools import combinations

def readFile(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    names = []
    sequences = []

    for line in lines:
        if line == '\n': continue
        l = line.rstrip()
        if re.search('^>.*$', l):
            names.append(l)
        else:
            sequences.append(l)
    f.close()
    return (names, sequences)


def lcs(str1, str2): 
    str1_len = len(str1) 
    str2_len = len(str2) 

    L = [[None] * (str2_len + 1) for _ in range(str1_len + 1)] 
  
    for i in range(str1_len + 1): 
        for j in range(str2_len + 1): 
            L[i][j] = 0 if i==0 or j==0 else(L[i-1][j-1]+1 if str1[i-1]==str2[j-1] else max(L[i-1][j], L[i][j-1]))

    return L[str1_len][str2_len] 

def main():
    names_and_seq = readFile(sys.argv[1])
    names_and_seq = [(i.split(' ', 1)[1], j) for i,j in zip(names_and_seq[0], names_and_seq[1])]

    for i in combinations(names_and_seq, 2):
        print('-' * 39)
        print('|'.ljust(1), 'Species A'.ljust(15), 'Species B'.ljust(15), 'LCS'.ljust(1), '|')
        print('|'.ljust(1), i[0][0].ljust(15), i[1][0].ljust(15), str(lcs(i[0][1], i[1][1])).ljust(1), '|')
    print('-' * 39)

if __name__ == "__main__":
    main()
	

