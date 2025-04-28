# --- Game World Definition ---
# Using dictionaries to structure room data

world_map = {
    "Gym Back Room": {
        "description": "You are in the dusty back room of a gym. The air smells faintly of sweat and disinfectant. There's a door leading NORTH.",
        "exits": {"north": "Gloomy Hallway"} # Exits link to other room IDs (keys in world_map)
        # We could add keys like "items": ["flyer", "old sock"] later
    },
    "Gloomy Hallway": {
        "description": "You've entered a gloomy, narrow hallway. The only light comes from the room to the SOUTH. Another door is visible to the EAST.",
        "exits": {
            "south": "Gym Back Room",
            "east": "Supply Closet" # Leads to a room we haven't defined yet!
            }
    },
    # We would define "Supply Closet" here too...
    "Supply Closet": {
        "description": "This is a small supply closet. Mostly empty except for some cleaning supplies and a flickering lightbulb. The only exit is WEST.",
        "exits": {"west": "Gloomy Hallway"}
    }
}

# --- Game State Variable ---
# Instead of storing the description directly, store the ID of the current room
current_room_id = "Gym Back Room"

# --- How to use this in the game loop ---

# Example: Getting the current room's data dictionary
current_room_data = world_map[current_room_id]

# Example: Printing the current description
print("Current description:")
print(current_room_data["description"])

# Example: Checking available exits
print("\nAvailable exits:")
available_exits = current_room_data["exits"] # This gets the inner dictionary of exits
for direction in available_exits.keys(): # .keys() gives us "north", "south", etc.
    print(f"- {direction}")

# Example: How we might use an exit later (foreshadowing next step)
# next_room_id = available_exits["north"] # Gets "Gloomy Hallway"
# print(f"\nGoing north leads to: {next_room_id}")