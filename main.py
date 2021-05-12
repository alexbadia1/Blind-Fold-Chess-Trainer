import random
from fen_position import FenPositon
from stockfish import Stockfish
from chess_pieces.piece import Piece
from chess_pieces.bishop import Bishop
from chess_pieces.rook import Rook
from chess_pieces.queen import Queen
from menu import Menu
from menu import MenuItem

def game_mode_learn(chessPiece: Piece):
    # Initialize any empty chess board, using Forsyth-Edwards Notation
    fen = FenPositon()
    
    # Coordinates for random choice
    ranks = [1, 2, 3, 4, 5, 6, 7, 8]
    files = ["a", "b", "c", "d", "e", "f", "g", "h"]

    # Pick a random starting coordinate
    randomStartRank: int = random.choice(ranks)
    randomStartFile: str = random.choice(files)
    randomStartCoordinate = randomStartFile + str(randomStartRank)

    # Create a queen and put her on the chess board at the random start coordinate
    chessPiece = Piece(
        file = randomStartFile,
        rank = randomStartRank,
        fen = fen
    )

    # Remove the start rank to prevent a duplicate random end coordinate
    ranks = ranks.remove(randomStartRank)
    randomEndRank: int = random.choice(ranks)
    randomEndFile: str = random.choice(files)
    randomEndCoordinate = random.choice(randomEndFile) + str(randomEndRank)

    # Let user try to answer the question
    answer = "?"
    while answer != "y" and answer != "n":
        print("\nGiven an empty board, is " + chessPiece.symbol + randomStartCoordinate + " to " + chessPiece.symbol + randomEndCoordinate + " a legal next move?")
        print(" Y.) Yes")
        print(" N.) No")
        print(" H.) See Chess Board")
        answer = input("Choose an answer: ")
        answer = answer.lower()

        # User chose h, show board
        if answer == "h":
            fen.toString()
            print()

    # Check user answer
    if (randomEndCoordinate in chessPiece.valid_moves and answer == "y") or (randomEndCoordinate not in chessPiece.valid_moves and answer == "n"):
        print("Congratulations, you got it right!")
    else:
        print("Oof, you got it wrong!")
        print("All possible moves from " + randomStartCoordinate + " were:")
        print(chessPiece.valid_moves)
    
    # Ask user to play again?
    playAgain = "?"
    while playAgain != "y" and playAgain != "n":
        print("Play again?")
        print(" Y.) Yes")
        print(" N.) No")
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

def practice():
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

def unimplemented():
    print("This feature is unimplemented!")

def newMenu():
    maimMenu = Menu(greeting = "What do you want to train today?")
    maimMenu.addMenuItem("P", MenuItem(newKey = "P", newDescription = "Practice", newFunction = practice))
    maimMenu.addMenuItem("G", MenuItem(newKey = "G", newDescription = "Game", newFunction = unimplemented))
    maimMenu.addMenuItem("S", MenuItem(newKey = "S", newDescription = "Settings", newFunction = unimplemented))
    maimMenu.addMenuItem("H", MenuItem(newKey = "H", newDescription = "Help", newFunction = unimplemented))
    maimMenu.addMenuItem("Q", MenuItem(newKey = "Q", newDescription = "Quit", newFunction = unimplemented))
    maimMenu.getUserChoice()

def main():
    newMenu()

main()
