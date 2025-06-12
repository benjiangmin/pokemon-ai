import requests
import json
import os

def fetch_pokemon_basic(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "id": pokemon_id,
            "name": data["name"],
            "types": [t["type"]["name"] for t in data["types"]],
            "base_stats": {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]},
            "image_url": data["sprites"]["front_default"]
        }
    else:
        print(f"Failed to fetch Pokémon #{pokemon_id}")
        return None

if __name__ == "__main__":
    all_pokemon = []
    os.makedirs("data", exist_ok=True)

    for poke_id in range(1, 152):  # Fetch Pokémon #1 to #151 (Gen 1)
        pokemon = fetch_pokemon_basic(poke_id)
        if pokemon:
            all_pokemon.append(pokemon)

    with open("data/pokemon_data.json", "w") as f:
        json.dump(all_pokemon, f, indent=2)

    print(f"✅ Saved data for {len(all_pokemon)} Pokémon!")
