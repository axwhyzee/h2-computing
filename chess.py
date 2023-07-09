from typing import List, Literal

'''
Assume following setting:

    0 1 2 3 4 5 6 7 
0  [ White lower rank ]
1  [ White upper rank ]
2  
3 
4
5
6  [ Black upper rank ]
7  [ Black lower rank ]
'''

AXIS_TYPE_HINT = Literal[0,1,2,3,4,5,6,7]

class Board:
    def __init__(self):
        self.__board = [[None for _ in range(8)] for _ in range(8)]
    
    def get_piece_at_pos(
        self, 
        x: AXIS_TYPE_HINT, 
        y: AXIS_TYPE_HINT
    ) -> "Piece":
        return self.__board[x][y]
    
    def display(self):
        for row in self.__board:
            print(' | '.join(row))

class Piece:
    def __init__(
        self, 
        x: AXIS_TYPE_HINT, 
        y: AXIS_TYPE_HINT, 
        color: Literal['w', 'b'], 
        board: "Board"
    ):
        self.__x = x
        self.__y = y
        self.__color = color
        self.__id = f'{color}-{x}-{y}'    
        self.__board = board    

    def is_move_valid(
        self, 
        x: AXIS_TYPE_HINT, 
        y: AXIS_TYPE_HINT
    ) -> bool:
        return True

    def move_to(
        self, 
        x: AXIS_TYPE_HINT, 
        y: AXIS_TYPE_HINT
    ) -> bool:
        if self.is_move_valid(x, y):
            self.__x = x
            self.__y = y

    def __str__(self):
        return self.__id

class Pawn(Piece):
    def is_move_valid(
        self, 
        x: AXIS_TYPE_HINT, 
        y: AXIS_TYPE_HINT
    ) -> bool:
        if self.__color == 'w':
            # first move from original pos. Can be 1 or 2 spaces down
            if self.__y == 1 and x == self.__x and y - self.__y == 2:
                return self.__board.get_piece_at_pos(x, y-1) == None
            elif y - self.__y == 1 and abs(x - self.__x) == 1 and self.__board.get_piece_at_pos(x, y).__color != self.__color:
                return True
            elif y - self.__y == 1 and x == self.__x:
                item = self.__board.get_piece_at_pos(x, y)
                if not item or item.__color != self.__color:
                    return True
        elif self.__color == 'w':
            # first move from original pos. Can be 1 or 2 spaces down
            if self.__y == 1 and x == self.__x and y - self.__y == 2:
                return self.__board.get_piece_at_pos(x, y-1) == None
            elif y - self.__y == 1 and abs(x - self.__x) == 1 and self.__board.get_piece_at_pos(x, y).__color != self.__color:
                return True
            elif y - self.__y == 1 and x == self.__x:
                item = self.__board.get_piece_at_pos(x, y)
                if not item or item.__color != self.__color:
                    return True
        
        return False