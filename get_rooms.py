import requests

TOKEN = "NTcyNGU5ODAtYTMxZC00YjQ5LTkxZTItNTM2NmI2NDEyZTQyOTNiMGRlOTQtN2Zj_P0A1_9f897fa5-c956-4265-b098-4452767a0486"
url = "https://webexapis.com/v1/rooms"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    rooms = response.json().get("items", [])
    for room in rooms:
        print(f"Room Name: {room['title']} | Room ID: {room['id']}")
else:
    print(f"Error: {response.status_code} - {response.text}")
