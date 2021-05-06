from chess_pieces.piece import Piece

class Rook(Piece):
    def __init__(self, file: str, rank: int, fen):
        Piece.__init__(self, newFile=file, newRank=rank, newFen=fen, newSymbol="r")
        self.calc_valid_laterals()

    def calc_valid_laterals(self):
        '''
        All Files in the current rank:

            a = 97  > current file < h = 104
        '''
        tempCurrFile = 97
        while (tempCurrFile <= 104):
            if tempCurrFile != int(ord(self.file)):
                self.valid_moves.append(str(chr(tempCurrFile)) + str(self.rank))
            tempCurrFile += 1

        '''
        All ranks in current file:

            current rank > 1 and rank < 8
        '''
        tempCurrRank = 1
        while tempCurrRank <= 8:
            if tempCurrRank != self.rank:
                self.valid_moves.append(self.file + str(tempCurrRank))
            tempCurrRank += 1


    def move_to(self, newAlgebraicNotation):
        if self.is_valid_move(newAlgebraicNotation):
            # Delete current position from board
            self.fen.setFileInRankToPiece(
                rankNum=self.rank, fileLetter=self.file, piece="-")

            # Update current position to new position
            self.rank = newAlgebraicNotation[1]
            self.file = newAlgebraicNotation[0]

            # Calculate new possible moves
            self.calc_valid_laterals()

            # Write new position to board
            self.fen.setFileInRankToPiece(
                rankNum=self.rank, fileLetter=self.file, piece=self.symbol)

