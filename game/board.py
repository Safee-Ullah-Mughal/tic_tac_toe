from game.utils import get_available_moves


class Board:
    
    def __init__(self):
        # Board positions are numbered 1-9
        self.cells = {i: str(i) for i in range(1, 10)}
        self.winning_combinations = [
            # Rows
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            # Columns
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            # Diagonals
            [1, 5, 9], [3, 5, 7]
        ]
    
    def get_board_state(self):
        return self.cells.copy()
    
    def get_cell(self, position):
        return self.cells[position]
    
    def is_cell_empty(self, position):
        return self.cells[position] not in ['X', 'O']
    
    def place_marker(self, position, marker):
        if self.is_cell_empty(position):
            self.cells[position] = marker
            return True
        return False
    
    def check_winner(self, marker):
        for combo in self.winning_combinations:
            if all(self.cells[pos] == marker for pos in combo):
                return True
        return False
    
    def is_full(self):
        return all(cell in ['X', 'O'] for cell in self.cells.values())
    
    def get_available_moves(self):
        return get_available_moves(self)
    
    def reset(self):
        self.cells = {i: str(i) for i in range(1, 10)}