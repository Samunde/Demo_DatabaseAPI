import requests
import pandas as pa 
from pprint import pp
baseurl="https://rickandmortyapi.com/api/"
endpoint='character'
def main_request(baseurl, endpoint,x):
    r=requests.get(baseurl+endpoint+f'?page={x}')
    return r.json()
def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    
    charlist=[]
    for item in response['results']:
        char={
            'name':item['name'],
            'no_ep':len(item['episode'])
        }
        charlist.append(char)
    return charlist
mainlist=[]
data=main_request(baseurl,endpoint,1)
pp(data)
# for x in range(1,get_pages(data)+1):
#     print(x)

# data=r.json()
# print(data['info']['pages'])
# print(data['results'][0]['name'])
# episodes=data['results'][0]['episode']
# print(len(episodes))