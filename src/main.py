class ChessBoard:
    def __init__(self):
        self.board = [
            ['Л', 'N', 'С', 'Ф', 'К', 'С', 'N', 'Л'],
            ['П', 'П', 'П', 'П', 'П', 'П', 'П', 'П'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['п', 'п', 'п', 'п', 'п', 'п', 'п', 'п'],
            ['л', 'n', 'с', 'ф', 'к', 'с', 'n', 'л']
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
    
    def is_free_cell(self, end):
        end_row, end_col = end
        if self.board[end_row][end_col] !=' ':
            return False
        return True 

    def is_valid_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]
        print("Ходит {tmp}".format(tmp=piece))
        if piece == 'п':  # Пешка
            print("Ходит пешка")
            if start_col == end_col and (end_row == (start_row - 1) or (start_row == 6 and end_row == 4)):
                return True
        elif piece == 'П': # Пешка 
            print("Ходит пешка")
            if start_col == end_col and (end_row == (start_row + 1) or (start_row == 1 and end_row == 3)):
                return True 
        elif piece.upper() == 'Л' :  # Ладья
            if start_row == end_row or start_col == end_col:
                return True
        elif piece.upper() == 'N':  # Конь
            if abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1 or abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2:
                return True         
        elif piece.upper() == 'С':  # Слон
            if abs(start_row - end_row) == abs(start_col - end_col):
                return True
        elif piece.upper() == 'Ф':  # Ферзь
            if start_row == end_row or start_col == end_col or abs(start_row - end_row) == abs(start_col - end_col):
                return True
        elif piece.upper() == 'К':  # Король
            if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
                return True
        return False

def get_user_input():
    start = input("Введите начальную позицию (например, '6 0'): ")
    end = input("Введите конечную позицию (например, '4 0'): ")
    if start == 'Stop':
        raise KeyboardInterrupt()
    return tuple(map(int, start.split())), tuple(map(int, end.split()))

def main():
    board = ChessBoard()
    board.display_board()
    while True:
        print(f"Ходит {board.current_player}")
        try:
            start, end = get_user_input()
            if board.is_valid_move(start, end):
                if board.is_free_cell(end):
                    board.move_piece(start, end)
                    board.display_board()
                    if board.current_player == 'white':
                        board.current_player = 'black'
                    else:
                        board.current_player = 'white'
                else:
                    print("Ячейка занята")
            else:
                print("Недопустимый ход!")

        except KeyboardInterrupt as e:
            print("Пока!!!")
            break
        except BaseException as e:
            print("Неверная позиция фигуры")

if __name__ == "__main__":
    main()