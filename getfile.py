import urllib.request,os

def get(url,path,savename):
    if os.path.exists(path) == False:
        os.mkdir(path)
    urllib.request.urlretrieve(url,path+savename)
    return("ok")