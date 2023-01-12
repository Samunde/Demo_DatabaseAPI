# import base64
# import requests
from clientid_and_secret import *
# import json

# auth_url="https://accounts.spotify.com/api/token"
# auth_header={}
# auth_data={}

# message = f"{client_id}:{client_secret}"
# message_bytes = message.encode("ascii")
# print(message_bytes)
  
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode("ascii")
  
# print(base64_message)
# auth_header['Authorization'] ="Basic" + base64_message
# # print(auth_header)
# auth_data['grant_type']="client_credentials"

# res=requests.post(auth_url,headers=auth_header,data=auth_data)
# print(res)
# response_obj=res.json()

# print(json.dumps(response_obj,indent=4))
# # print(res)

import requests
import json
import base64
from pprint import pp

client = f"{client_id}:{client_secret}"
client_b64= base64.b64encode(client.encode())
headers = {
        "Authorization": f"Basic {client_b64.decode()}"
  
    }
    
data = {
        'grant_type': 'client_credentials'
    }
    
response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
# print(response.status_code)
pp(response.json())
