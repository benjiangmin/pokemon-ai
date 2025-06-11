import requests
import json

# Fetch basic data for one Pokémon
def fetch_pokemon_basic(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "types": [t["type"]["name"] for t in data["types"]],
            "base_stats": {
                stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]
            },
            "image_url": data["sprites"]["front_default"]
        }
    else:
        print(f"Failed to fetch Pokémon #{pokemon_id}")
        return None

# Main routine: fetch Bulbasaur (#1) and save it
if __name__ == "__main__":
    pokemon = fetch_pokemon_basic(1)
    if pokemon:
        # Ensure data directory exists
        import os
        os.makedirs("data", exist_ok=True)

        # Write to JSON file
        with open("data/pokemon_data.json", "w") as f:
            json.dump([pokemon], f, indent=2)

        print("✅ Saved data for:", pokemon["name"])
