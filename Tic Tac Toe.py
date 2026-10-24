def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")
    print()


def check_winner(board):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def dfs(board, computer_turn):
    result = check_winner(board)

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Draw":
        return 0

    if computer_turn:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = dfs(board, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score

    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = dfs(board, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score


def computer_move(board):
    best_score = -float("inf")
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = dfs(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    if move != -1:
        board[move] = "O"


def play_game():
    board = [" "] * 9

    print("Tic Tac Toe")
    print("You are X, Computer is O")
    print("Enter positions from 1 to 9:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")

    while True:
        print_board(board)

        try:
            position = int(input("Enter your position (1-9): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid position. Try again.")
            continue

        board[position] = "X"
        result = check_winner(board)

        if result:
            print_board(board)
            print("You win!" if result == "X" else "It's a draw!")
            break

        computer_move(board)
        result = check_winner(board)

        if result:
            print_board(board)
            print("Computer wins!" if result == "O" else "It's a draw!")
            break


if __name__ == "__main__":
    play_game()
