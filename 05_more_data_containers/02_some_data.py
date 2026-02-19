# () tuple
# [] list
# {} dict

ditto_data = {
  "abilities": [
    {
      "ability": {
        "name": "limber",
        "url": "https://pokeapi.co/api/v2/ability/7/"
      },
      "is_hidden": False,
      "slot": 1
    },
    {
      "ability": {
        "name": "imposter",
        "url": "https://pokeapi.co/api/v2/ability/150/"
      },
      "is_hidden": True,
      "slot": 3
    }
  ]
}
print(ditto_data.get("abilities", [])[1].get("ability", {}).get("name", "Unknown ability"))