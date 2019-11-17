#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import time


# # Creating the list of movies' links

# In[2]:


movie_list = []


# In[4]:


urls = ['https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies1.html',
        'https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies2.html',
        'https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies3.html']
       
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a', href=True):
        movie_list.append(link['href'])
        with open('movie_list.txt', 'a') as f:
            f.write(link['href'] + "\n")  


# # Getting all the WebPages

# In[33]:


for movie in range(len(movie_list)):
    try:
        response = requests.get(movie_list[movie])
    except:
        time.sleep(1201)  # 20 mins sleep in case of blocking by wikipedia
        response = requests.get(movie_list[movie])
    soup = BeautifulSoup(response.text, 'html.parser')
    name = "article-"+ str(movie) +".html"
    page = str(soup)
    time.sleep(1)
    with open(name, 'a') as f:
        f.write(page)
        


# In[ ]:




