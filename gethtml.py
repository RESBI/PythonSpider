import urllib.request,ssl

ssl._create_default_https_context = ssl._create_unverified_context

def get(url):
    header = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent' : header}
    data = urllib.request.Request(url = url,headers = headers)
    page = urllib.request.urlopen(data)
    result = page.read()
    return(result)