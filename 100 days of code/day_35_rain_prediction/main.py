from http.client import responses

import requests
from pyexpat.errors import messages
from twilio.rest import Client

OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key=
account_sid=
auth_token=
weather_params={
    "lat": 12.914142,
    "lon":74.855957,
    "appid":api_key,
    "cnt":4,
}

response=requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()

weather_data=response.json()
will_rain=False
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True
if will_rain:
        client=Client(account_sid,auth_token)
        message=client.messages\
        .create(
            body="its going to rain today.Remenber to bring an umbrella",
            from_='+19786254472',
            to='+919947613366'
            )
print(message.status)

