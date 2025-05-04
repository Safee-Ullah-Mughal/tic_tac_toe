import sys
from game.board import Board
from game.players import Player
from tools.display import welcome_message, display_board, announce_winner, prompt_replay
from tools.logger import Logger


def main():
    """Main function to run the Tic-Tac-Toe game."""
    while True:
        # Get player names
        player1_name = input("Please enter Player 1 name: ")
        player2_name = input("Please enter Player 2 name: ")
        
        # Display welcome message
        welcome_message(player1_name, player2_name)
        
        # Initialize game components
        board = Board()
        player1 = Player(player1_name, "X")
        player2 = Player(player2_name, "O")
        current_player = player1
        logger = Logger()
        
        # Log game start
        logger.start_game(player1, player2)
        
        # Main game loop
        while True:
            # Display current board
            display_board(board)
            
            # Get player's move
            position = current_player.get_move(board)
            
            # Update board with move
            board.place_marker(position, current_player.marker)
            
            # Log the move
            logger.log_move(current_player, position, board)
            
            # Check for win or draw
            if board.check_winner(current_player.marker):
                display_board(board)
                announce_winner(current_player.name)
                logger.log_result(f"{current_player.name} wins!")
                break
            
            if board.is_full():
                display_board(board)
                print("It's a draw!")
                logger.log_result("Draw")
                break
            
            # Switch players
            current_player = player2 if current_player == player1 else player1
        
        # Ask if players want to play again
        if not prompt_replay():
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame terminated by user. Goodbye!")
        sys.exit(0)
