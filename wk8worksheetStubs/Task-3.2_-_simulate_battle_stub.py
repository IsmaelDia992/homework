"""
Exercise 3.2: Simulate a Turn-Based Battle (Class-Based)

In this exercise, you will create a Pokemon class and use it to simulate battles.
This demonstrates object-oriented programming principles: encapsulation, methods, and clear responsibilities.
"""

import httpx


class Pokemon:
    """
    Represents a Pokemon with stats fetched from the PokeAPI.
    """

    def __init__(self, name):
        """
        Initialise a Pokemon by fetching its data from the API and calculating its stats.

        Args:
            name (str): The name of the Pokemon (e.g., "pikachu")
        """
        self.name = name.lower()
        # TODO: Store the Pokemon's name (lowercase) done

        # TODO: Fetch Pokemon data from PokeAPI
        # - Create the URL: f"https://pokeapi.co/api/v2/pokemon/{name.lower()}" done
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        # - Make GET request done
        response = httpx.get(url)
        if response.status_code == 200:
            data = response.json()

            hp = next(s['base_stat'] for s in data['stats'] if s['stat']['name'] == 'hp')
            attack = next(s['base_stat'] for s in data['stats'] if s['stat']['name'] == 'attack')
            defense = next(s['base_stat'] for s in data['stats'] if s['stat']['name'] == 'defense')
            speed = next(s['base_stat'] for s in data['stats'] if s['stat']['name'] == 'speed')
        
            lvl50hp = self._calculate_hp(hp)
            lvl50attack = self._calculate_stat(attack)
            lvl50defense = self._calculate_stat(defense)
            lvl50speed = self._calculate_stat(speed)
            self.stats = {
                'hp': lvl50hp,
                'attack': lvl50attack,
                'defense': lvl50defense,
                'speed': lvl50speed
            }
            self.current_hp = lvl50hp
        else:
            raise ValueError(f"Could not fetch data for Pokemon: {name}")
        # - Check response status code (raise error if not 200) done
        # - Store the JSON data done

        # TODO: Calculate and store stats

        # - Use _calculate_stat() for attack, defense, speed done
        # - Use _calculate_hp() for max HP done
        # - Store stats in a dictionary done
        # - Set current_hp = max_hp done

        

    def _calculate_stat(self, base_stat, level=50, iv=15, ev=85):
        """
        Calculate a Pokemon's stat at a given level.
        Helper method (note the underscore prefix).

        Args:
            base_stat (int): The base stat value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 15)
            ev (int): Effort value (default 85)

        Returns:
            int: The calculated stat
        """
        # TODO: Implement the stat calculation formula
        # Formula: int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)
        return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

    def _calculate_hp(self, base_stat, level=50, iv=15, ev=85):
        """
        Calculate a Pokemon's HP at a given level.
        HP uses a different formula than other stats.

        Args:
            base_stat (int): The base HP value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 15)
            ev (int): Effort value (default 85)

        Returns:
            int: The calculated HP
        """
        # TODO: Implement the HP calculation formula
        # Formula: int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)
        return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

    def attack(self, defending_pokemon):
        """
        Attack another Pokemon, dealing damage based on stats.

        Args:
            defending_pokemon (Pokemon): The Pokemon being attacked

        Returns:
            int: The amount of damage dealt
        """
        # TODO: Calculate damage using the damage formula
        # Formula: int((((2 * 50 * 0.4 + 2) * self.stats['attack'] * 60) / (defending_pokemon.stats['defense'] * 50)) + 2)
        # Where 50 is level and 60 is base_power
        damage = int((((2 * 50 * 0.4 + 2) * self.stats['attack'] * 60) / (defending_pokemon.stats['defense'] * 50)) + 2)
        # TODO: Make the defending_pokemon take damage done
        # Call defending_pokemon.take_damage(damage)done
        defending_pokemon.take_damage(damage)
        return damage
    
        # TODO: Return the damage amount done
        

    def take_damage(self, amount):
        """
        Reduce this Pokemon's HP by the damage amount.

        Args:
            amount (int): The damage to take
        """
        # TODO: Reduce current_hp by amount
        # Make sure HP doesn't go below 0 yeppers
        self.current_hp -= amount
        if self.current_hp < 0:
            self.current_hp = 0
        

    def is_fainted(self):
        """
        Check if this Pokemon has fainted (HP <= 0).

        Returns:
            bool: True if fainted, False otherwise
        """
        # TODO: Return True if current_hp <= 0, False otherwise donezo
        if self.current_hp <= 0:
            return True
        else:            
            return False
        

    def __str__(self):
        """
        String representation of the Pokemon for printing.

        Returns:
            str: A nice display of the Pokemon's name and HP
        """
        # TODO: Return a string like "Pikachu (HP: 95/120)" donearumma
        return f"{self.name.capitalize()} (HP: {self.current_hp}/{self.stats['hp']})"
        


def simulate_battle(pokemon1_name, pokemon2_name):
    """
    Simulate a turn-based battle between two Pokemon.

    Args:
        pokemon1_name (str): Name of the first Pokemon
        pokemon2_name (str): Name of the second Pokemon
    """
    # TODO: Create two Pokemon objects donedozo
    pokemon1 = Pokemon(pokemon1_name)
    pokemon2 = Pokemon(pokemon2_name)

    # TODO: Display battle start message done done done....
    print(f"A battle starts between {pokemon1.name.capitalize()} and {pokemon2.name.capitalize()}!")
    print(f"{pokemon1}: {pokemon1.current_hp} HP")
    print(f"{pokemon2}: {pokemon2.current_hp} HP")
    # Show both Pokemon names and initial HP

    # TODO: Determine who attacks first based on speed donevenask
    if pokemon1.stats['speed'] > pokemon2.stats['speed']:
        attacking_pokemon = pokemon1
        defending_pokemon = pokemon2
    else:
        attacking_pokemon = pokemon2
        defending_pokemon = pokemon1
    # The Pokemon with higher speed goes first
    # Hint: Compare pokemon1.stats['speed'] with pokemon2.stats['speed'] done flamingo

    # TODO: Battle loop
    # - Keep track of round number done is the name of the dog
    round_number = 1
    while not attacking_pokemon.is_fainted() and not defending_pokemon.is_fainted():
        print(f"\n-- Round {round_number} --")
        damage = attacking_pokemon.attack(defending_pokemon)
        print(f"{attacking_pokemon.name.capitalize()} attacks {defending_pokemon.name.capitalize()} for {damage} damage!")
        print(f"{defending_pokemon}: {defending_pokemon.current_hp} HP remaining")

        if defending_pokemon.is_fainted():
            print(f"{defending_pokemon.name.capitalize()} has fainted!")
            break

        # Swap attacking_pokemon and defending_pokemon for next turn donelij
        attacking_pokemon, defending_pokemon = defending_pokemon, attacking_pokemon
        round_number += 1
    # - While neither Pokemon is fainted:
    #   - Display round number done
    #   - attacking_pokemon attacks defending_pokemon done
    #   - Display damage and remaining HP done
    #   - Check if defending_pokemon fainted
    #   - If not, swap attacking_pokemon and defending_pokemon
    #   - Increment round number all done

    # TODO: Display battle result
    print("The Battle is Over! ")
    if attacking_pokemon.is_fainted():
        winner = defending_pokemon
    else:
        winner = attacking_pokemon
    print(f"{winner.name.capitalize()} wins the battle with {winner.current_hp} HP remaining!")
    # Show which Pokemon won and their remaining HP
    


if __name__ == "__main__":
    # Test your battle simulator
   # simulate_battle("pikachu", "bulbasaur")

    # Uncomment to test other battles:
    #simulate_battle("pidgey", "rattata")
     simulate_battle("eevee", "jigglypuff")
