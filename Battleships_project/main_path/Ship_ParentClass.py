


class Ship:
    def __init__(self):
        pass

    def horizontal_or_vertical(self):
        user_input = input(f"Do you want this ship to be rotated horizontal or vertical? \n('H' for horizontal and 'V' for vertical: ")
        if user_input.lower() == 'h':
            return True
        elif user_input.lower() == 'v':
            return False