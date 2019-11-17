#!/usr/bin/env python
# coding: utf-8

# ## All functions for search engines
# 

# In[117]:


# The first search engine
def query1():
    a = input("Enter a Query: ")
    a = f_clean(a)     #we need to clean the input so we have the match between the word
    l = []
    for i in a:
        try:
            l1 = list(voca[i].keys())
            l += [l1]
        except Exception as e:
            print("Not in any films:"+str(a))
            return
    e = list(reduce(set.intersection, [set(item) for item in l ]))  # we find the intersection from all the lis
    p = df_film[df_film['film_id'].isin(e)]  #we select only the film that are in the intesection
    p.reset_index(inplace=True)
    return p[['title','intro','url']].head(10)


# In[118]:


query1()


# In[38]:


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


# In[79]:


tfldf = invertx_voc(voca)
json.dump(tfldf, open("tfidf.txt",'w'))


# In[39]:


tfldf = json.load(open("tfidf.txt"))


# In[119]:


# Second search engine with cosine similarity
def query2():
    def cosSim(row):
        film_vector = []
        for elem in cleaned_query:
            if(elem in tfldf):
                if(str(row['film_id']) in tfldf[elem]):
                    film_vector.append(tfldf[elem][str(row['film_id'])])
                else:
                    film_vector.append(0)
            else:
                film_vector.append(0)
        query_vector_idf = tfidf_query(cleaned_query)
        cos_sim = cosine_similarity([film_vector], [query_vector_idf])[0][0]
        return cos_sim
    def tfidf_query(q):
        tfidf_q = []
        for elem in q:
            tfidf_q.append(1)
        return tfidf_q

    query = input("Enter a Query: ")
    tfldf = json.load(open("tfidf.txt"))
    cleaned_query = f_clean(query)
    query_vector = tfidf_query(cleaned_query)
    df_film['Similarity'] = df_film.apply(cosSim, axis = 1)
    ndf = df_film[['title', 'intro','url', 'Similarity']]
    result = ndf[ndf['Similarity'] > 0.7].sort_values('Similarity', ascending = False).head(10)
    return result  


# In[120]:


query2()


# In[121]:


# Third search engine with the most similarity of desired runtime and the film's runtime
def query3():
    q_min = input("DESIRE RUNTIME(in mins): ")
    inp = input("Enter The Query: ")
    inp = f_clean(inp)     #we need to clean the input
    l = []
    for i in inp:
        try:
            l1 = list(voca[i].keys())
            l += [l1]
        except Exception as e:
            print("Not in any films:"+str(inp))
            return
    e = list(reduce(set.intersection, [set(item) for item in l ]))  # we find the intersection from all the lis
    p = df_film[df_film['film_id'].isin(e)]  #we select only the film that are in the intesection
    p.reset_index(inplace=True)
    p = p[['title','intro','url','runtime']]
    sim = []
    # here we calculate sort-scoring
    for i in range(len(p.runtime)):
        try:
            resrun = int(p.runtime[i].split('minutes')[0].strip())
            qrun   = int(q_min.strip())
            calc   = abs(resrun - qrun)
            sim.append(calc)
        except:
            # in some fields that we don't have any data for runtimes we replace it by a very large number
            sim.append(int('1000000')) 
    p['Differrence'] = sim   
    p.sort_values('Differrence',ascending = True,inplace = True)
    return p.head(10)    


# In[129]:


query3()


# In[130]:


# The total search engines
def search_engines():
    q = input("Choose which engine to search[1,2 or 3](ex: 1): \n")
    if q == '1':
        print('** THE SIMPLE QUERY **')
        return query1()
    if q == '2':
        print('** THE QUERY WITH HIGHEST SIMILARITY **')
        return query2()
    if q == '3':
        print('** THE QUERY WITH HIGHEST SIMILARITY With DESIRED RUNTIME **')
        print('** The lower is the Differrence, the highest is the similarity **')
        return query3()
    else:
        print('** PLEASE TRY AGAIN WITH CHOOSING A SEARCH ENGINE **')
        
     


# In[ ]:


search_engines()

