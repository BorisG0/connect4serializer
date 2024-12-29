

def print_board(board):
    for row in board:
        print(row)
    print()

def play_tile(board, column, player):
    for row in range(5, -1, -1):
        if board[row][column] == 0:
            board[row][column] = player
            return True
    return False

def start_game():

    def play_turn(player):
        print("Player", player ,"what column? (1-7)")
        column = int(input()) - 1
        if not play_tile(board, column, player):
            print("Invalid move")
            play_turn(player)
            return
        print_board(board)

    board = [[0 for _ in range(7)] for _ in range(6)]
    print_board(board)
    player = 1
    
    

    while True:
        play_turn(player)
        player = 3 - player



start_game()