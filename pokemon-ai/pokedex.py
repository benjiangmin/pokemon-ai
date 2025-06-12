import json

class Pokedex:
    def __init__(self, json_file_path):
        with open(json_file_path, "r") as f:
            self.pokemon_list = json.load(f)

    def get_all_pokemon(self):
        return self.pokemon_list

    def get_by_type(self, type_name):
        return [p for p in self.pokemon_list if type_name.lower() in (t.lower() for t in p["types"])]

    def get_by_stat(self, stat_name, min_value):
        return [p for p in self.pokemon_list if p["base_stats"].get(stat_name, 0) >= min_value]

    def get_by_name(self, name):
        return [p for p in self.pokemon_list if p["name"].lower() == name.lower()]

# Example usage
if __name__ == "__main__":
    pokedex = Pokedex("data/pokemon_data.json")

    print(f"Total Pokémon loaded: {len(pokedex.get_all_pokemon())}")

    fire_pokemon = pokedex.get_by_type("fire")
    print(f"Fire-type Pokémon count: {len(fire_pokemon)}")

    fast_pokemon = pokedex.get_by_stat("speed", 100)
    print(f"Pokémon with speed >= 100: {len(fast_pokemon)}")
