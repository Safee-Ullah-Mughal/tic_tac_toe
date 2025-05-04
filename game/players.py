import random
from game.utils import validate_move, clean_input


class Player:
    
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker
    
    def get_move(self, board):
        if self.name.lower() == "computer":
            return self._get_computer_move(board)
        
        while True:
            try:
                print(f"{self.name}'s Turn ({self.marker}):")
                user_input = input("Enter a position (1-9): ")
                position = clean_input(user_input)
                
                if validate_move(position, board):
                    return position
                print("That position is already taken or invalid. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
    
    def _get_computer_move(self, board):
        available_moves = list(board.get_available_moves())
        position = random.choice(available_moves)
        print(f"{self.name}'s Turn ({self.marker}):")
        print(f"Computer selects position {position}")
        return position