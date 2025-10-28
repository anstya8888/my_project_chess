from utils import is_valid_move
class ChessBoard:
    def __init__(self):
        self.board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
        self.current_player = 'white'

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]
        self.board[start_row][start_col] = ' '
        self.board[end_row][end_col] = piece

def get_user_input():
    start = input("Введите начальную позицию (например, '6 0'): ")
    end = input("Введите конечную позицию (например, '4 0'): ")
    return tuple(map(int, start.split())), tuple(map(int, end.split()))

def main():
    board = ChessBoard()
    while True:
        board.display_board()
        print(f"Ходит {board.current_player}")
        start, end = get_user_input()
        if is_valid_move(start, end, board.board):
            board.move_piece(start, end)
            board.display_board()
            if board.current_player == 'white':
                board.current_player = 'black'
            else:
                board.current_player = 'white'
        else:
            print("Недопустимый ход!")

if __name__ == "__main__":
    main()