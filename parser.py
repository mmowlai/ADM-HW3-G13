#!/usr/bin/env python
# coding: utf-8

# In[1]:


# All the Functions are in parser_utils.py

import os
from bs4 import BeautifulSoup as BS
import csv
import pandas as pd
from time import time 


# In[2]:


# Here at path we have all the html files
path = './0-30k/'


# In[6]:


if not os.path.exists('tsv_files'):
    os.makedirs('tsv_files')


# In[7]:


# creating the all tsv files
columns = ['title', 'intro', 'plot', 'film_name', 'director', 'producer', 'writer', 'starring', 'music', 'release date', 'runtime', 'country', 'language', 'budget']
exceptions = []
start = time()
for subdir, dirs,files in os.walk(path):
    for file in files:
        try:
            soup = BS(open(path+file, encoding="utf8"), "html.parser")
            title = soup_parser(soup=soup,next_tag=None,class_name='firstHeading')
            intro = intro_plot(soup=soup)
            plot = intro_plot(soup=soup,index=len(intro))
            index = 0
            while intro == ['\n']:
                index+=1
                intro = intro_plot(soup=soup,index=index)
                plot = intro_plot(soup=soup,index=len(intro)+index)
            director = soup_parser(soup=soup, info='Directed by')
            producer = soup_parser(soup=soup, info='Produced by')
            writer = soup_parser(soup=soup, info='Written by')
            starred = soup_parser(soup=soup, info='Starring')
            music = soup_parser(soup=soup, info='Music by')
            date = soup_parser(soup=soup,info='Release date')
            duration = soup_parser(soup=soup, info='Running time')
            country = soup_parser(soup=soup, info='Country')
            language = soup_parser(soup=soup, info='Language')
            budget = soup_parser(soup=soup, info='Budget')
            
            all_info = [title,intro,plot,title,director,producer,writer,starred,music,date,duration,country,language,budget]
            with open('tsv_files/%s.tsv' %(file[:-5]), 'wt',encoding="utf-8") as out_file:
                tsv_writer = csv.writer(out_file, delimiter='\t')
                tsv_writer.writerow(columns)
                tsv_writer.writerow(all_info)

        except:
            print('Could not parse html file:', file)
            exceptions.append(file)
print("Execution time is:",time()-start)

