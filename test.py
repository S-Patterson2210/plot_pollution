import requests 
import matplotlib
import numpy


url = 'https://i.imgflip.com/5obphi.jpg'
r = requests.get(url, allow_redirects=True)

f = open ('lotr_meme.jpg', 'wb')
f.write(r.content)

f.close()

