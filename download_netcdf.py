import requests 
import matplotlib
import numpy

def download_netcdf(url, save_file):
    
    r = requests.get(url, allow_redirects=True)

    f = open (save_file, 'wb')
    f.write(r.content)

    f.close()

download_netcdf ('https://i.imgflip.com/5obphi.jpg', 'lotr_meme')

