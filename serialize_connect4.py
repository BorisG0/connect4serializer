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

def deserialize_game(serialized_game):
    board = [[0 for _ in range(7)] for _ in range(6)]
    turn = 0

    while serialized_game > 6:
        column = serialized_game % 7
        serialized_game = serialized_game // 7
        print("turn", turn, "column", column)
        _, row = play_tile(board, column, turn%2 + 1)
        turn += 1

    print_board(board)
    print("turn:", turn)

    last_player = (turn - 1) % 2 + 1
    if turn > 3 and check_win(board, last_player, row, column):
        print("Player", last_player,"wins!")
        exit()

    print("processed",serialized_game)
    return board, turn

def start_game():
    board = [[0 for _ in range(7)] for _ in range(6)]
    turn = 0
    serialized_game = 0

    def play_turn():
        nonlocal turn
        nonlocal board
        nonlocal serialized_game

        player = turn % 2 + 1

        print("Player", player ,"what column? (1-7)")

        inp = input()
        if len(inp) > 3 and inp[:3] == "des":
            print("Deserializing")
            print(int(inp[3:]))

            serialized_game = int(inp[3:])
            board, turn = deserialize_game(serialized_game)
            serialized_game = serialized_game - serialize_turn(1, turn)
            print("serialized:", serialized_game)
            return


        column = int(inp) - 1
        if column < 0 or column > 6:
            print("Invalid move")
            play_turn(player)
            return

        valid, placed_row = play_tile(board, column, player)
        if not valid:
            print("Invalid move")
            play_turn(player)
            return
        
        print_board(board)
        
        serialized_game += serialize_turn(column, turn)
        print("serialized:", (serialized_game + serialize_turn(1,turn +1))) # add 1 to indicate turn
        turn += 1

        if check_win(board, player, placed_row, column):
            print("Player", player, "wins!")
            exit()

    
    print_board(board)
    
    while True:
        play_turn()



start_game()