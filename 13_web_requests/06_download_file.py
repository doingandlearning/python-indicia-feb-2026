import requests

response = requests.get("https://cdn.wsform.com/wp-content/uploads/2020/06/industry.csv")
data = response.content

with open("industry.csv", mode="wb") as file:  # wb if you are working with non-text
  file.write(data)