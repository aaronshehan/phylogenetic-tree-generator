from itertools import permutations

def lcs(X, Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n + 1) for i in xrange(m + 1)] 
  
    """Following steps build L[m + 1][n + 1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 
# end of function lc

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]




def readFromFile(name):
	DNA_Sequence=[]
	with open(name) as f:
		for line in f:
			if not line.lstrip().startswith('>'):
				DNA_Sequence.append(line)
	
	#print(DNA_Sequence)
	return DNA_Sequence

def readFromFile2(name):
	animalName=[]
	with open(name) as fh:
		for line in fh:
			if line.startswith('>'):
				animalName.append(line)
	return animalName
	
def merge(list1, list2): 
	merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
	return merged_list 

x=readFromFile('tulp3_relatives-2.txt')
y=readFromFile2('tulp3_relatives-2.txt')
y = map(lambda s: s.strip(), y)
#print(y)
x = map(lambda s: s.strip(), x)
#print(x)
i=0 #loop counter
length = len(x)  #list length 
while(i<length):
	if(x[i]==''):
		x.remove (x[i])
		# as an element is removed	
		# so decrease the length by 1	
		length = length -1  
		# run loop again to check element							
		# at same index, when item removed 
		# next item will shift to the left 
		continue
	i = i+1
z=merge(y,x)
#print(z)

perm = permutations(z, 2) 
  
# Print the obtained permutations 
for i in list(perm): 
    #print(i)
	res = [list(ele) for ele in i]
	g,h=split_list(res)
	d2 = [item[1] for item in g]
	d3 = [item[1] for item in h]
	sa = d2[0]
	sb = d3[0]
	print(g[0][0],h[0][0])
	print(lcs(sa,sb))
	
	
	

