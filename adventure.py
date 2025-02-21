'''Runsthrough a adventure situation through the use of functions'''
import random

#Prints health
def display_player_status(player_health):
    # ... function code ...
    "Prints health using parameter player_health (int)"
    print(f"Your current health: {player_health}.")

#Handles left and right situations
def handle_path_choice(player_health):
    """Parameter: player_health (int)"""
    # ... function code ...
    updated_player_health = player_health
    choice = random.choice(["left", "right"])
    if choice == "left":
        updated_player_health += 10
        print("You encounter a friendly gnome who heals you for 10 health points.")
        updated_player_health = min(updated_player_health, 100)
    elif choice == "right":
        updated_player_health -= 15
        print("You fall into a pit and lose 15 health points.")
        if updated_player_health < 0:
            updated_player_health = 0
            print("You are barely alive!")
    return updated_player_health

#Simulates player attack
def player_attack(monster_health, attack):
    "Evaluates monster health after a player attack"
    # ... function code ...
    updated_monster_health = monster_health
    print("You strike the monster for 15 damage!")
    updated_monster_health -= attack
    return updated_monster_health

#Simulates monster attack
def monster_attack(player_health):
    "Evaluates player health after a monster attack"
    # ... function code ...
    updated_player_health = player_health
    critical = random.random()
    if critical < 0.5:
        updated_player_health -= 20
        print("The monster lands a critical hit for 20 damage!")
    elif critical >= 0.5:
        updated_player_health -= 10
        print("The monster hits you for 10 damage!")
    return updated_player_health

#Simulates encounter
def combat_encounter(player, monster_health, has_treasure):
    "Simulates encounter depending on player health, monster health, and loot"
    # ... function code ...
    updated_player_health = player["player_health"]
    updated_monster_health = monster_health
    treasure_found_and_won = False
    while (updated_player_health > 0 and updated_monster_health > 0):
        updated_monster_health = player_attack(updated_monster_health, player["attack"])
        display_player_status(updated_player_health)
        if updated_monster_health > 0:
            updated_player_health = monster_attack(updated_player_health)
    if updated_player_health <= 0:
        print("Game Over!")
    elif updated_monster_health <= 0:
        print("You defeated the monster!")
        treasure_found_and_won = has_treasure
    return treasure_found_and_won # boolean

#Prints depending if monster had treasure
def check_for_treasure(has_treasure):
    "Print depends on treasure value"
    # ... function code ...
    if has_treasure:
        print("You found the hidden treasure! You win!")
    else:
        print("The monster did not have the treasure. You continue your journey.")

def acquire_item(inventory, item):
    """Acquires item"""
    if item not in inventory: # Checks for duplicates
        inventory.append(item) #  - append(): Used in acquire_item to add an item
        print(f'You found a {item} in the room.')
        print(f'You acquired a {item}!')
    elif item in inventory:
        print("You already have the item.")
    return inventory

def display_inventory(inventory):
    """Shows inventory"""
    if not inventory:  # If the inventory is empty
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for i, item in enumerate(inventory, start=1):  # enumerate() to print items with numbers
            print(f"{i}. {item}")


def enter_dungeon(player_health, inventory, dungeon_rooms, clues):
    "Enters dungeon and runs through scenario"
    for room in dungeon_rooms:
        room_description, item, challenge_type, challenge_outcome = room
        print(room_description)
        try:
            room[1] = "Bathroom"
        except TypeError:
            print("Cannot modify a tuple")
        if item is not None:
            acquire_item(inventory, item)
        else:
            print("There was nothing in the room.")
        if challenge_type == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")
        elif challenge_type == "puzzle":
            print("You encounter a puzzle!")
            choice = input("Do you want to solve or skip the puzzle?").strip().lower()
            if choice == "solve":
                success = random.choice([True, False])
                if success:
                    print(challenge_outcome[0])  # Success message
                    player_health += challenge_outcome[2]  # Health change
                else:
                    print(challenge_outcome[1])  # Failure message
                    player_health += challenge_outcome[2]  # Health change
                if player_health <= 0:
                    print("You are barely alive!")
                    player_health = 0
        elif challenge_type == "trap":
            print("You see a potential trap!")
            choice = input("Do you want to disarm or bypass the trap?: ").strip().lower()
            if choice == "disarm":
                success = random.choice([True, False])
                if success:
                    if "iron sword" in inventory:
                        print(challenge_outcome[0])
                        player_health += challenge_outcome[2]
                        inventory.remove("iron sword") # Uses remove to remove item used to disarm
                else:
                    print(challenge_outcome[1])  # Failure message
                    player_health += challenge_outcome[2]  # Health change
                if player_health <= 0:
                    print("You are barely alive!")
                    player_health = 0
            elif choice == "bypass":
                success = random.random() < 0.75
                if "staff_of_wisodom" in inventory:
                    print("You used your knowledge to avoid the puzzle.")
                elif success:
                    print("You successfully manuevered around the trap.")
                    player_health -= 5
                else:
                    print("You tripped while trying to bypass the trap.")
                    player_health -= 15
                if player_health <= 0:
                    print("You are barely alive!")
                    player_health = 0
        elif challenge_type == "library":
            print(room_description[4])
            clues_list =  ["The treasure is hidden where the dragon sleeps.",
                      "The key lies with the gnome.", "Beware the shadows.",
                      "The amulet unlocks the final door."]
            find_clue(clues, random.sample(2,clues_list))
            if "staff_of_wisdom" in inventory:
                print("You understand the meaning of the clues. You bypass a puzzle challenge.")
    display_inventory(inventory)  # Show inventory after each room
    print(f"Your final health is {player_health}.")
    return player_health, inventory, clues

def discover_artifact(player_stats, artifacts, artifact_name):
    "Prints artifacts and effects"
    if artifacts[artifact_name]:
        print(artifacts[artifact_name].get("description"))
        print(artifacts[artifact_name].get("effect"))
        if artifacts[artifact_name].get("description") == "increases health":
            player_stats["player_health"] += artifacts["artifact_name"].get("power")
        elif artifacts[artifact_name].get("description") == "enhances attack":
            player_stats["player_attack"] += artifacts["artifact_name"].get("power")
    else:
        print("You found nothing of interest.")

def find_clue(clues, new_clue):
    "finds a clue"
    if new_clue not in  clues:
        clues.add(new_clue)
        print(f"You discovered a new clue: {new_clue}")
    else:
        print("You already know this clue.")
    return clues

def main():
    """main"""
    artifacts = {
        "amulet_of_vitality": {
            "description": "A glowing amulet that enhances your life force.",
            "power": 15,
            "effect": "increases health"
        },
        "ring_of_strength": {
            "description": "A powerful ring that boosts your attack damage.",
            "power": 10,
            "effect": "enhances attack"
        },
        "staff_of_wisdom": {
            "description": "A staff imbued with ancient wisdom.",
            "power": 5,
            "effect": "solves puzzles"
        }
    }
    clues = {}
    player = {"player_health": 100, "player_attack": 5,
        "monster_health": 70, 
        "has_treasure": False}

    player["has_treasure"] = random.choice([True, False]) # Randomly assign treasure

    player["player_health"] = handle_path_choice(player["player_health"])

    treasure_obtained_in_combat = combat_encounter(player["player_health"],
                                player["monster_health"], player["has_treasure"])
    artifact = random.choice([True, False])
    if artifact:
        i = random.choice([0, 1, 2])
        discover_artifact(player, artifacts, random.sample(1, artifacts[i]))
        print(f"Player Health and Attack: {player["player_health"]}, {player["player_attack"]}")

    check_for_treasure(treasure_obtained_in_combat) # Or has_treasure, depending on logic

    inventory = []  # Empty inventory at the start
    inventory = ["old map"] + ["iron sword"] #Uses concatination to give starting items

    # Example dungeon rooms
    dungeon_rooms = [
        ("A dusty old library", "key", "puzzle",
         ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
        ("A narrow passage with a creaky floor",
         None, "trap", ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
        ("A grand hall with a shimmering pool", "healing potion", "none", None),
        ("A small room with a locked chest", "treasure",
         "puzzle", ("You cracked the code!", "The chest remains stubbornly locked.", -5),
         ("A vast library filled with ancient, cryptic texts.", None, "library", None))
    ]
    # Start the dungeon exploration
    player["player_health"], inventory, clues = enter_dungeon(
        player["player_health"], inventory, dungeon_rooms, clues)
    if player["player_health"] > 0:
        print(f"You survived the dungeon with {player["player_health"]} health.")
    else:
        print("You perished.")

if __name__ == "__main__":
    main()
