#!/usr/bin/python3
import sys
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()

def unique(list1): # Function that takes a list and returns it without duplicate characters
    x = np.array(list1)
    return(np.unique(x))

def rmchar(A): # Function that "strips" the text by removing capital letters and characters !@#$(),.
    for i in range(0, len(A)):
        A[i] = A[i].translate({ord(c): None for c in '!@#$(),.'})
        A[i] = A[i].lower()
    return(A)

def compare(d,di): # Function that calculates the term vector of each text
    cmp=[]
    for j in range(0,len(d)):
        cnt=0
        for i in range(0,len(di)):
            if d[j]==di[i]:  # If the word exists in the text, increase the counter
                cnt+=1
        cmp.append(cnt) # Add the counter to the vector to create the final vector
    return(cmp)

def calculate(d1,d2): # Function that calculates the cosine similarity of 2 texts
    d1 = rmchar(d1)
    d2 = rmchar(d2)
    d1 = compare(d,d1)
    d2 = compare(d,d2)
    dot= np.dot(d1,d2, out=None)
    ld1= np.linalg.norm(d1,2)
    ld2= np.linalg.norm(d2,2)
    cos= 0
    if ld1*ld2!=0:
        cos= dot/(ld1*ld2)
    return(cos)

d=[]
l1=len(sys.argv)
for x in range(2,l1):
    d+=(open(sys.argv[x], "r").read().split()) # Read texts and put them in a list of words

d = unique(rmchar(d)) # Remove duplicates from the list, sort in alphabetical order, and remove characters "!@#$(),." and capital letters

l=len(sys.argv)
res=[]
doc1=[]
for x in range(2,l): # Read texts in pairs and compare with the list we created to get the vector from each text
    for y in range(x,l-1):
        d1 = open(sys.argv[x], "r").read().split()
        d2 = open(sys.argv[y+1], "r").read().split()
        cos= calculate(d1,d2) # Calculate the similarity of 2 texts
        res.append(cos) # Place required information for printing
        res.append(sys.argv[x])
        res.append(sys.argv[y+1])

doc1 = [res[i:i + 3] for i in range(0, len(res),3)] # Convert the list to a "table" containing {[cos,document1,document2]...}
doc1 = sorted(doc1, key=lambda x:x[0], reverse = True) # Sort the "table" in descending order according to cos
for z in range(0, int(sys.argv[1])):
    print ("Cosine difference of",doc1[z][1],",", doc1[z][2],"is", doc1[z][0]) # Print desired results
