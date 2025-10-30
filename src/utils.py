def is_valid_move(start, end, board):
    start_row, start_col = start
    end_row, end_col = end
    piece = board[start_row][start_col]
    if piece == 'P':  # Пешка
        if start_col == end_col and (end_row == start_row - 1 or (start_row == 6 and end_row == 4)):
            return True
    elif piece == 'R':  # Ладья
        if start_row == end_row or start_col == end_col:
            return True
    elif piece == 'N':  # Конь
        if abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1 or abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2:
            return True
    elif piece == 'B':  # Слон
        if abs(start_row - end_row) == abs(start_col - end_col):
            return True
    elif piece == 'Q':  # Ферзь
        if start_row == end_row or start_col == end_col or abs(start_row - end_row) == abs(start_col - end_col):
            return True
    elif piece == 'K':  # Король
        if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
            return True
    return False