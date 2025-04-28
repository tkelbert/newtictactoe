import math
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

print(f"This is the default color.")
print(f"{RED}This text is red!{RESET}")
print(f"{GREEN}This text is green.{RESET}")
print(f"This part is default, {BLUE}this part is blue{RESET}, and back to default.")
print(f"{YELLOW}Warning:{RESET} Something might be wrong.")

class ConnectFourGame:
    def __init__(self):
       
        self.winning = None
        self.board = []
        self.current_player = 'X'
        self.truth = False
        self.coordinate_list = [' ']*4

    def create_board(self):
        rows, cols = 6, 7

        arr = [[' ' for _ in range(cols)] for _ in range(rows)]

        for i in range(7):
            arr[0][i] = ' '
        arr[3][5] = 'X'
        arr[3][2] = 'X'
        arr[3][3] = 'X'
        arr[3][4] = 'X'
        arr[4][4] = ' '
        arr[5][1] = ' '
        self.board = arr
        return arr

    def display_board(self, board_array=None):
        if board_array == None:
            board_array = self.board
        for i in range(7):
            print(f" {i}",end = '' )
        print(f"\n--------------")
        for i in range(6):
            print(f"|", end='')
            for j in range(7):
                try:
                    print(f"{board_array[i][j]}", end='|')
                except:
                    print(f"i:{i}, j:{j}")
            print(f"\n--------------")
            
    def gravity_check(self, board_state, column):
        contents_of_column = []
        for i in range(6):
            contents_of_column.append(self.board[i][column])

        print(contents_of_column)

        empty_col = 0 
        for i in range(6):
            if board_state[i][column] != ' ':
                
                print(f"{i} is {self.board[i][column]} in the location [{i},{column}]")
                top_open_space = (i-1)
                if i == 0:
                    print("column full, try again")
                    if self.board[0][column] == ' ':
                        return 0 
                empty_col += 1
                print(f"top_open_space: {top_open_space}")
                return top_open_space
        if empty_col == 0:
            print("col is empty")
            return 5
        empty_col = 0
        print("DEBUG: COLUMN IS FULL")
        return None
            
    def play_move(self, col, current_player, board_state=None):
        if board_state==None:
            board_state = self.board
        try:
            move = self.gravity_check(board_state, col)
        except TypeError as e:
            print({e})
            print("you just made an illegal move you complete idiot!")
            return False
        row = int(move)
        if row >= 0:
            board_state[row][col] = current_player
            print(f"Playing a move for player {current_player} at coordinates {row},{col}")
        else:
            print("illegal move, youre under arrest. no move has been played")
        
        return board_state

    def switch_players(self, current_player= None):
        if current_player == None:
            current_player = self.current_player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
        return current_player
    def get_move(self):
        move = input("Which column would you like to play in? choose between 0 and 6 based on the numbers on top of the game board > ")
        move = int(move)
        ##error checking on this move
        if move > -1 and move < 7:
            print(f"passing {move} to the move variable")
            return move
        else: 
            print("illegal move, try again")
            return False

    def is_game_over(self, board_status= None):
        if board_status == None:
            board_status = self.board
        ##check if board is full
        empty_spaces = 0
        for row in board_status:
            for cell in row:
                if cell == ' ':
                    empty_spaces =+ 1
        if empty_spaces == 0:
            print("full board")
            return False
        ## check for horizontal victories
        far_left = 0
        far_right = 4
        print("DEBUG CHECK")
        if self.horizontal_check(board_status) == True:
            print("end from game over loop")
            return False
        if self.vertical_check(board_status) == True:
            print("end from game over loop")
            return False
        
        ''' for rows in range(6):
            
            counter = 0
            for j in range(4):
                for i in range(far_left, far_right):
                    print(f"checking {far_left} to {far_right}")
                    check = far_left + j
                    print(f"printing: {self.current_player} in location {rows} {i} and check is {check}")
                    
                    print(f"far_left + j = {check}")
                    if board_status[rows][check] != ' ':
                        counter = counter + 1
                        print(f"counter added to, current level: {counter}. Rows: {rows} i = {i}")
                    if counter == 3:
                        print("winner winner")
                        if board_status[far_left][rows] == board_status[far_left+1][rows] == board_status[far_left + 2][rows] == board_status[far_right][rows]:
                            print("we have a victory")
                            print(f"winning squares are between [{far_left} and {far_right} in row {rows}]")
                            self.display_board()
                            return True
                counter = 0
                    '''

    def counting_practice(self):
        first_step = 0 
        rows, cols = 6, 7

        arr = [[' ' for _ in range(cols)] for _ in range(rows)]
        x = 0
        for rows in range(6):
            for col in range(7):
                x += 1
                arr[rows][col] = x
        self.display_board(arr)

        examination = [' '] * 4
        print(examination)
        ##try to get one row read in groups of for
        column = 0 
        y = 0 
        number_for_exam = 0 
        total_numbers = [' ',' ',' ',' ']
        for f in range(3):
            for column in range(7):
                for i in range(y,(y+4)):
                    print(f"i{i}, column {column}")
                    examination[number_for_exam] = arr[i][column]
                    print(f" - examining {examination[number_for_exam]}, i:{i}, column {column}")
                    number_for_exam += 1
                    
                number_for_exam = 0
                print(examination)
                print(f"total numbers{total_numbers}")
                total_numbers.append(examination.copy())
                
            y += 1                
        print(first_step) 
        print(total_numbers)
        return arr



    def vertical_check(self, board_state=None):
        if board_state == None:
            board_state = self.board
        block_to_check = [' '] * 4
        column = 0
        range_start = 0
        number_to_check = 0
        total = [' ',' ',' ',' ']
        for f in range(3):
            for column in range(7):
                for i in range (range_start, (range_start + 4)):
                    block_to_check[number_to_check] = board_state[i][column]
                    
                    number_to_check += 1
                ##for a in range(4):
                #    print(f"{block_to_check[a]} a : {a}", end='|' )
                number_to_check = 0
                if block_to_check[number_to_check] == block_to_check[number_to_check + 1] == block_to_check[number_to_check + 2] == block_to_check[number_to_check + 3]:
                    if block_to_check[number_to_check] != ' ':
                        print('hello')
                        print(f"winning 4 are in column: {column} between {range_start} and {range_start + 3}")
                        print(f"block to check: {block_to_check}")
                        print(block_to_check[number_to_check])
                        bae = 0
                        self.winning = [column, range_start, range_start+3]
                        self.truth = True
                        print(f"setting self.truth to {self.truth}")
                        self.vertical_coordinate_getter()
                        return True
                
                
                
                total.append(block_to_check.copy())
                print(block_to_check)
                
            range_start += 1

        print(f"we did it. ")
        print(total)



    def vertical_coordinate_getter(self):
        column = self.winning[0] 
        up_most = self.winning[1]
        coordinate_list = []
        player = self.board[column][up_most]
        if player == ' ':
            player = self.current_player
        for i in range(4):
            new_coords = [column, up_most]
            coordinate_list.append(new_coords)
            
            self.board[up_most][column] = f'{RED}{player}{RESET}'
            up_most += 1       
        print(coordinate_list)
        self.coordinate_list = coordinate_list
        
        
    def horizontal_check(self, board=None):
        if board == None:
            board = self.board
        block_to_check = [' '] * 4
        range_start = 0
        number_to_check = 0
        total = [' '] * 4
        
        for row in range(5):
            for q in range(3):
                while range_start + 4 < 8:
                    for i in range(range_start, range_start + 4):
                        if i < 7:
                            if row == 6:
                                print("debug: row overflow caught")
                                return False
                            print(f"number to check {number_to_check}, row :{row} | i : {i} | range start + 3{range_start + 3}")
    
                            block_to_check[number_to_check] = board[row][i]
                           
                            number_to_check += 1
                            ##print(block_to_check)
                            ##print(f"row:{row} | range start {range_start} | range end {range_start + 3}, i: {i}")
                        else:
                            pass
                    
                        
                    number_to_check = 0
                    print(f"finalized version of {block_to_check}")
                    
                    if block_to_check[number_to_check] == block_to_check[number_to_check + 1] == block_to_check[number_to_check + 2] == block_to_check[number_to_check + 3]:
                        if block_to_check[number_to_check] != ' ':
                            print("horizontal check completed")
                            print(f"row:{row} | range start {range_start} | range end {range_start + 3}")
                            self.winning = [row, range_start, range_start + 3]
                            self.truth = True
                            print(self.winning)
                            self.horizontal_coordinate_getter()
                            print(f"self.coordinate list {self.coordinate_list}")
                            
                            return True
                    range_start += 1
                    if range_start > 3:
                       
                        row = row + 1
                        range_start = 0
                    
    def horizontal_coordinate_getter(self):
        row = self.winning[0]
        column = self.winning[1]

        coordinate_list = []
        player = self.board[row][column]
        if player == ' ':
            player = self.current_player
        for i in range(4):
            new_coords = [row, column]
            coordinate_list.append(new_coords)
            self.board[row][column] = f"{RED}{player}{RESET}"
            print(f"column: {column}")
            column = column + 1
            
        self.coordinate_list = coordinate_list


game = ConnectFourGame()
game.board = game.create_board()
game.display_board(game.board)

print('attempting initial horizontal check')
game.horizontal_check()
print(f"the self.coordinate list {game.coordinate_list}")


'''game.vertical_check(game.counting_practice())
game.vertical_check(game.board)
running = True
array = game.counting_practice()
game.horizontal_check(array)

while not game.is_game_over():
    game.display_board()
    move = None
    while move is None or move is False:
        move = game.get_move()
        print(move)
        print("====")
        if move is False:
            print("invalid input detected, please try again")
    game.board = game.play_move(move, game.current_player)
    
   
    print(game.current_player)
    ##game.horizontal_check()
    if game.vertical_check() == True or game.horizontal_check() == True:
        game.display_board()

        if game.truth == True:
            game.vertical_coordinate_getter()
        break
    game.current_player = game.switch_players(game.current_player)
game.display_board()
print(game.coordinate_list)
print("game over")'''