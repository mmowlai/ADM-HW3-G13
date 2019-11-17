#!/usr/bin/env python
# coding: utf-8

# In[2]:


from itertools import combinations

sequence = 'dataminingsapienza'

count = set()
done = False
for i in range(len(sequence), 1, -1):
    sub = list(combinations(sequence, i))
    for k in range(len(sub)):
        if sub[k] == sub[k][::-1]:
            count.add(len(sub[k]))
            print(sub[k])
            done = True
            break
    if done: break

print(max(count))

