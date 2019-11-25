#!/usr/bin/python3
import sys
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
#import

def unique(list1): #συναρτηση που παιρνει μια λιστα και την επιστρεφει χωρις διπλοτυπους χαρακτηρες
    x = np.array(list1)
    return(np.unique(x))

def rmchar(A): #συναρτηση που "ξεγυμνωνει" το κειμενο βγαζοντας τα κεφαλαια και τους χαρακτηρες !@#$(),.
    for i in range(0, len(A)):
        A[i] = A[i].translate({ord(c): None for c in '!@#$(),.'})
        A[i] = A[i].lower()
    return(A)

def compare(d,di): #συναρτηση που υπολογιζει το διανυσμα ορων του καθε κειμένου
    cmp=[]
    for j in range(0,len(d)):
        cnt=0
        for i in range(0,len(di)):
            if d[j]==di[i]:  #αν η λεξη υπαρχει στο κείμενο αυξησε τον μετρητη
                cnt+=1
        cmp.append(cnt) #προσθεσε τον μετρητη στο διανυσμα για δημιουργια τελικου διανυσματος
    return(cmp)

def calculate(d1,d2): #συναρτηση που υπολογιζει την ομοιοτητα συνημιτονου 2 κειμενων
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
    d+=(open(sys.argv[x], "r").read().split()) #αναγνωση κειμενων και τοποθετηση σε λιστα λεξεων

d = unique(rmchar(d)) # αφαιρεση διπλοτυπων απο λιστα, τοποθετηση σε αλφαβητικη σειρα, και αφαιρεση χαρακτηρων "!@#$(),." και κεφαλαιων

l=len(sys.argv)
res=[]
doc1=[]
for x in range(2,l): # αναγνωση ανα 2 των κειμενων και συγκριση με την λιστα που δημιουργησαμε ωστε να βγαλουμε το δυανισμα απο καθε κειμενο
    for y in range(x,l-1):
        d1 = open(sys.argv[x], "r").read().split()
        d2 = open(sys.argv[y+1], "r").read().split()
        cos= calculate(d1,d2) # υπολογισμος της ομοιοτητας 2 κειμενων
        res.append(cos) # τοποθετηση απαιτουμενων πληροοριων για την εκτυπωση
        res.append(sys.argv[x])
        res.append(sys.argv[y+1])

doc1 = [res[i:i + 3] for i in range(0, len(res),3)] # μετατροπη της λιστας σε "πινακα" οπου περιεχει {[cos,document1,document2]...}
doc1 = sorted(doc1, key=lambda x:x[0], reverse = True) # ταξινομηση του "πινακα" σε φθινουσα σειρα αναλογα με το cos
for z in range(0, int(sys.argv[1])):
    print ("Cosine difference of",doc1[z][1],",", doc1[z][2],"is", doc1[z][0]) # εκτυπωση επιθυμητων αποτελεσματων
