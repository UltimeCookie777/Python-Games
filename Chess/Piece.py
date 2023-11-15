

class Piece:
    def __init__(self, startingPosition : tuple[int,int], color_ : int) -> None:
        """Parent of all pieces. 

        Args:
            startingPosition (tuple): (x,y) starting position
            color_ (int): 1 = white, 0 = black
        """
        self.pos = startingPosition
        self.color= color_
    
    def getMoves(self) -> list[tuple[int,int]]:
        """Returns a list of tuples with all available moves.

        Returns:
            list: list of tuples (x,y)
        """
        return []
    
    def move(self, board : list[list[tuple]], targetPos : tuple[int,int]) -> list[tuple]:
        
        """If the position is valid, delete the old pos and set the new ones.

        Returns:
            _type_: _description_
        """
        
        if targetPos in self.getMoves():
            x,y = targetPos
            x_,y_ = self.pos
            self.pos=(x,y)
            board[x][y], board[x_][y_] = board[x_][y_], ""
        
        return board
    
class NonePiece(Piece):
    
    def __init__(self, startingPosition: tuple, color_: int) -> None:
        super().__init__(startingPosition, color_)
        
    def getMoves(self) -> list:
        return []
    
    def move(self, board: list[list[Piece]], targetPos: tuple) -> list[tuple]:
        return super().move(board, targetPos)
    
class pawn(Piece):
    
    def __init__(self, startingPosition: tuple, color_: int) -> None:
        super().__init__(startingPosition, color_)
        
    def getMoves(self) -> list:
        
        x,y = self.pos
        
        if self.color==1:
            return [(x-1,y+1),(x+1,y+1)]
        else:
            return [(x-1,y-1),(x+1,y-1)]
        