#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# We want just to parse the intro paragraphs and plot paragraphs
def intro_plot(soup,index=0):
    try:
        Node = soup.find_all('p')[index]
        lst = [Node.text]
        nextNode = Node
        while True:
            nextNode = nextNode.next_sibling

            try:
                tag_name = nextNode.name
            except AttributeError:
                tag_name = ""
            if tag_name == "p":
                lst.append(nextNode.text)
            else:
                break
    except:
        lst = None
    return lst

# parsing the desire informations
def soup_parser(soup,info=None,next_tag='td',class_name=None):
    if next_tag:
        element = soup.find('th', text=info)
        if not element:
            element = 'NA'
        else:
            if info=='Release date':
                element = element.find_next(next_tag).text.split()[0]
            else:
                element = element.find_next(next_tag).text
    else:
        element = soup.find('h1').text
    return element

