import urllib

def download(url):
    name = "name.jpg"
    urllib.urlretrieve(url,name)


download('Give here Url of image')