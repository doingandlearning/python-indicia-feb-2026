import requests

response = requests.post("https://httpbin.org/post", json={"name":"Kevin"})
print(response)
data = response.json()
print(data)