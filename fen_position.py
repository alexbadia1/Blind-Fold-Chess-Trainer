import re

class FenPositon:
    def __init__(self):
        self.fen = ["8", "8", "8", "8", "8", "8", "8", "8"]
    
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

            if len(fileLetter) == 1 and len(piece) == 1:

                # Make sure for valid piece and valid file
                if re.search(r"r|n|b|q|k|p", piece) == None or re.search(r"[a-h]", fileLetter) == None:
                    return False
                
                '''
                The current format of the FEN rank is for example: 
                    k1p5

                To make insertion easier we'll expanding the format to:
                    k1p11111
                '''
                tempFenRank = ""
                for file in self.fen[rankNum]:

                    if re.search(r"r|n|b|q|k|p", file) != None:
                        tempFenRank += file

                    if re.search(r"[1-8]", file) != None:
                        for i in range(int(file)):
                            tempFenRank += "1"
                
                '''
                Now we can just insert a piece by directly accesing the index,
                this is easy after mapping the [a-g] to indexes [0-7]
                
                Luckily I can use ascii values for this and offset by lower case "a"s ascii value (97)
                '''
                array = []
                array[:0] = tempFenRank
                array[ord(fileLetter.lower()) - 97] = piece

                '''
                Now, don't forget to collapse the tempFenRankString again!

                Just iterate through the temp string and replace consecutive 1's with the count instead.
                '''
                self.fen[rankNum] = ""
                count = 0
                for letter in array:
                    if(letter == "1"):
                        count += 1
                    else:
                        # Add compressed number if there were zeros to compress
                        if count > 0:
                            self.fen[rankNum] += str(count)
                        
                        # Add the letter
                        self.fen[rankNum] += letter
                        count = 0
                
                # Just encase the string ended with numbers
                self.fen[rankNum] += str(count)
                
    def setFenPosition(self, stockfish):
        print("/".join(self.fen))
        stockfish.set_fen_position("/".join(self.fen))

       

            

