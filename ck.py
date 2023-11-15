import os
try:
  muhib = open('/cntrl/requests/models.py','r').read()
  lipi = len(muhib);print(lipi)
except:
  exit('no')

from cntrl import requests
a = requests.get('https://github.com/JISAN-404/DARK_SERVER/blob/main/file/mtd.txt').text
print(a)
