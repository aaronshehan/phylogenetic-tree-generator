'''Our source for the generateTree.py file is:
https://github.com/SupriyaL/Hierarchical-Clustering/blob/master/code_1.py'''


import matplotlib
matplotlib.use('Agg')
from scipy.cluster import hierarchy
import numpy as np
import scipy
import matplotlib.pyplot as plt
import time


"""
input: Two numbers
output: Minimum of the two numbers
"""

#function to find the minimum of two numbers takes two doubles as parameters
def minimum(double1, double2):
    if double1 < double2:   #compare the two number and check if number 1 is less than number 2
        return double1  #return number 1
    else:
        return double2 #else return number 2


"""
input: Two numbers
output:Maximum of the two numbers
"""

#function to find the maixmum of two numbers takes two doubles as parameters
def maximum(double1, double2):
    if double1 > double2: #if number 1 is greater than number 2 
        return double1  #return number 1
    else:
        return double2 #else return number 2


"""
Performs agglomerative clustering
input:	distance matrix,its size and iteration value k
output:	returns the modified distance matrix
"""

#function to make groupings based on lcs values, this function takes in the distance matrix from GenerateLcsMatrix.py
def clust(a, size, k):
    min = 1000000.0 #set treshold value for min
    m = (len(a))  #set m=number of protein sequences
    n = (len(a)) #set n=number of protein sequences
    for i in range(0, size - 1): #iterate over size of matrix - 1
        for j in range(1, size): #iterate over size of matrix
            if i < j: #if i is less than j
                if a[i][j] < min: #check if a[i][j] in matrix is less than min
                    min = a[i][j] #set min as a[i][j] 
                    m = i #set m =i
                    n = j #set n=j
    big_list = [] #make a initial list
    if m < n:  # To keep track of the order
        big_list.append(dict[m]) #append m into list
        big_list.append(dict[n]) #append n into list
        dict[m] = big_list #set dict[m] as the big list
        del dict[n] #delete dict[n] as we do not need it
    # This section of the function is used to fill values in Z
    if new_clusters[m] == -1 and new_clusters[n] == -1:  # both are -1
        Z[k][0] = m #set Z[k][0] as m
        Z[k][1] = n #set Z[k][1] as n
        x = minimum(m, n) #find the minimum value of m and n
        new_clusters[x] = size + k #set the new grouping as size plus k
        Z[k][3] = 2 #set Z[k][3] as 2
    elif new_clusters[m] != -1 and new_clusters[n] != -1:  # both not -1
        Z[k][0] = new_clusters[m] #set Z[k][0] as new cluster
        Z[k][1] = new_clusters[n] #set Z[k][1] as new cluster
        if m < n: #check is m is less than n
            new_clusters[m] = size + k #set new cluster as size plus k
        else: #if m is greater than n
            new_clusters[n] = size + k #if m is greater than n set new cluster is size plus k
        Z[k][3] = Z[int(maximum(Z[k][0], Z[k][1]) - size)][3] + 1 #set Z[k][3] as Z[maximum valive of Z[k][0], and Z[k][1]-size][3] plus 1
    elif new_clusters[m] != -1 and new_clusters[n] == -1:  # m is not -1 and n is -1
        if m < n: #check is m is less than n
            Z[k][0] = new_clusters[m] #set Z[k][0] as new cluster
            Z[k][1] = n #set Z[k][1] as n
            Z[k][3] = Z[int(maximum(Z[k][0], Z[k][1]) - size)][3] + 1 #set Z[k][3] as Z[maximum valive of Z[k][0], and Z[k][1]-size][3] plus 1
            new_clusters[m] = size + k #set new cluster as size plus k
        else: #if m is greater than n
            Z[k][0] = m #set Z[k][0] as m
            Z[k][1] = new_clusters[n] #set Z[k][1] as new cluster
            Z[k][3] = Z[int(maximum(Z[k][0], Z[k][1]) - size)][3] + 1 #set Z[k][3] as Z[maximum valive of Z[k][0], and Z[k][1]-size][3] plus 1
            new_clusters[n] = size + k
    elif new_clusters[m] == -1 and new_clusters[n] != -1:  # m is -1 and n is not -1
        if m < n:   #check if m is less than n
            Z[k][0] = m #set Z[k][0] as m
            Z[k][1] = new_clusters[n] #set Z[k][1] as a new cluster
            Z[k][3] = Z[int(maximum(Z[k][0], Z[k][1]) - size)][3] + 1 #set Z[k][3] as Z[maximum valive of Z[k][0], and Z[k][1]-size][3] plus 1
            new_clusters[m] = size + k #set new cluster as size plus k
        else: #if m is greater than n
            Z[k][0] = new_clusters[m] #set Z[k][0] as the new cluster
            Z[k][1] = n #set Z[k1][1] as n
            Z[k][3] = Z[int(maximum(Z[k][0], Z[k][1]) - size)][3] + 1 #set Z[k][3] as Z[maximum valive of Z[k][0], and Z[k][1]-size][3] plus 1
            new_clusters[n] = size + k #set new cluster as size plus k
    else: #if conditions are not met 
        print("Error") #print error
    Z[k][2] = min #set Z[k][2] as the min
    for j in range(0, size): #iterate over the size
        if j != n: #is j is not equal to n
            a[j][m] = minimum(a[j][m], a[j][n]) #set a[j][m] as the minimum of a[j][m] and a[j][n]
        a[m][j] = a[j][m] #set a[m][j] as a[j][m]
        a[j][n] = 10000.0 #set large values for a[j][n]
        a[n][j] = 10000.0 #set large values for a[n][j]
    return a #return the matrix a


"""
This is used to form the dendrogram
"""

#this function is used to make a augmented dendrogram which is stored in a png file
def augmented_dendrogram(*args, **kwargs): #takes in function parameters
    data = scipy.cluster.hierarchy.dendrogram(*args, **kwargs) #uses scipy to store data
    if not kwargs.get('no_plot', False): #if there is no data return false
        for i, d in zip(data['icoord'], data['dcoord']): #iterate over data
            x = 0.5 * sum(i[1:3]) #set the x plot scale
            y = d[1] #set the y plot scale
            plt.plot(x, y, 'ro') #plot x and y
            plt.annotate("%.3g" % y, (x, y), xytext=(0, 12), textcoords='offset points', va='top', ha='center') #format the data
    return data #return the data which will be stored in a png file


# MAIN
a = np.load('distance_matrix.npy') #load the distance matrix file from GenerateLcsMatrix.py
size = len(a) #store size as the length of the distance matrix
dict = {} #create a dictionary called dict
Z = np.zeros(shape=(size - 1, 4)) #set the matirx Z with zeroes
new_clusters = {} #create a dictionary for new clusters
for i in range(0, size): #itreate over the size of the distance matrix
    list = [] #make a list
    list.append(i) #append i into the list
    dict[i] = list #store values in dict[i]
for i in range(0, size): #iterate over the size of the distance matrix
    new_clusters[i] = -1 #set new clusters to default value of -1
start = time.time() #start a timer
for k in range(0, size - 1): #iterate of the size of the distance matrix - 1
    a = clust(a, size, k) #make a cluster and sotre it in the distance matrix
print("Clustering function is working please wait... The results are in PyhlogeneticTreePicture.png\t" + str(time.time() - start)) #print that the clustering function is working
# Plot dendrogram
names = [i for i in range(0, size)] #sotre the names for the dendrogram
plt.figure(figsize=(25, 25)) #format the background
plt.title('Hierarchical Clustering Dendrogram (Agglomerative)') #give the graph a title
plt.xlabel('Sequence No.') #give the graph a x label
plt.ylabel('Distance') #give the graph a y label
x=augmented_dendrogram(Z, labels=names, show_leaf_counts=True, p=25, truncate_mode='lastp') #format the graph
plt.savefig('PyhlogeneticTreePicture.png')  #save the graph as PhylogenticTreePicture.png
