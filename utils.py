#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Data preprocessing
def f_clean(i):
    s_word = stopwords.words('english')
    i = i.replace("\\n","")
    i = i.lower()
    i = i.translate(str.maketrans("","",string.punctuation))
    word = word_tokenize(i) 
    
    filt = [w for w in word if not w in s_word]
    ps = PorterStemmer()
    stemmed = []
    for w in filt:
        stemmed.append(ps.stem(w))
    
    punctuation = list(string.punctuation)
    punctuation.append("''")
    
    without_punt = [w for w in stemmed if not w in punctuation]

    return without_punt

#we map the keys of the vocabulary in a number
def map_voc(voc):       
    i = 0 
    new_voc = {}
    for e in voc.keys():
        new_voc[e] = i
        i +=1
    return new_voc

