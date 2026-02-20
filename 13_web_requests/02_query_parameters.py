import requests
import json
from requests import HTTPError

try: 
  response = requests.get("https://pokeapi.co/api/v2/pokemon", 
                            params={"offset": 10, "limit": 10}, 
                            headers={"Authorization": "Bearer asdasdasd"},
                            timeout=3)
  print(response)  # <Response [200]>
  response.raise_for_status()
  data = response.json()
  print(response.url)
  with open("pokemon.json", mode="w") as file:
    file.write(json.dumps(data, indent=2))
except requests.HTTPError as e:
  print(f"Something went wrong: {e}")


  