import requests
import json
from pprint import pp


baseurl="https://rickandmortyapi.com/api/character" # Getting the URL for API data
page=1
pages ='?page={}'

reponse=requests.get(baseurl+pages)
data=reponse.json()
# pp(data)
total_pages=data['info']['pages'] #Assigning Total number of pages into the variable
mylist=[]
for page_no in range(page,total_pages+1): #Accessing Each page 
    
    reponse=requests.get(baseurl+pages.format(page_no))
    result=reponse.json()

    for item in result['results']:  # Getting the specific key in each page with the 
                                            #following condition
        if item['status']=='Alive' and '2021' in item['created']: 
            result_data={}
            result_data['Id']=item['id']
            result_data['Loaction_Name']=item['location']['name']
            mylist.append(result_data)

result={i:j for i,j in enumerate(mylist,1)} #Using Dict comprehension for getting dict's inside dict's
print(result)
    
with open('Retrive_data_by_Year.json','w')as file:  #Writing result to the json file
    json.dump(result,file,indent=4)
    
    