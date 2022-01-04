#!/usr/bin/python
import requests
import urllib

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00451/'


download = requests.get(url)


urllib.urlretrieve(url, 'dataR2.csv')
