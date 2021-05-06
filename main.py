from fen_position import FenPositon
from stockfish import Stockfish

def menu():
    run = True

    print("Welcome to the Blindfold Chess Trainer!")

    while (run):
        choice = input("""
        Menu:
            a.) Practice
            b.) Match
            b.) Settings
            c.) Help
            q.) Quit 
        
        Menu choice: """)

        if (choice == "A"):
            pass
        elif(choice == "B" or choice == "b"):
            pass
        elif(choice == "C" or choice == "c"):
            pass
        elif(choice == "D" or choice == "d"):
            pass
        elif(choice == "Q" or choice == "q"):
            raise SystemExit
        else:
            print("Please select a choice from the menu.")

def main():
    stockfish = Stockfish("stockfish_13_win_32bit\stockfish_13_win_32bit\stockfish_13_win_32bit.exe")
    # fenPosition = FenPositon()
    # fenPosition.setFileInRankToPiece(rankNum = 1, fileLetter = "a", piece = "k")
    # fenPosition.setFenPosition(stockfish = stockfish)
    stockfish.set_fen_position('k7/8/8/8/8/8/8/K7')
    # print(stockfish.is_move_correct('a6b6'))
    print(stockfish.get_board_visual())

    # menu()

main()
