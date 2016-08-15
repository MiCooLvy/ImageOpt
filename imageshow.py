import requests
from bs4 import BeautifulSoup

# http://jandan.net/ooxx/page-1969#comments

url = 'http://jandan.net/ooxx/page-'

for page in range(1950, 1971):
    res = requests.get(url + str(page) + '#comments')
    html = BeautifulSoup(res.text, "html.parser")
    for index, each in enumerate(html.select('img')):
        with open('{}.jpg'.format(str(page) + '-' + str(index)), 'wb') as jpg:
            jpg.write(requests.get(each.attrs['src'], stream=True).content)
