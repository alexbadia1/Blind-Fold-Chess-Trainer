# Blind-Fold-Chess-Trainer
Can you create a mental image of the chess board by just only reading chess notation?!

## Getting Started

Currently this is a command line, menu driven program. As I get more time, I plan to convert this to 
GUI based application with more features.

The opening command line menu is:
  - Learn 
  - Play
  - Settings
  - Help
  - Quit

### Learn

The goal of learning is to provide excersises that will help beginners build there skills in creating a mental image of the board.
Specifically, excersises such as:
  - Empty board valid move questions (currently, only implemented for the queen)
  - Capture the flag, via chess notation (Not yet implemented)
  - Shortest path to a certain sqaure, given a piece and its legal moves (Not yet implemented)
  - etc.

### Play

Play a match against stockfish by only typing in chess notation and receiving chess notation.
The user may peek the board, if they get lost, or see a list of the moves written in chess notation.

### Blindfold Openings

Not yet implmented

- Try to guess openings and their variations by only looking at chess notation, keeping in mind that many openings transpose into each other.
- Write chess notation for a given opening, X moves deep.

### Blindfold Puzzles

Not yet implemented

Shown, visually a starting position, and told a series of moves, can you answers questions like:

  - Is a specific piece hanging?
  - What two pieces are being forked (if any)?
  - Is this specific piece pinned?
  - Is, for example, Nc6 a valid move in the new position?
  - Can a certain piece be captured?
  - etc.


## Installation

Blind-Fold-Chess-Trainer is built using python, to install Python go to https://www.python.org/.

During the python installation process, set Python to the computers path variables.
  - This should be an option in the setup wizard
  - This can be done manually.

Once Python is installed, download the stockfish python package: `pip install stockfish`

Stockfish is a well known chess engine (as you probably know if you're cloning this). This package
lets the user play against the stockfish engine by creating a subprocess to communicate with the Stockfish engine
via the command line.

Communication with Stockfish is done through the Universal Chess Interface which is described in great detail here: https://github.com/official-stockfish/Stockfish

## Built With

- IDE: Visual Code Studio
- Language(s): Python
- Package(s): stockfish 3.14.0

## Authors
- Alex Badia
