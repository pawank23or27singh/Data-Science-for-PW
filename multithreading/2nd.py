import threading 
import urllib.request

def file_download(url,filname) :
    urllib.request.urlretrieve(url,filname)

file_download("https://en.wikipedia.org/wiki/Shreya_Ghoshal")
print(file_download)