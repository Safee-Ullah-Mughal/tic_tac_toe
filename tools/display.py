def welcome_message(player1, player2):
    print(f"\nWelcome, {player1} and {player2}!")
    print("Let's play Tic-Tac-Toe!\n")


def display_board(board):
    cells = board.get_board_state()
    
    print("\nCurrent Board:")
    print(f" {cells[1]} | {cells[2]} | {cells[3]} ")
    print("-----------")
    print(f" {cells[4]} | {cells[5]} | {cells[6]} ")
    print("-----------")
    print(f" {cells[7]} | {cells[8]} | {cells[9]} ")
    print()


def announce_winner(player_name):
    print(f"Congratulations, {player_name}! You win!")


def prompt_replay():
    while True:
        response = input("Would you like to play again? (yes/no): ").lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def board_to_string(board):
    cells = board.get_board_state()  
    board_str = (
        f" {cells[1]} | {cells[2]} | {cells[3]} \n"
        f"-----------\n"
        f" {cells[4]} | {cells[5]} | {cells[6]} \n"
        f"-----------\n"
        f" {cells[7]} | {cells[8]} | {cells[9]} "
    )
    
    return board_str