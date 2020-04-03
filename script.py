import os
import sys

os.system('python GenerateLcsMatrix.py ' + sys.argv[1])
os.system('python GenerateTree.py')
os.system('rm distance_matrix.npy')
