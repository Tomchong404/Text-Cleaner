#!/usr/bin/env python
# coding: utf-8

# ## Remove line break

# In[37]:


text= input("Enter your sentence:") 


# In[38]:


clean_text = text.replace('\n', '') 
print(clean_text)


# ## Turn paragraph to point form

# In[5]:


text= input("Enter your sentence:") 


# In[6]:


import re

points = re.split(r'\.\s*', text)

for point in points:
    print("•" + point.strip())


# ## Compare and track changes

# In[53]:


old_text= input("Enter your sentence:") 


# In[55]:


new_text= input("Enter your new sentence:") 


# In[56]:


import difflib
from IPython.display import HTML

def compare_text(old_text, new_text):
    # Compare and generate the differences between the two text
    differ = difflib.Differ()
    diff = differ.compare(old_text.split(), new_text.split())
    changes = []
    # Highlight the changes through sepcified color
    for line in diff:
        if line.startswith('- '):
            # Cross through and red for removed
            changes.append('<del style="color:red">' + line[2:] + '</del>')
            # Green and underscore for new added
        elif line.startswith('+ '):
            changes.append('<ins style="color:green">' + line[2:] + '</ins>')
        else:
            changes.append(line)
    return ' '.join(changes)

# Display the changes
changes = compare_text(old_text, new_text)
HTML(changes)


# ## Text extract

# In[1]:


text= input("Enter your sentence:") 


# In[2]:


start_condition= input("Enter your sentence:") 


# In[3]:


end_condition = input("Enter your sentence:") 


# In[4]:


import re

def extract_words_between(text, start_condition, end_condition):
    pattern = re.compile(f"{start_condition}(.*?){end_condition}")
    # Use findall to get all matches
    matches = pattern.findall(text)
    
    # Extract words from matches
    words = []
    for match in matches:
        # Split the match into words and add them to the list
        words.extend(match.split())
    # Join the words into a single string
    extracted_sentence = ' '.join(words)
    return extracted_sentence

# Example usage
extracted_sentence = extract_words_between(text, start_condition, end_condition)
print(extracted_sentence)

