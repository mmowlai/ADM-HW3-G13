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


# create the vocabulary and set a new column in the dataframe with the len on the plot+intro
def create_voc(row,vocabulary):
    film_id = row['film_id']
    try:
        text = f_clean(row['intro']+row['plot'])
    except Exception as e:
        print(film_id,e)
        return 0
    for w in text:
        if w not in vocabulary:
            vocabulary[w] = {film_id:1}
        else:
            if film_id not in vocabulary[w]:
                vocabulary[w][film_id] = 1
            else:
                vocabulary[w][film_id] += 1
    return len(text)

#we map the keys of the vocabulary in a number
def map_voc(voc):       
    i = 0 
    new_voc = {}
    for e in voc.keys():
        new_voc[e] = i
        i +=1
    return new_voc

# Now we define a function to calculates the tf idf
def invertx_voc(voc):
    new_voc = {}
    for k in voc.keys():
        repetition = len(voc[k])
        IDF = math.log(30000/repetition)
        for elem in voc[k].keys():
            val = voc[k][elem]
            length = list(df_film[df_film['film_id'] == int(elem)]['len_text'])[0]
            
            tf = val/length
            
            if k not in new_voc:
                new_voc[k] = {elem : tf*IDF}
            else:
                new_voc[k][elem] = tf*IDF
    return new_voc

