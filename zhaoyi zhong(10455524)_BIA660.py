# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:12:12 2020

@author: Zzysq
"""

import pandas as pd
import requests
import re

url = 'https://en.m.wikipedia.org/wiki/List_of_Internet_top-level_domains'

response = requests.get(url)

html = response.content
body = html.decode('utf-8')

rule = re.compile(r'>(\.\S+)</')
top_domains = rule.findall(body)

top_domains = list(set(top_domains))
print(top_domains)


for i, domain in enumerate(top_domains):
    if '</a>' in domain:
        top_domains[i] = top_domains[i].replace('</a>', '')
print(top_domains)

res = []
for domain in top_domains:
    url = 'http://www.example' + domain
    try:
        response = requests.get(url)
        res.append(True)
    except Exception as e:
        res.append(e)
        
output = pd.DataFrame()
output['domain'] = top_domains
output['availability'] = res
output.to_csv('result.csv')
