import random
from fen_position import FenPositon
from stockfish import Stockfish
from chess_pieces.piece import Piece
from chess_pieces.bishop import Bishop
from chess_pieces.rook import Rook
from chess_pieces.queen import Queen

def game_mode_learn():
    stockfish = Stockfish("stockfish_13_win_32bit\stockfish_13_win_32bit\stockfish_13_win_32bit.exe")
    f = FenPositon()
    
    # Coordinates for random choice 
    ranks = [1, 2, 3, 4, 5, 6, 7, 8]
    files = ["a", "b", "c", "d", "e", "f", "g", "h"]

    # Pick a random starting coordinate
    randomFile: str = random.choice(files)
    randomRank = random.choice(ranks)
    randomStartCoordinate = randomFile + str(randomRank)
    q = Queen(file=randomFile, rank=randomRank,  fen = f)

    randomEndCoordinate = random.choice(files) + str(random.choice(ranks))

    # Find a non-matching coordinates... theoretically this could inifitely loop...
    while randomStartCoordinate == randomEndCoordinate:
        randomEndCoordinate = random.choice(files) + str(random.choice(ranks))

    # Let user try to answer the question
    answer = "w"
    while answer != "y" and answer != "n":
        print("Can the queen at Q" + randomStartCoordinate + " reach " + randomEndCoordinate + " in it's very next move?")
        print(" y.) Yes")
        print(" n.) No")
        print(" h.) See Chess Board")
        answer = input("Choose an answer: ")
        answer = answer.lower()

        if answer == "h":
            f.toString()
            print()

    # Check user answer
    if (randomEndCoordinate in q.valid_moves and answer == "y") or (randomEndCoordinate not in q.valid_moves and answer == "n"):
        print("Congratulations, you got it right!")
    else:
        print("Oof, you got it wrong!")
        print("All possible moves from " + randomStartCoordinate + " were:")
        print(q.valid_moves)
    
    playAgain = ""
    while playAgain != "y" and playAgain != "n":
        print("Play again?")
        print(" y.) Yes")
        print(" n.) No")
        playAgain = input("Choose an option: ")
        playAgain = playAgain.lower()
    
    if playAgain == "y":
        game_mode_learn()

def piece_practice(piece: str):
    run = True

    # Greet the user
    print()
    print("You chose the " + piece + "!")
    print()

    while (run):
        print("Which game mode do you want to play?")
        print(" l.) Learn")
        print(" c.) Checkpoints")
        
        choice = input("Please choose a game mode: ")

        if (choice == "l" or choice == "L"):
            game_mode_learn()
            pass
        elif (choice == "c" or choice == "C"):
            pass
        else:
            print("Please select a game mode from the menu.")

def choose_practice():
    run = True

    # Greet the user
    print()
    print("Welcome to the practice ground!")
    print()

    while (run):
        print("Which peace do you want to practice with?")
        print(" k.) King")
        print(" q.) Queen")
        print(" b.) Bishop")
        print(" n.) Knight")
        print(" r.) Rook")
        print(" p.) Pawn")
        choice = input("Please choose a peace: ")

        if (choice == "k"):
            print('King Practice Coming Soon!')
            pass
        elif (choice == "q" or choice == "Q"):
            piece_practice("Queen")
            pass
        elif (choice == "b" or choice == "B"):
            pass
        elif (choice == "n" or choice == "N"):
            print('Knight Practice Coming Soon!')
            pass
        elif (choice == "r" or choice == "R"):
            pass
        elif (choice == "p" or choice == "P"):
            print('Pawn Practice Coming Soon!')
            pass
        else:
            print("Please select an activity from the menu.")

def menu():
    run = True

    # Greet the user
    print()
    print("Welcome to the Blindfold Chess Trainer!")
    print()

    while (run):
        print("What do you want to train today?")
        print(" a.) Practice")
        print(" b.) Game")
        print(" c.) Settings")
        print(" h.) Help")
        print(" q.) Quit")
        choice = input("Choose a menu option: ")

        if (choice == "A" or choice == "a"):
            choose_practice()
        elif(choice == "B" or choice == "b"):
            print("Blindfold Games With Stockfish Coming Soon!")
            pass
        elif(choice == "C" or choice == "c"):
            print('Not yet implemented!')
            pass
        elif(choice == "D" or choice == "d"):
            print('Not yet implemented!')
            pass
        elif(choice == "Q" or choice == "q"):
            raise SystemExit
        else:
            print("Please select a choice from the menu.")

def main():
    stockfish = Stockfish("stockfish_13_win_32bit\stockfish_13_win_32bit\stockfish_13_win_32bit.exe")
    menu()
    # fenPosition = FenPositon()

    # b = Bishop(rank=1, file="h", fen = fenPosition)
    # print("Bishop: ")
    # print(b.valid_moves)

    # r = Rook(rank=1, file="h", fen = fenPosition)
    # print("Rook: ")
    # print(r.valid_moves)

    # q = Queen(rank=4, file="e", fen = fenPosition)
    # print("Quuen: ")
    # print(q.valid_moves)

    # fenPosition.toString()

main()
