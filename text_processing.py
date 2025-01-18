#!/usr/bin/env python
# coding: utf-8

# In[7]:


def remove_punc(input_text):
    punctuation_marks = ['.',',','"','{','}',';',':','-','?','!','#','&','(',')','[',']','/','%',"'",'\\','`','~','|','@','^','$','"']
    
    output_text = ""
    for char in input_text:
        if char not in punctuation_marks:
            output_text += char
    return output_text


# In[8]:


def remove_stopmarks(input_text):
    stop_marks = ['a', 'about', 'above', 'after', 'again','on', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren’t', 'as', 'at',
    'be', 'because']
    
    word = input_text.split()
    
    filtered_words = []
    for word in words:
        if word.lower() not in stop_marks:
            filtered_words.append(word)
    output = ' '.join(filtered_words)
    return (output)


# In[ ]:





# In[ ]:




