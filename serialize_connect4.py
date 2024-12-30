def print_board(board):
    for row in board:
        print(row)
    print()

def play_tile(board, column, player):
    for row in range(5, -1, -1):
        if board[row][column] == 0:
            board[row][column] = player
            return True, row
    return False

def check_win(board, player, row, column):
    # check vertical
    if row <= 2:
        if board[row+1][column] == player and board[row+2][column] == player and board[row+3][column] == player:
            return True
        
    # check horizontal
    search = 1
    count = 1
    # search left
    while column - search >= 0 and board[row][column - search] == player:
        count += 1
        search += 1

    # search right
    search = 1
    while column + search < 7 and board[row][column + search] == player:
        count += 1
        search += 1
    
    if count >= 4:
        return True


    # check diagonal
    search = 1
    count = 1
    # search left up
    while row - search >= 0 and column - search >= 0 and board[row - search][column - search] == player:
        count += 1
        search += 1

    # search right down
    search = 1
    while row + search < 6 and column + search < 7 and board[row + search][column + search] == player:
        count += 1
        search += 1

    if count >= 4:
        return True

    # search left down
    search = 1
    count = 1
    while row + search < 6 and column - search >= 0 and board[row + search][column - search] == player:
        count += 1
        search += 1

    # search right up
    search = 1
    while row - search >= 0 and column + search < 7 and board[row - search][column + search] == player:
        count += 1
        search += 1

    if count >= 4:
        return True

    return False
    

def serialize_turn(column, turn):
    return 7**turn * column

def start_game():
    turn = 0
    serialized_game = 0

    def play_turn(player):
        print("Player", player ,"what column? (1-7)")
        column = int(input()) - 1

        valid, placed_row = play_tile(board, column, player)
        print(placed_row)
        if not valid:
            print("Invalid move")
            play_turn(player)
            return
        
        print_board(board)
        nonlocal turn
        nonlocal serialized_game

        turn += 1
        serialized_game += serialize_turn(column, turn)
        print("serialized:", serialized_game)

        if check_win(board, player, placed_row, column):
            print("Player", player, "wins!")
            exit()

    board = [[0 for _ in range(7)] for _ in range(6)]
    print_board(board)
    player = 1
    
    
    while True:
        play_turn(player)
        player = 3 - player



start_game()