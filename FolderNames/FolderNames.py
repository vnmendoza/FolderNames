from __future__ import print_function
import os

path = input("what is the file path? \n")
 
files = os.listdir(path)
f= open("PolesInFolder.txt","w+")
for name in files:
    f.write(name + "\n")    
f.close()
