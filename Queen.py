from stockfish import Stockfish

class QueenPractice:
    def __init__(self, currentAlgebraicPosition, stockfish):
        self.currentAlgebraicPosition = currentAlgebraicPosition
        self.stockfish = stockfish
    
    def move(self, nextAlgebraicPosition):
        if len(algebraicNotation) == 3:
            
            # Make sure a valid piece is specified, in capital letters too
            if re.search(r"R|N|B|Q|K|P", algebraicNotation[0]) != None:
                
                # Make sure a valid rank is specified, in lower case letters too
                if re.search(r"a|b|c|d|e|f|g", algebraicNotation[1]):
                   
                    # Make sure a valid rank is specified
                    if re.search(r"[1-8]", algebraicNotation[2]):
                        
                        # Make sure move if legal
                        if self.stockfish.is_move_correct(self.currentAlgebraicPosition + nextAlgebraicPosition):
                            
                            # Make move
                            # self.stockfish.set_position()

        