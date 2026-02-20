import requests
import json
from requests import HTTPError

try: 
  response = requests.get("https://pokeapi.co/api/v2/pokemon", 
                            params={"offset": 10, "limit": 50}, 
                          )
  response.raise_for_status()
  data = response.json()
  results = data.get("results", [])
  for result in results:
    response = requests.get(result.get("url"))
    data = response.json()
    with open(f"{result.get("name")}.json", mode="w") as file:
      file.write(json.dumps(data, indent=2))
except requests.HTTPError as e:
  print(f"Something went wrong: {e}")


  