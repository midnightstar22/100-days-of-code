from http.client import responses
from datetime import datetime

import requests
API_ID="*****"
API_KEY="*****"
TOKEN="********"
GENDER="female"
WEIGHT_KG=45
HEIGHT_CM=160
AGE=12
USERNAME="***"
PASSWORD="*****"

exercise_endpoint="******"

sheet_endpoint="******"
exercise_text=input("Tell me which exercise you did:")

headers={
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameters={
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)


# #Basic Authentication
# sheet_response = requests.post(
#   sheet_endpoint,
#   json=sheet_inputs,
#   auth=(
#       USERNAME,
#       PASSWORD,
#   )
# )

#Bearer Token Authentication
    bearer_headers = {
 "Authorization": f"Bearer {TOKEN}"
}
    sheet_response = requests.post(
         sheet_endpoint,
         json=sheet_inputs,
         headers=bearer_headers
)