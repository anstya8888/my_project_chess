def is_valid_move(start, end, board):
    start_row, start_col = start
    end_row, end_col = end
    piece = board[start_row][start_col]
    # Простая проверка на валидность хода (пока без логики шахмат)
    if start_row < 0 or start_row > 7 or start_col < 0 or start_col > 7:
        return False
    if end_row < 0 or end_row > 7 or end_col < 0 or end_col > 7:
        return False
    if piece == ' ':
        return False
    return True