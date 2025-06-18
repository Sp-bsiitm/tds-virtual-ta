import requests

url = "https://e771-4-240-39-196.ngrok-free.app/ask"
data = {
    "question": "What is the course schedule?"  # or whatever key your code expects
}
response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
