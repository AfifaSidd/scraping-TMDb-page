#!/usr/bin/env python
# coding: utf-8

# #  Scraping Top Movie Details from the TMDb

# ##### 1) We will scrape the website - TMDb movies
# 
# ##### 2) Scraping/Fetching the TOP 20 Movies 
# 
# ##### 3) List of movie details we will get in this:-  {movie title,movie page url, movie release date}
# 
# ##### 4) We are also Going to fetch the images of the movies and will save it into one folder

# In[ ]:





# # Rough Code

# In[ ]:





# ### Using the request library to download the webpage

# In[1]:


import requests


# In[2]:


# Paste the website url


# In[3]:


website_url= 'https://www.themoviedb.org/movie'


# In[4]:


# Use Request Library


# In[5]:


response = requests.get(website_url)


# In[6]:


# Use status_code to check whether url is fetched or not


# In[7]:


response.status_code


# In[8]:


# Length of the website


# In[9]:


len(response.text)


# In[10]:


# Getting the text out of the website content


# In[11]:


page_contents = response.text


# In[12]:


# Displaying the text of the website


# In[13]:


page_contents[0:1000]


# In[14]:


# Opening the file to store the page_contents


# In[15]:


file = open('webpage.html', encoding="utf8")


# In[16]:


with open('webpage.html', 'w', encoding="utf8") as f:
    f.write(page_contents)


# In[ ]:





# ### Use Beautiful Soup to parse and extract information

# In[17]:


from bs4 import BeautifulSoup


# In[18]:


doc = BeautifulSoup(page_contents, 'html.parser')


# In[19]:


# Fetching/Scraping h2 tags from website 


# In[20]:


movie_title_tags = doc.find_all('h2')


# In[21]:


# Length of the h2 tags


# In[22]:


len(movie_title_tags)


# In[23]:


# Displaying the movie_title_tags where it contains the movie name


# In[24]:


movie_title_tags[4:24]


# In[25]:


# Scraping release date of the movie from the website 


# In[26]:


release_date_tags = doc.find_all('p')


# In[27]:


# Displaying the tags 


# In[28]:


release_date_tags[1:21]


# In[29]:


# Scraping the Url from the website


# In[30]:


url = doc.find_all('a', {'class':'image'})


# In[31]:


# Displaying the url tag


# In[32]:


url


# In[33]:


# Length of the url


# In[34]:


len(url)


# In[35]:


# Complete Url of one movie 


# In[36]:


movie_pg_url_tags = "https://www.themoviedb.org" + url[0]['href']
print(movie_pg_url_tags)


# In[37]:


# Displaying all the Movie Titles in order


# In[38]:


movie_titles= []

for tag in movie_title_tags[4:24]:
    movie_titles.append(tag.text)

movie_titles


# In[39]:


# Displaying all the Movie Titles in order


# In[40]:


movie_titles


# In[41]:


# Length of movie Titles


# In[42]:


len(movie_titles)


# In[43]:


# Displaying all the Release Date of Movies in order


# In[44]:


release_dates= []

for tag in release_date_tags[1:21]:
    release_dates.append(tag.text.strip())
    
release_dates


# In[45]:


# Length of release_date


# In[46]:


len(release_dates)


# In[47]:


# Displaying all the Movie urls in order


# In[48]:


movie_urls= []
base_url = 'https://www.themoviedb.org'

for tag in url:
    movie_urls.append(base_url + tag['href'])

movie_urls


# In[ ]:





# In[49]:


# importing pandas 


# In[50]:


import pandas as pd


# In[51]:


# Making the Dictionary


# In[52]:


movie_pg_dict= {
    'title': movie_titles,
    'Release Dates': release_dates,
    'Url': movie_urls
}


# In[53]:


# Adding the dict into dataframe


# In[54]:


movie_pg = pd.DataFrame(movie_pg_dict)


# In[55]:


# Displaying the DataFrame


# In[56]:


movie_pg


# In[57]:


# Saving the DataFrame into csv file


# In[58]:


movie_pg.to_csv('movies_list', index = None)


# In[ ]:





# ## Loading the Images

# In[59]:


# Scraping the image from the website


# In[60]:


images_tags = doc.find_all('img',{'class': 'poster'})


# In[61]:


# Displaying the tags


# In[62]:


images_tags


# In[63]:


# Getting the scource from the image tag


# In[64]:


imageSources = []
 
for image in images_tags:
    imageSources.append(image.get('src'))

imageSources


# In[65]:


# Getting the Image Url


# In[66]:


image_urls= []
base_url = 'https://www.themoviedb.org'

for img in images_tags:
    image_urls.append(base_url + img['src'])

image_urls


# In[67]:


# Importing other required files


# In[68]:


import random

import string

import urllib.request

import os


# In[69]:


# Forming the Url of the file image (optional)


# In[70]:


for image in image_urls:
    images = ''.join(random.choices(string.ascii_lowercase+string.digits, k = 8))
    beta = 'movie_img/'+images+'.jpg'
    print(beta)
    


# In[71]:


# Making the Folder
os.makedirs('movie_img', exist_ok=True)

for image in image_urls:
    # Getting the url of file image
    images = ''.join(random.choices(string.ascii_lowercase+string.digits, k = 8))
    # Downloading the images
    alpha=urllib.request.urlretrieve (image, 'movie_img/'+images+'.jpg')


# In[72]:


# Forming the DataFrame of all the image url


# In[73]:


path = pd.DataFrame(image_urls)


# In[74]:


path


# In[ ]:





# # Final Code

# In[ ]:





# In[75]:


import requests

import pandas as pd

import random

import string

import urllib.request

import os


# In[76]:


def get_movie_title(doc):
    movie_title_tags = doc.find_all('h2')
    movie_titles= []
    for tag in movie_title_tags[4:24]:
        movie_titles.append(tag.text)
    return movie_titles
    
def get_release_dates(doc):
    release_date_tags = doc.find_all('p')
    release_dates= []
    for tag in release_date_tags[1:21]:
        release_dates.append(tag.text.strip())
    return release_dates
        
    
def get_movie_url(doc):
    url = doc.find_all('a', {'class':'image'})
    movie_urls= []
    base_url = 'https://www.themoviedb.org'
    for tag in url:
        movie_urls.append(base_url + tag['href'])
    return movie_urls


def get_movie_details():
    website_url= 'https://www.themoviedb.org/movie'
    response = requests.get(website_url)
    if response.status_code != 200:
        raise Exception('Failed to load page{}'.format(website_url))
    doc = BeautifulSoup(page_contents, 'html.parser')
    movie_pg_dict= {
    'title': movie_titles,
    'Release Dates': release_dates,
    'Url': movie_urls
    }
    return pd.DataFrame(movie_pg_dict)


# In[77]:


get_movie_details()


# In[78]:


import random

import string

import urllib.request

import os

def get_images_src(doc):
    images_tags = doc.find_all('img',{'class': 'poster'})
    imageSources = []
    for image in images_tags:
        imageSources.append(image.get('src'))
    return imageSources

def get_img_url(doc):
    image_urls= []
    base_url = 'https://www.themoviedb.org'
    for img in images_tags:
        image_urls.append(base_url + img['src'])
    return image_urls

def scrape_img():
    print("Image getting loaded.....................................................................!!!!!!!!!!!!!!!!")
    os.makedirs('movie_img', exist_ok=True)
    for image in image_urls:
        images = ''.join(random.choices(string.ascii_lowercase+string.digits, k = 8))
        alpha=urllib.request.urlretrieve (image, 'movie_img/'+images+'.jpg')
    print("\n")
    print("-------------Image loaded!!!!--------------")


# In[79]:


scrape_img()


# In[ ]:




