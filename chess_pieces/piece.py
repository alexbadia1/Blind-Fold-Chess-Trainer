from fen_position import FenPositon

class Piece:
    def __init__(self, newFile: str, newRank: int, newFen, newSymbol: str):
        self.file = newFile
        self.rank = newRank
        self.fen = newFen
        self.symbol = newSymbol
        self.valid_moves=[]

        self.fen.setFileInRankToPiece(rankNum=newRank, fileLetter=newFile, piece=newSymbol)
    
    def is_valid_move(self, newAlgebraicNotation):
        return newAlgebraicNotation in self.valid_moves
