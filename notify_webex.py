import sys
import requests

def send_message(message):
    token = "NTcyNGU5ODAtYTMxZC00YjQ5LTkxZTItNTM2NmI2NDEyZTQyOTNiMGRlOTQtN2Zj_P0A1_9f897fa5-c956-4265-b098-4452767a0486"
    room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNTZiNWZlZTAtZGU2Zi0xMWYxLWFkOGYtODVkNmNiYTYxZmVi"
    url = "https://webexapis.com/v1/messages"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "roomId": room_id,
        "text": message
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print("Webex notification sent successfully.")
    else:
        print(f"Failed: {response.status_code} - {response.text}")

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "Jenkins Build Update"
    send_message(msg)
