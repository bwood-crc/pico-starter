import requests

response = requests.get("http://localhost:5000/api/v1/books")

print(response)
print(response.text)
print(response.json())

for x in response.json():
    print(x)
