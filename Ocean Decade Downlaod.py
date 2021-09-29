from download_netcdf import download_netcdf
import requests

def download_video (url, save_file):
    r = requests.get (url, allow_redirects=True)

    f = open  (save_file, 'wb')
    f.write(r.content)

    f.close()

download_video('https://www.facebook.com/messenger_media?thread_id=100002231179035&attachment_id=594923048306064&message_id=mid.%24cAAAAAPF7icqCYoOMkF8MT2u24_vi', 'ocean_decade_video')

