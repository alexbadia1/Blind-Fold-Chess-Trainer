from chess_pieces.piece import Piece
from chess_pieces.bishop import Bishop
from chess_pieces.rook import Rook

class Queen(Bishop, Rook, Piece):
    def __init__(self, file: str, rank: int, fen):
        Piece.__init__(self, newFile=file, newRank=rank, newFen=fen, newSymbol="Q")
        self.calc_valid_laterals()
        self.calc_valid_diagonals()
    

    def move(self, nextAlgebraicPosition):
        if len(algebraicNotation) == 3:

            # Make sure a valid piece is specified, in capital letters too
            if re.search(r"R|N|B|Q|K|P", algebraicNotation[0]) != None:

                # Make sure a valid rank is specified, in lower case letters too
                if re.search(r"a|b|c|d|e|f|g", algebraicNotation[1]):

                    # Make sure a valid rank is specified
                    if re.search(r"[1-8]", algebraicNotation[2]):
                        pass