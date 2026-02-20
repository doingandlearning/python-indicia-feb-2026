import requests
import json
from requests import HTTPError

try: 
  response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
  print(response)  # <Response [200]>
  response.raise_for_status()
  data = response.json()

  with open("ditto.json", mode="w") as file:
    file.write(json.dumps(data, indent=2))
except requests.HTTPError as e:
  print(f"Something went wrong: {e}")


  