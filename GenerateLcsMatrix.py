'''Our source for lcs is:
https://www.geeksforgeeks.org/longest-common-substring-dp-29/'''
'''Our source for the generateLcsMatrix.py file is:
https://github.com/SupriyaL/Hierarchical-Clustering/blob/master/Preprocess.py'''


import time
import sys
import numpy as np

#function that finds the longest common subseqence takes two strings as parameters
def lcs(str1, str2):
    str1_len = len(str1)    #calculate the length of string 1
    str2_len = len(str2)    #calculate the length of string 2

    L = [[0] * (str2_len + 1) for _ in range(str1_len + 1)] #populate matrix size

    for i in range(str1_len + 1):   #iterate over the length of string 1
        for j in range(str2_len + 1):   #iterate over the length of string 2
            L[i][j] = 0 if i == 0 or j == 0 else (  #set matrix = 0 if i or j is 0
                L[i - 1][j - 1] + 1 if str1[i - 1] == str2[j - 1] else max(L[i - 1][j], L[i][j - 1]))   #else store the lcs value
    g=L[str1_len][str2_len] #store the row and col of the L matrix
    return (str1_len-g)+(str2_len-g) #return the lcs of the given two strings

#function to make a distance matrix based on lcs value
def distance_matrix():
    global dist #declare dist value as global
    for i in range(0, count + 1):   #iterate over the count i.e, number of combinations
        for j in range(0, i): #itrative over i
            if i != j:  #if i is not equal to j
                dist[i][j] = lcs(seq[i], seq[j])    #put lcs value in distance matrix
                dist[j][i] = dist[i][j] #format distance matrix
                values.insert(i, dist[i][j])    #insert values to distance matrix
    values.sort()   #sort the values
    return dist #return the distance matrix based on lcs values

#function used to read from fasta file
def preprocess():
    global count    #global count value
    t = len(lines) #store the length of the line as t
    for i in range(len(lines)): #itrate over lines
        line = lines[i] #store lines[i] into a line
        if line[0] == '>': #if there is a greater than symbol on a line
            r = "" #take care of empty string
            i += 1 #increment i
            line = lines[i] #store in next line
            while line[0] != '>': #check for lines which do not beign with the greater than character
                r += line #set r to line
                i += 1 #increment i
                if i < t: #check if i is less than line length
                    line = lines[i] #store lines[i] as line
                else: # if line starts with greater than
                    break #then break
            count += 1 #increment count
            seq[count] = r #store values in seq[count]


# MAIN
"""
Stores the distance matrix in a .npy file
"""
f = open(sys.argv[1], "r").read() #read file from command line arg1
lines = f.splitlines() #split the lines
lines=list(filter(lambda x: (x != ''), lines)) #filter out junk empty char
seq = dict() #store seq in dict
values = list() #values are a list
count = -1 #set count to initial value less than 0
start = time.time() #start timer
preprocess() #start the preprocess to readinput file
print("Function is reading input file please wait...\t" + str(time.time() - start)) #preprocess is done
dist = np.zeros(shape=(count + 1, count + 1)) #add zero values to distance matrix
start = time.time() #start timer
a = distance_matrix() #store distance matrix in a
print("Distance Matrix Calculation is done! " + str(time.time() - start)) #distance matrix is done 
np.save('distance_matrix.npy', a) #save the distance matrix as a numpy matrix in a temp file for GenerateTree.py to use
