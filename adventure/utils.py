COMPASS_SHORT_MAP = {
    "n": "north",
    "e": "east",
    "s": "south",
    "w": "west",
}

def get_reverse_direction(direction: str) -> str:
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    elif direction == 'w':
        return 'e'
