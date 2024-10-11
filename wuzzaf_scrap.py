import requests
from  bs4 import BeautifulSoup


response =  requests.get('https://wuzzuf.net/search/jobs/?a=hpb&q=machine%20learning%20&start=0')
page = BeautifulSoup(response.content ,'html.parser')

title =  page.find_all('h2', {'class':'css-m604qf'})
title = [ i.text for i in title ]

link = page.find_all('h2', {'class':'css-m604qf'})
link = [i.a['href'] for i in link ]

ocupation = page.find_all('div', {'class':'css-1lh32fc'})
ocupation = [i.text for i in ocupation ]

company =  page.find_all('div', {'class':'css-d7j1kk'})
company = [i.a.text for i in company ]

specs =  page.find_all('div', {'class':'css-y4udm8'})
specs = [i.text for i in specs ]

data =  {}

data['title'] = title
data['link'] = link
data['ocupation'] = ocupation
data['company'] = company
data['specs'] = specs

import pandas as pd

final = pd.DataFrame(data)
print(final.head())