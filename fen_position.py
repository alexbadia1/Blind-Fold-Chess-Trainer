import re


class FenPositon:
    def __init__(self):
        self.fen = ["8", "8", "8", "8", "8", "8", "8", "8"]
        self.hasTarget = False

    def setRank(self, rankNum, fenCode):
        length = 0

        for char in fenCode:
            # Validate for correct numbers
            if re.search(r"[1-8]", char) != None:
                length += int(char)

            # Validate for characters
            elif re.search(r"r|n|b|q|k|p", char):
                length += 1

            # Invalid character, don't modify fen at specified rank
            else:
                return False

        # Any combination of numbers and character's length must equal 8
        if(length == 8):

            # Valid fen code for rank, apply changes
            self.fen[rankNum] = fenCode

    def setFileInRankToPiece(self, rankNum, fileLetter, piece):
        if isinstance(rankNum, int) and isinstance(piece, str) and isinstance(piece, str):

            if len(fileLetter) == 1 and len(piece) == 1 and rankNum > 0 and rankNum < 9:

                # Make sure for valid piece and valid file
                if re.search(r"r|n|b|q|k|p", piece) == None or re.search(r"[a-h]", fileLetter) == None:
                    return False

                expandedFenRank = self.expandFenRank(
                    collapsedFenRank=self.fen[rankNum - 1])
                '''
                Now we can just insert a piece by directly accesing the index,
                this is easy after mapping the [a-g] to indexes [0-7]
                
                Luckily I can use ascii values for this and offset by lower case "a"s ascii value (97)
                '''
                array = []
                array[:0] = expandedFenRank
                array[ord(fileLetter.lower()) - 97] = piece

                '''
                Now, don't forget to collapse the expandedFenRank again!

                Just iterate through the temp string and replace consecutive 1's with the count instead.
                '''
                self.fen[rankNum - 1] = ""
                count = 0
                for letter in array:
                    if(letter == "1"):
                        count += 1
                    else:
                        # Add compressed number if there were zeros to compress
                        if count > 0:
                            self.fen[rankNum - 1] += str(count)

                        # Add the letter
                        self.fen[rankNum - 1] += letter
                        count = 0

                # Just encase the string ended with numbers
                self.fen[rankNum - 1] += str(count)

    def expandFenRank(self, collapsedFenRank):
        '''
        The current format of the FEN rank is for example: 
            k1p5

        To make insertion easier we'll expanding the format to:
            k1p11111
        '''
        expandedFenRank = ""
        for file in collapsedFenRank:

            if re.search(r"r|n|b|q|k|p", file) != None:
                expandedFenRank += file

            if re.search(r"[1-8]", file) != None:
                for i in range(int(file)):
                    expandedFenRank += "1"

        return expandedFenRank

    # def setFenPosition(self, stockfish):
    #     print("/".join(self.fen))
    #     stockfish.set_fen_position("/".join(self.fen))

    def toString(self):
        for rank in self.fen[::-1]:
            print(self.expandFenRank(rank).replace("1", " - ").replace("k", " k ").replace("n",
                  " n ").replace("r", " r ").replace("b", " b ").replace("q", " q ").replace("p", " p "))
