def validate_move(position, board):
    try:
        position = int(position)
        if 1 <= position <= 9 and board.is_cell_empty(position):
            return True
        return False
    except (ValueError, KeyError):
        return False


def clean_input(user_input):
    cleaned = user_input.strip()
    return int(cleaned)


def get_available_moves(board):
    for position in range(1, 10):
        if board.is_cell_empty(position):
            yield position