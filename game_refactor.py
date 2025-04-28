import json
import os


SAVE_GAME = "savegame.json"

class Player:
    def __init__(self, start_room_id, initial_inventory=None, initial_stats=None):
        print("DEBUG: Creating a new player object!")
        self.current_room_id = start_room_id

        if initial_inventory is None:
            self.inventory = []
        else: 
            self.inventory = list(initial_inventory)
        
        if initial_stats is None:
            self.stats= {
                "score": 0,
                "has_flipped": False,
                "flashlight": 100,
                "found_key": False
            }
        else:
            self.stats = dict(initial_stats)

    def show_inventory(self):
        print("\nYou are carrying:")
        if not self.inventory:
            print("- Nothing")
        else:
            for item in self.inventory:
                print(f" - {item}")

    def move_to(self, new_room_id):
        print(f"DEBUG, Moving player to {new_room_id}")
        self.current_room_id = new_room_id

    def add_item(self, item):
        self.inventory.append(item)
        print(f"DEBUG: added {item} to the inventory")

    def remove_item(self, item):
        print(f"DEBUG: BEGINNING REMOVAL PROCESS")
        if item not in self.inventory:
            print(f"{item} not found in inventory")
            return False
        else:
            self.inventory.remove(item)
            print(f"DEBUG: item {item} successfully removed")
            return True











def handle_save(room_id, player_inv, player_stats_dict):
    game_state = {
        "current_room_id": room_id,
        "inventory": player_inv,
        "player_stats": player_stats_dict
    }

    try:   
        with open(SAVE_GAME, "w") as save_file:
            json.dump(game_state, save_file, indent=4)
        print("game saved successfully!")
    except IOError as e:
        print(f"--Error saving game: {e} ---")
    except Exception as e:
        print(f"--- An unexpected error occured during save: {e} ---")

def handle_load():
    if not os.path.exists(SAVE_GAME):
        print("---No save file found. starting a new game. ----")
        return None
    try:
        with open(SAVE_GAME, "r") as save_file:
            loaded_state = json.load(save_file)

            if "current_room_id" in loaded_state and "inventory" in loaded_state and "player_stats" in loaded_state:
                return loaded_state
            else:
                print("---Error: save file has invalid format---")
                return None
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading game: {e}")
        return None
    except Exception as e:
        print(f"---an unexpected error ocurred during load: {e}---")



def display_status(room_id):
    print(f"\nLocation: {room_id}")
    print("----------------------")

def show_help():
    ##prints the help message##
    print("=============")
    print("Available commands are as follows:")
    print("  look - check surroundings / status")
    print("  move - initiate moving to another area")
    print("  quit - exit the game")
    print("  flip - you do a sick flip")
    print("  help - show this message")
    print(" inventory - show contents of inventory")

def handle_look(room_id, room_dict, player_status_dict):
    current_room_data = room_dict[room_id]
    print(f"Flashlight: {player_status_dict['flashlight']}% | Score: {player_status_dict['score']} | Key: {player_status_dict['found_key']}")
    print ("\nLooking around, you see:")
    print(current_room_data.get("description", "an undescribable area.")) ##get to avoid an error##
    ##display the exits##
    exits = current_room_data.get("exits",{})
    print("Available exits:")
    if exits:
        for direction in exits.keys():
            print(f" - {direction}")
    else:
        print("There are no obvious exits.")
    ##print the items##
    current_items = current_room_data.get("items",[])
    print("\nItems available:")
    if current_items:
        for item in current_items:
            print(f" - {item}")
    else:
        print("you're broke buddy")
def handle_move(current_id, rooms_dict):
    current_exits = rooms_dict[current_id].get("exits",{})
    if not current_exits:
        print("nowhere to go.")
        return current_id
    print("Available directions:")
    for direction in current_exits.keys():
        print(f" = {direction}")
    
    movement_input = input("Which direction would you like to go?")
    player_choice = movement_input.lower()

    if player_choice in current_exits:
        next_room_id = current_exits[player_choice]
        print(f"\nYou move {player_choice}")
        print("\n" + rooms_dict[next_room_id].get("description", "there are no words for this area, you can only gasp."))
        return next_room_id
    else:
        print(f"\nYou can't go {player_choice} from this location")
        return current_id
def handle_flip(score, has_flipped):
    print("you do the sickest flip that has ever been done")
    new_score = score + 20
    new_flipped_status = has_flipped
    if not has_flipped:
        new_score+=10
        print("first flip bonus! you figured the game out!")
        new_flipped_status = True
    else:
        print("you do another flip, just as sick as the last one")
        new_score = score + 100
    print(f"your score is now: {new_score}")
    return new_score, new_flipped_status

def handle_quit():
    a = input("are you sure you want to quit? (Y/N) > ")
    b = a.lower()
    if b == "y":
        exit
    elif b == "n":
        print("okay, let's continue")
    else:
        print("that wasn't an option buddy, please type y for yes, and n for no")
        handle_quit()

def handle_get(current_items, room_id, rooms_dict):
    print("Available items to get are:")
    available_items = rooms_dict[room_id].get("items",[])
    for item in available_items:
        print(f" - {item}")
    choice = input("Which one would you like to have? > ")
    player_choice = choice.lower()
    if player_choice in available_items:
        if player_choice in current_items:
            print("you already have that.")
        else:
            new_item = player_choice
            new_inventory = current_items + [new_item]
            rooms_dict[room_id]["items"].remove(new_item)
            return new_inventory
    else:
        still_running = True
        while still_running == True:
            a = input("Would you like to try again? (y/n)")
            b = a.lower()
            if b == "y":
                handle_get(current_items,available_items)
                still_running = False
            elif b == "n":
                print("okay, back to the game")
                return(current_items)
                still_running = False    
                
            else:
                print("this wasn't an option motherfucker")
                print("try again and put either y for yes or n for no")

def handle_drop(current_items, room_id, rooms_dict):
    drop_item = input("which item woudl you like to drop?")
    dropped_item = drop_item.lower()
    if dropped_item in current_items:
        new_items = [x for x in current_items if x !=dropped_item]
        print(f"here are your new items {new_items}")
        current_room_data = rooms_dict[room_id]
        current_room_items = current_room_data.get("items", [])
        rooms_dict[room_id].setdefault("items",[]).append(dropped_item)
        return new_items
    else:
        return current_items

def handle_inventory(player_inventory):
    ##display current inventory##
    print("Here is your current inventory")
    print("====================================")
    print("====================================")
    for item in player_inventory:
        print(f" - {item}")
    
def parse_command(player_input):
    ##handle commands with multiple words##
    result = player_input.split()
    print("-------------------------------")
    print("-------------------------------")
    for item in result:
        print(f" - {item}")
     
    print("returning:",result)
    return result
def display_player_info(player_info):
    
    print(player_info)



   



current_room_id = "parking lot"
inventory = ["$100"]
has_flipped = False
initial_score = 0
initial_has_flipped = False
initial_flashlight = 100
initial_found_key = False
player_stats = {
    "score": initial_score,
    "has_flipped": initial_has_flipped,
    "flashlight": initial_flashlight,
    "found_key": initial_found_key,
    
}

player = Player     

rooms = {
    "Gym Locker Room": {  # Colon after room name key
        "description": "You are in the dusty back room of a gym, you are offered steroids by the guy next to you.",  # Comma added
        "exits": {
            "north": "Gloomy Hallway",  # Comma optional on last item in inner dict
            "south": "parking lot"
        },  # Comma added
        "items": ["steroids"]  # Changed to list for consistency
    },  # Comma added between rooms
    "Shower Area": {  # Colon added
        "description": "you are in the shower room, its wet and humid, and it smells bad",  # Comma added
        "exits": {"west": "Gloomy Hallway"},  # Comma added
        "items": ["soap"]  # Changed to list
    },  # Comma added
    "Weight room": {  # Colon added
        "description": "a loud weight room, crowded with people with the clank of metal against metal and grunts from the men inside",  # Comma added
        "exits": {"east": "Gloomy Hallway"},  # Comma added
        "items": ["chalk", "weight belt", "needles"]  # Already a list - good!
    },  # Comma added
    "Gloomy Hallway": {  # Colon added, fixed capitalization consistency
        "description": "You've entered a gloomy, narrow hallway. The only light comes from the room to the SOUTH. Another door is visible to the EAST.",  # Comma added
        "exits": {
            "south": "Gym Locker Room",
            "east": "Shower Area",
            "west": "Weight room",

        },  # Comma added (optional on last item)
        "items": [] # Added empty list for consistency if no items
    },  # Comma added
    "parking lot": {  # Colon added
        "description": "A crowded parking lot with a lot of cars driving around looking for parking, you hear honking in the distance",  # Comma added
        "exits": {
            # Changed exit from self-loop (unless intended)
            "north": "Gym Locker Room"
        },  # Comma added
        "items": ["car"]  # Changed to list
    }
}
running = True
while running:
    display_status(current_room_id)
    player_input = input("What do you want to do? > ")
    choice = player_input.lower()
    if choice == "look":
        handle_look(current_room_id, rooms, player_stats)
    elif choice == "quit":
        running = handle_quit()
    elif choice == "save":
        handle_save(current_room_id, inventory, player_stats)
    elif choice == "load":
        loaded_data = handle_load()
        if loaded_data is not None:
            current_room_id = loaded_data["current_room_id"]
            inventory = loaded_data["inventory"]
            player_stats = loaded_data["player_stats"]
            print("---game state restored---")
            handle_look(current_room_id, rooms, player_stats)
            handle_inventory(inventory)
    elif choice == "move":
        current_room_id = handle_move(current_room_id, rooms)
        
    elif choice == "flip":
        returned_score, returned_flip = handle_flip(player_stats["score"],player_stats["has_flipped"])
        player_stats["score"] = returned_score
        player_stats["has_flipped"] = returned_flip
    elif choice == "drop":
        inventory = handle_drop(inventory, current_room_id, rooms)
    elif choice == "get":
        inventory = handle_get(inventory, current_room_id, rooms)
    elif choice == "help":
        show_help()
    elif choice == "info":
        display_player_info(player_stats)
    elif choice == "inventory" or choice == "i":
        player.show_inventory()
    
    else:
        print("that is not a valid choice")
        show_help()
        answer = input("Do you want to quit? (y/n)")
        a = answer.lower()
        if a == "y":
            running = False

