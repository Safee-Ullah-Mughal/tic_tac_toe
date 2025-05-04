"""
Logger module for the Tic-Tac-Toe game.
Manages game logging to files.
"""

import time
from pathlib import Path
from tools.display import board_to_string


class Logger:
    
    def __init__(self):
        self.base_log_dir = Path("game_log")
        self.game_number = self._get_next_game_number()
        self.log_dir = self.base_log_dir / f"game{self.game_number}"
        self.log_file = self.log_dir / "log.txt"
        self.move_count = 0
        self.create_log_directory()
    
    def create_log_directory(self):
        self.log_dir.mkdir(parents=True, exist_ok=True)
    
    def _get_next_game_number(self):

        self.base_log_dir.mkdir(parents=True, exist_ok=True)

        existing_games = [d for d in self.base_log_dir.iterdir() 
                          if d.is_dir() and d.name.startswith("game")]
        
        if not existing_games:
            return 1

        game_numbers = []
        for game_dir in existing_games:
            try:
                num = int(game_dir.name.replace("game", ""))
                game_numbers.append(num)
            except ValueError:
                continue
        
        return max(game_numbers, default=0) + 1
    
    def start_game(self, player1, player2):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        header = (
            f"Game {self.game_number} Log\n"
            f"Started: {timestamp}\n\n"
            f"Players:\n"
            f"- {player1.name} ({player1.marker})\n"
            f"- {player2.name} ({player2.marker})\n\n"
            f"First move: {player1.name}\n\n"
            f"Moves:\n"
        )
        
        with open(self.log_file, "w") as f:
            f.write(header)
    
    def log_move(self, player, position, board):
        self.move_count += 1
        
        move_info = f"Move {self.move_count}: {player.name} -> Position {position}\n"
        board_state = f"Board After Move {self.move_count}:\n{board_to_string(board)}\n\n"
        
        with open(self.log_file, "a") as f:
            f.write(move_info)
            f.write(board_state)
    
    def log_result(self, result):
        with open(self.log_file, "a") as f:
            f.write(f"Result: {result}\n")