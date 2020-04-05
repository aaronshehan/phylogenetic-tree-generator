import re
import sys
from itertools import combinations

#function to read the input file, takes filename as the parameter
def readFile(filename):
    with open(filename, 'r') as f:	#open the inputfile
        lines = f.readlines()	#reaad the lines

    names = []	#make a list of names
    sequences = []	#make a list of sequences	

    for line in lines:	#iterative over the line
        if line == '\n': continue	#if there is a newline ignore it and continue
        l = line.rstrip()	#strip the line
        if re.search('^>.*$', l):	#split line based on greater than character symbol using regex
            names.append(l)	#apped the names
        else:
            sequences.append(l)	#if there is not a greater than caharacter symbol then append the sequence
    f.close()	#close the input file
    return (names, sequences)	#return the list of names and sequences

#function that finds the longest common subsequence between two strings, takes two strings as the parameters
def lcs(str1, str2): 
    str1_len = len(str1)	#store the length of the first string
    str2_len = len(str2)	#store the length of the second string

    L = [[None] * (str2_len + 1) for _ in range(str1_len + 1)]	#create the matrix
  
    for i in range(str1_len + 1):	#iterate over the length of the first matrix plus one
        for j in range(str2_len + 1):	#iterate over the length of the second matrix plus one
            L[i][j] = 0 if i==0 or j==0 else(L[i-1][j-1]+1 if str1[i-1]==str2[j-1] else max(L[i-1][j], L[i][j-1]))	#store the lcs value inside the matrix

    return L[str1_len][str2_len]	#retrun the lcs value of the two strings

#the main function that calls all the other functions
def main():
    names_and_seq = readFile(sys.argv[1])	#take the input file name as the command line argument and read the input file
    names_and_seq = [(i.split(' ', 1)[1], j) for i,j in zip(names_and_seq[0], names_and_seq[1])]	#format the names and sequence

    for i in combinations(names_and_seq, 2):	#make combination of every name and sequence in the input file
        print('-' * 39)	#print a '-' for formating
        print('|'.ljust(1), 'Species A'.ljust(15), 'Species B'.ljust(15), 'LCS'.ljust(1), '|')	#print a '|' for formatting
        print('|'.ljust(1), i[0][0].ljust(15), i[1][0].ljust(15), str(lcs(i[0][1], i[1][1])).ljust(1), '|')	#print a '|' for formatting
    print('-' * 39)	#print a '-' for formatting

if __name__ == "__main__":
    main()	#call the main function 
	

