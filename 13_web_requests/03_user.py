import requests
import json
from requests import HTTPError
from pathlib import Path

def get_and_save_pokemon_details(pokemon):
  try: 
    file_path = Path(f"{pokemon}.json")

    if file_path.exists():
      with open(file_path) as file:
        return json.load(file)
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    print(response)  # <Response [200]>
    response.raise_for_status()
    data = response.json()

    with open(f"{pokemon}.json", mode="w") as file:
      file.write(json.dumps(data, indent=2))
    return data
  except requests.HTTPError as e:
    print(f"Something went wrong: {e}")


pokemon_name = input("What pokemon do you want information about? ")
data = get_and_save_pokemon_details(pokemon_name)
print(data)