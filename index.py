#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# All the used FUNCTIONS are in index_utils

import os
import csv
import numpy as np
from functools import reduce
import pandas as pd
import nltk
import json


# create list of the links in movies
tree1 = html.parse(r"movies1.html")
movies1 = html.tostring(tree1)
soup1 = BS(movies1)

tree2 = html.parse(r"movies2.html")
movies2 = html.tostring(tree2)
soup2 = BS(movies2)

tree3 = html.parse(r"movies3.html")
movies3 = html.tostring(tree3)
soup3 = BS(movies3)

links = []
for link in soup1.findAll('a'):
    links.append(link.get('href'))
for link in soup2.findAll('a'):
    links.append(link.get('href'))
for link in soup3.findAll('a'):
    links.append(link.get('href'))
len(links)

###

# Creating a data frame of all films with their links
c = ['url','title','intro','plot','film_name','director','producer','writer','starring','music',
           'release_date','runtime','country','language','budget']
df_films = pd.DataFrame(columns = c)
for i in range(30000):
    with open("tsv_files/article-{}.tsv".format(i)) as f:
        reader = csv.reader(f, delimiter='\t')
        l = list(reader)[1]
        r = [links[i]] + l[0:]
        df_films = df_films.append(pd.DataFrame([r],columns = c),ignore_index = True)

###

# Save it to a csv file
df_films.to_csv('film.csv')

###

df_film = pd.DataFrame(pd.read_csv('film.csv'))   # in the film.csv we have a data of all films
df_film.rename(columns = {'Unnamed: 0':'film_id'}, inplace = True) 

###


df_film['plot'] = df_film['plot'].astype(str)
v = {}
df_film['len_text'] = df_film.apply(create_voc,axis=1, vocabulary = v)
mp = map_voc(v) #map
tfldf = invertx_voc(voca)
json.dump(tfldf, open("tfidf.txt",'w'))


