from flask import Flask, request, jsonify
from pokedex import Pokedex

app = Flask(__name__)
pokedex = Pokedex("data/pokemon_data.json")

@app.route("/pokemon", methods=["GET"])
def get_pokemon():
    type_filter = request.args.get("type")
    min_speed = request.args.get("min_speed", type=int)

    results = pokedex.get_all_pokemon()

    if type_filter:
        results = pokedex.get_by_type(type_filter)

    if min_speed is not None:
        results = [p for p in results if p["base_stats"].get("speed", 0) >= min_speed]

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
