#-*- encoding:UTF-8 -*-
import os
import urllib


# download file from url to path
def download(url, path):
    urllib.urlretrieve(url, path)

