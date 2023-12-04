# import requests
# url = "http://pudim.com.br/"
#
# try:
#     if requests.get(url).status_code == 200:
#         print('Servidor está disponível')
#     else:
#         print('Servidor está indisponível')


import urllib
import urllib.request

try:
    url = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('Servidor está indisponível')
else:
    print('Servidor está disponível')
    print(url.read())


