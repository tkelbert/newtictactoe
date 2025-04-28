import random


class TicTacToe:

    def __init__(self):
        # 0 | 1 | 2
        # ---------
        # 3 | 4 | 5
        # ---------
        # 6 | 7 | 8
        # ' ' empty, 'X' for player, 'O' for the computer
        self.board = [" "] * 9
        self.current_player = "X"
        print("New board initialized")
        print(f"board: {self.board}")
        print(f"player {self.current_player}'s turn")

    def display_board(self):
        print("\n Board:")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("")

    def move_numbers(self):
        print("\n Board:")
        print(f" 0 | 1 | 2 ")
        print("---|---|---")
        print(f" 3 | 4 | 5 ")
        print("---|---|---")
        print(f" 6 | 7 | 8 ")
        print("")

    def is_valid_move(self, move):
        if move >= 0 and move < 9:
            if self.board[move] == " ":
                print("legal move confirmed")
                return True
            else:
                print("square already taken")
                return False
        else:
            print(f"{move} is not between 0 and 8")
            return False

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def make_move(self, move):
        if self.is_valid_move(move) == True:
            self.board[move] = self.current_player
            self.switch_player()
            self.display_board()
            return True
        else:
            print("invalid move")
            return False

    def get_move(self):
        self.move_numbers()
        move = input(
            "Pick a number between 0 and 8 that corresponds to one of the empty squares on the board > ")
        move1 = int(move)
        return move1

    def check_winner(self, board=None):
        if board is None:
            board = self.board
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        for line in win_conditions:
            sq1, sq2, sq3 = board[line[0]], board[line[1]], board[line[2]]

            if sq1 == sq2 == sq3 and sq1 != " ":
                return sq1
        return None

    def is_draw(self, board=None):
        if board is None:
            board = self.board
        if " " not in board:
            if self.check_winner(board=board) is None:
                print("draw confirmed, no winner")
                return True
        print("not a draw")
        return False

    def get_available_moves(self, board=None):
        if board is None:
            board = self.board
        moves = []
        for i in range(9):
            if board[i] == " ":
                moves.append(i)
        return moves

    def minimax(self, board_state, is_maximizing):
        winner = self.check_winner(board=board_state)
        if winner:
            return 1 if winner == 'O' else -1
        if self.is_draw(board=board_state):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for move in self.get_available_moves(board=board_state):
                board_copy = board_state.copy()
                board_copy[move] = 'O'

                score = self.minimax(board_copy, False)
                best_score = max(best_score, score)
            return best_score
        else:  # human x's turn
            best_score = float('inf')

            for move in self.get_available_moves(board=board_state):
                board_copy = board_state.copy()

                board_copy[move] = 'X'

                score = self.minimax(board_copy, True)
                best_score = min(best_score, score)
            return best_score

    def find_best_move(self, player):
        best_score = -float('inf')
        best_move = None
        for move in self.get_available_moves():
            board_copy = self.board.copy()
            board_copy[move] = player
            move_score = self.minimax(board_copy, is_maximizing=False)

            if move_score > best_score:
                best_score = move_score
                best_move = move
        return best_move


print("===TicTacToe Class defined===")

game = TicTacToe()
game_over = False


while not game_over:
    if game.current_player == 'X':
        game.display_board()

        print(f"Player {game.current_player}'s turn")
        while True:
            try:
                move = game.get_move()
                if game.is_valid_move(move):
                    break
                else:
                    print("try again")
            except ValueError:
                print("invalid input, please enter a number")

        success = game.make_move(move)

        if not success:
            print("try a different square")
            game.move_numbers()
            continue

        # check for victory or draw after a successful move
        winner = game.check_winner()
        if winner:
            print(f"{winner} has won the game")
            game_over = True
        elif game.is_draw():
            print("\n====== The game is a draw =======")
            game_over = True
    else:
        ai_move = game.find_best_move('O')
        print(ai_move)
        success = game.make_move(ai_move)

print("game over man, game over")
game.display_board()
