from http.client import responses
from datetime import datetime
import requests
from requests import delete

USERNAME= "nakshatra"
TOKEN="skdjkcndnjnfjjfkk"
GRAPH_ID="graph10"
pixela_endpoint="https://pixe.la/v1/users"

user_params={
    "token": "skdjkcndnjnfjjfkk",
    "username": "nakshatra",
    "agreeTermsOfService": "yes",
    "notMinor" : "yes",

}

# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":"graph10",
    "name":"Cycling graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":TOKEN
}
today=datetime.now()
# print(today.strftime("%Y%m%d"))
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many kilometers did u cycle today "),

}
response=requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

new_pixel_data={
    "quantity":"4.5"
}
# response=requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
# response=requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)