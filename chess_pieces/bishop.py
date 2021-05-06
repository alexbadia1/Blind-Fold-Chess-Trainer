from chess_pieces.piece import Piece

class Bishop(Piece):
    def __init__(self, file: str, rank: int, fen):
        Piece.__init__(self, newFile=file, newRank=rank, newFen=fen, newSymbol="b")
        self.calc_valid_diagonals()

    def calc_valid_diagonals(self):
        '''
        Move down through ranks

        Numeric boundaries for ranks:
            current rank > 1

        Numeric boundaries for files:
            a = 97
        '''
        loweringTempCurrRank = self.rank
        lTempCurrFile = int(ord(self.file))
        rTempCurrFile = int(ord(self.file))
        while loweringTempCurrRank > 1:
            loweringTempCurrRank -= 1

            if lTempCurrFile > 97:
                lTempCurrFile -= 1
                self.valid_moves.append(
                    str(chr(lTempCurrFile) + str(loweringTempCurrRank)))

            if rTempCurrFile < 104:
                rTempCurrFile += 1
                self.valid_moves.append(
                    str(chr(rTempCurrFile) + str(loweringTempCurrRank)))

        '''
        Move up through ranks

        Numeric boundaries for ranks:
            current rank < 8

        Numeric boundaries for files:
            h = 104
        '''
        risingTempCurrRank = self.rank
        lTempCurrFile = ord(self.file)
        rTempCurrFile = ord(self.file)
        while risingTempCurrRank < 8:
            risingTempCurrRank += 1
            if lTempCurrFile > 97:
                lTempCurrFile -= 1
                self.valid_moves.append(
                    str(chr(lTempCurrFile) + str(risingTempCurrRank)))

            if rTempCurrFile < 104:
                rTempCurrFile += 1
                self.valid_moves.append(
                    str(chr(rTempCurrFile) + str(risingTempCurrRank)))

    def move_to(self, newAlgebraicNotation):
        if self.is_valid_move(newAlgebraicNotation):
            # Delete current position from board
            self.fen.setFileInRankToPiece(
                rankNum=self.rank, fileLetter=self.file, piece="-")

            # Update current position to new position
            self.rank = newAlgebraicNotation[1]
            self.file = newAlgebraicNotation[0]

            # Calculate new possible moves
            self.calc_valid_diagonals()

            # Write new position to board
            self.fen.setFileInRankToPiece(
                rankNum=self.rank, fileLetter=self.file, piece=self.symbol)