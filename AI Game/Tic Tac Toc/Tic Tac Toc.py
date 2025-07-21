import random
from colorama import Init ,Fore ,Style
Init(autoreser=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O":
            return Fore.Blue + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(" " + colored(board)[0] + " " + colored(board)[1] + " " + colored(board)[2])
    print(Fore.CYAN + "_ _ _ _ _ _ _" + Style.RESET_ALL)
    print(" " + colored(board)[3] + " " coloured(board)[4] + " " + colored(board[5]))
    print(Fore.CYAN + "_ _ _ _ _ _" + Style.RESET_ALL )
    print(" " + colored(board)[6] + " " + colored(board)[7] + " " + colored(board)[8])
    print()

    def player_choice():
        symbol = " "
        while symbol not in ["X","O"]:
            symbol = input(Fore.GREEN) + "Do you want to be X or 0 ? " + Style.RESET_ALL.upper()
            if symbol = "X":
              return("X" , "O")
            else:
                return("O" , "X")
            
    def player_move(board, symbol):
        move = -1
        while move not in range(1,10) or not board[move - 1].isdigit():
            try:
                move = int(input("Enter a number between 1 and 9"))
                if move not in range(1,10) or not board[move - 1].isdigit():
                except ValueError:
                print("Please enter a valid input")
        board[move - 1] = symbol

    def ai_move(board, ai_symbol, player_symbol):
        for i in range(9):
            if board[i].isdigit():
                board_copy = board.copy()
                board_copy[i] = player_symbol
                if check_win(board_copy, ai_symbol):
                    board[i] = ai_symbol
                    return
                
        for i in range(9):
            if board[i].isdigit():
                board_copy = board.copy()
                board_copy[i] = player_symbol
                if check_win(board_copy, player_symbol):
                    board[i] = ai_symbol
                    return
        possible_moves = [i for i in range(9) if board[i].isdigit()]
        move = random.choice(possible_moves)
        board[move] = ai_symbol


                            

                   
            
        
     





