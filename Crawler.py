#from bs4 import *
 

import requests as rq
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml


#Here in the parentheses you have to put the exact link of that website on which you want to run Image Crawler.

r2 = rq.get("https://unsplash.com/t/travel")
soup = BeautifulSoup(r2.text, "lxml")

links = []

#Inspect the website and write the image link format below linke this(https://images.unsplash.com/photo)
x = soup.select('img[src^="https://images.unsplash.com/photo"]')

for img in x:
    links.append(img['src'])

os.mkdir('Satyam_photos')
i = 1

for index, img_link in enumerate(links):
    #You can define the If condition here according the the needs of the images here. Linke I want to extract onlt 10 images
    #that's why I have defined if i <= 10:
    if i <= 10:
        img_data = rq.get(img_link).content
        with open('Satyam_photos\\' + str(index+1)+'.jpg', 'wb+') as f:
            f.write(img_data)
            i += 1
    else:
        f.close()
        break
		
##Jayant 