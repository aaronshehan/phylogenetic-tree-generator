'''Our source for lcs is:
https://www.geeksforgeeks.org/longest-common-substring-dp-29/'''
'''Our source for the generateLcsMatrix.py file is:
https://github.com/SupriyaL/Hierarchical-Clustering/blob/master/Preprocess.py'''


import time
import sys
import numpy as np


def lcs(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)

    L = [[0] * (str2_len + 1) for _ in range(str1_len + 1)]

    for i in range(str1_len + 1):
        for j in range(str2_len + 1):
            L[i][j] = 0 if i == 0 or j == 0 else (
                L[i - 1][j - 1] + 1 if str1[i - 1] == str2[j - 1] else max(L[i - 1][j], L[i][j - 1]))
    g=L[str1_len][str2_len]
    return (str1_len-g)+(str2_len-g)


def distance_matrix():
    global dist
    for i in range(0, count + 1):
        for j in range(0, i):
            if i != j:
                dist[i][j] = lcs(seq[i], seq[j])
                dist[j][i] = dist[i][j]
                values.insert(i, dist[i][j])
    values.sort()
    return dist


def preprocess():
    global count
    t = len(lines)
    for i in range(len(lines)):
        line = lines[i]
        if line[0] == '>':
            r = ""
            i += 1
            line = lines[i]
            while line[0] != '>':
                r += line
                i += 1
                if i < t:
                    line = lines[i]
                else:
                    break
            count += 1
            seq[count] = r


# MAIN
"""
Stores the distance matrix in a .npy file
"""
f = open(sys.argv[1], "r").read()
lines = f.splitlines()
lines=list(filter(lambda x: (x != ''), lines)) 
seq = dict()
values = list()
count = -1
start = time.time()
preprocess()
print("Function is reading input file please wait...\t" + str(time.time() - start))
dist = np.zeros(shape=(count + 1, count + 1))
start = time.time()
a = distance_matrix()
print("Distance Matrix Calculation is done!" + str(time.time() - start))
np.save('distance_matrix.npy', a)
