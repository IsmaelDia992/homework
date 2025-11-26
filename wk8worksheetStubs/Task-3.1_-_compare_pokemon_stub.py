"""
Exercise 3.1: Fetch and Compare Pokémon Stats (Stub)
- Fetch data for two Pokémon from the PokéAPI.
- Calculate their stats at level 50.
- Compare their base stats (e.g., attack, defense, speed).
"""

import httpx

def calculate_stat(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's stat at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

def calculate_hp(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's HP at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

def compare_pokemon(pokemon1, pokemon2):
    """Compare the calculated stats of two Pokémon."""

    url1 = f"https://pokeapi.co/api/v2/pokemon/{pokemon1}"
    response = httpx.get(url1)
    if response.status_code == 200:
        data1 = response.json()

        # Extract base stats from the stats array
        pokemon1hp = next(s['base_stat'] for s in data1['stats'] if s['stat']['name'] == 'hp')
        pokemon1attack = next(s['base_stat'] for s in data1['stats'] if s['stat']['name'] == 'attack')
        pokemon1defense = next(s['base_stat'] for s in data1['stats'] if s['stat']['name'] == 'defense')
        pokemon1speed = next(s['base_stat'] for s in data1['stats'] if s['stat']['name'] == 'speed')
        
        pokemon1lvl50hp = calculate_hp(pokemon1hp)
        pokemon1lvl50attack = calculate_stat(pokemon1attack)
        pokemon1lvl50defense = calculate_stat(pokemon1defense)
        pokemon1lvl50speed = calculate_stat(pokemon1speed)


    url2 = f"https://pokeapi.co/api/v2/pokemon/{pokemon2}"
    response = httpx.get(url2)
    if response.status_code == 200:
        data2 = response.json()

        # Extract base stats from the stats array
        pokemon2hp = next(s['base_stat'] for s in data2['stats'] if s['stat']['name'] == 'hp')
        pokemon2attack = next(s['base_stat'] for s in data2['stats'] if s['stat']['name'] == 'attack')
        pokemon2defense = next(s['base_stat'] for s in data2['stats'] if s['stat']['name'] == 'defense')
        pokemon2speed = next(s['base_stat'] for s in data2['stats'] if s['stat']['name'] == 'speed')
        
        pokemon2lvl50hp = calculate_hp(pokemon2hp)
        pokemon2lvl50attack = calculate_stat(pokemon2attack)
        pokemon2lvl50defense = calculate_stat(pokemon2defense)
        pokemon2lvl50speed = calculate_stat(pokemon2speed)
    # TODO: Compare the calculated stats and print the results

    print(f"{pokemon1} has an hp stat of {pokemon1lvl50hp}, whilst {pokemon2} has an hp stat of {pokemon2lvl50hp}")
    print(f"{pokemon1} has an attack stat of {pokemon1lvl50attack}, whilst {pokemon2} has an attack stat of {pokemon2lvl50attack}")
    print(f"{pokemon1} has a defense stat of {pokemon1lvl50defense}, whilst {pokemon2} has a defense stat of {pokemon2lvl50defense}")
    print(f"{pokemon1} has a speed stat of {pokemon1lvl50speed}, whilst {pokemon2} has a speed stat of {pokemon2lvl50speed}")
# Example usage
if __name__ == "__main__":
    compare_pokemon("pikachu", "bulbasaur")

"""
Hints:
- Use httpx.get(url) to fetch data for each Pokémon.
- Access base stats using data['stats'] and extract base_stat values.
- Use calculate_stat and calculate_hp to compute level 50 stats.
"""
