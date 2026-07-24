# Each room has a description and a dict of choices mapping
# player input -> next room name
rooms = {
    "start": {
        "description": "You wake up in a dark forest. Paths lead north west and east, but you can also search south.",
        "choices": {"north": "cave", "east": "river", "south": "waterfall", "west": "mountain"}
    },
    "cave": {
        "description": "A damp cave. You hear dripping water. There's a path south.",
        "choices": {"south": "start"}
        # TODO: add more choices/rooms, maybe one with an item or ending
    },
    "river": {
        "description": "A wide river blocks your path. You could go west or search the shore.",
        "choices": {"west": "start", "river_search": "find_rope"}
    },
    "waterfall": {
        "description": "A rushing waterfall is all you see. You could go north or climb down.",
        "choices": {"north": "start", "climb": "find_flashlight"}
    },
    "mountain": {
        "description": "A towering mountain stands before you. You could try to climb it for a better view, or take the cave.",
        "choices": {"climb": "mountain_choice", "north": "cave"}
    },
    
    "ending_good": {
        "description": "You made it across and found a village! You win!",
        "choices": {}  # empty choices = game over
    }
    # TODO: add more rooms — try for at least 5-6, with at least one "bad" ending
}

def show_room(room_name):
    """Print the description of the current room and its choices."""
    room = rooms[room_name]
    print("\n" + room["description"])

    # TODO: if room["choices"] is empty, this is an ending — return False (game over)
    # TODO: otherwise print the available choices, e.g. "Go: north, east"
    # TODO: return True (game continues)
    pass

def get_choice(room_name):
    """Ask the player what they want to do, validate it against available choices."""
    room = rooms[room_name]

    while True:
        choice = input("> ").strip().lower()
        # TODO: check if choice is a valid key in room["choices"]
        # TODO: if valid, return the next room name (room["choices"][choice])
        # TODO: if invalid, print an error and ask again
        pass

def main():
    current_room = "start"
    playing = True

    while playing:
        playing = show_room(current_room)
        if playing:
            current_room = get_choice(current_room)

    print("\nThe End.")

if __name__ == "__main__":
    main()