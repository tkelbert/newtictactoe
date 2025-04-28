# --- Variable Setup ---
# We'll replace these single location variables with the dictionary structure later

location_description = "In a dusty locker room, a sweaty and very large man with a gym bag pulls out some steroids to sell you"
# Assuming this is assigned to a variable, like 'world_map' or 'rooms'
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
            "west": "Weight room"
        }  # Comma added (optional on last item)
        # "items": [] # Added empty list for consistency if no items
    },  # Comma added
    "parking lot": {  # Colon added
        "description": "A crowded parking lot with a lot of cars driving around looking for parking, you hear honking in the distance",  # Comma added
        "exits": {
            # Changed exit from self-loop (unless intended)
            "north": "Gym Locker Room"
        },  # Comma added
        "items": ["car"]  # Changed to list
    }
}  # Final closing brace for the main 'rooms' dictionary

# --- Game State ---
current_room_id = "Gym Locker Room"  # Start in the locker room
current_room_id = "Gym Locker Room"
# Player status variables
found_key = False
flashlight = 100
player_score = 0
did_flip_this_game = False  # To track if the flip bonus was given

# --- Game Loop Control ---
running = True  # This boolean controls the main loop

# --- Initial Welcome/Setup (Runs Once) ---
print("Welcome back to the Gym Adventure!")
print("(Type 'help' for commands, 'quit' to exit)")
print("========================================")

# --- Main Game Loop (Repeats) ---
while running:  # Using 'running' as you had it, same as 'game_running'

    # ----- START OF A TURN -----

    # Display current status
    # NOTE: We'll change 'start_location' to 'current_room_id' in the next step
    print("You are in", current_room_id)
    print("------------------------------")
    current_room_data = rooms[current_room_id]
    # Get the command for this turn
    player_input = input("What do you want to do? > ")
    command = player_input.lower()
    print("---")  # Optional separator

    # Process the command
    if command == "look":
        # NOTE: We'll change this to fetch from the dictionary in the next step
        print(location_description)
        # Adding status details here is good practice for 'look'
        print(
            f"Flashlight: {flashlight}% | Score: {player_score} | Key: {found_key}")
        print("looking around, you see:")
        description = current_room_data["description"]
        print(description)
        exits = current_room_data["exits"]
        print("\nAvailable exits:")

        if exits:
            for direction in exits.keys():
                print(f" - {direction}")
        else:
            print("there are no obvious exits")
        items = current_room_data.get("items",[])
        print("\nItems visible")
        if items:
            for item in items:
                print(f" - {item}")
        else:
            print("\nNothing of interest")

    elif command == "quit":
        print("Okay, heading out. See you next time!")
        running = False  # Stop the loop

    elif command == "help":
        print("=============")
        print("Available commands are as follows:")
        print("  look - check surroundings / status")
        print("  quit - exit the game")
        print("  flip - you do a sick flip")
        print("  help - show this message")

    elif command == "flip":
        print("You execute a surprisingly agile flip!")
        if not did_flip_this_game:  # Give points only for the first flip
            player_score += 10
            print("First flip bonus! +10 points!")
            did_flip_this_game = True
        else:
            print("Still fun, but you already got the flip points.")
        print(f"Your score is now: {player_score}")
    elif command == "move":
        print("okay time to move! Your available directions are:")
        current_exits = current_room_data["exits"]
        if not current_exits:
            print("just kidding theres no exits")
        else:
            for exit in current_exits:
                print(f" - {exit}")
            movement = input("Which direction do you want to go in? > ")
            chosen_direction = movement.lower()
            if chosen_direction in current_exits:
                next_room_id = current_exits[chosen_direction]
                current_room_id = next_room_id
                print(f"\nYou move{chosen_direction}")
                print("\n" + rooms[current_room_id]["description"])
            else:
                print(f"\nYou can't go '{chosen_direction}'from here. Try one of the other directions")
    else:
        # Handle unrecognized commands
        print(
            f"Sorry, I don't understand the command '{player_input}'. Try 'help'.")

    # ----- END OF A TURN -----
    # The loop automatically goes back to the 'while running:' line

# --- Post-Loop (Runs Once After Loop Ends) ---
print("\n========================================")
print("Thanks for playing!")
# Optional: Show final score
print(f"Your final score was: {player_score}")
print("========================================")
