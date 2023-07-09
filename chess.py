from typing import List, Literal,Tuple

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

AXIS = Literal[0,1,2,3,4,5,6,7]

class Board:
    def __init__(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        for side in [0, 1]:
            upper_rank = 6 - side * 5
            lower_rank = 7 - side * 7
            for col in range(8):
                board[upper_rank][col] = Pawn(upper_rank, col, self)
    
        # rook
        board[lower_rank][0] = Rook(lower_rank, 0, self)
        board[lower_rank][7] = Rook(lower_rank, 7, self)

        # knight
        board[lower_rank][1] = Knight(lower_rank, 1, self)
        board[lower_rank][6] = Knight(lower_rank, 6, self)

        # bishop
        board[lower_rank][2] = Knight(lower_rank, 2, self)
        board[lower_rank][5] = Knight(lower_rank, 5, self)

        # queen & king
        board[lower_rank][3] = Queen(lower_rank, 3, self)
        board[lower_rank][4] = King(lower_rank, 4, self)

        self.__board = board
    
    def get_at_pos(
        self, 
        x: AXIS, 
        y: AXIS
    ) -> "Piece":
        return self.__board[x][y]
    
    def display(self):
        for row in self.__board:
            print(' | '.join(row))

class Piece:
    def __init__(
        self, 
        x: AXIS, 
        y: AXIS,
        board: "Board",
        name: str
    ):
        self.__x = x
        self.__y = y
        self.__color = 'b' if y > 5 else 'w'
        self.__board = board
        self.__name = name

    def get_valid_moves(self) -> List[Tuple[AXIS, AXIS]]:
        return []

    def peek(
        self, 
        x: AXIS, 
        y: AXIS
    ) -> "Piece":
        return self.__board.get_at_pos(x, y)
        
    def move_to(
        self, 
        x: AXIS, 
        y: AXIS
    ) -> bool:
        if (x, y) in self.get_valid_moves():
            self.__x = x
            self.__y = y
            return True
        return False

    def __str__(self):
        return f'{name}-{color}-{x}'

class Pawn(Piece):
    def __init__(
        self, 
        x: AXIS,
        y: AXIS,
        board: "Board"
    ):
        super.__init__(x, y, board, 'Pawn')
        
    def get_valid_moves(self) -> List[Tuple[AXIS, AXIS]]:
        direction = 1 if self.__colour == 'w' else -1
        moves = []
        
        if not 0 <= self.y + direction <= 7:
            return []
            
        is_blocked = self.peek(self.x, self,y+direction) != None
        
        if not is_blocked:
            moves.append((self.x, self.y + direction))
            if 0 <= (self.y + 2*direction) <= 7:
                moves.append((self.x, self.y + 2*direction))

        y_fwd = self.y + direction
        front_left = self.peek(self.x-1, y_fwd) 
        front_right = self.peek(self.x+1, y_fwd)
        
        if not front_left or front_left.__color != self.__color:
            moves.append((self.x-1, y_fwd))
        if not front_right or front_right.__color != self.__color:
            moves.append((self.x+1, y_fwd))
        return moves

class Rook(Piece):
    def __init__(
        self, 
        x: AXIS,
        y: AXIS,
        board: "Board"
    ):
        super.__init__(x, y, board, 'Rook')
        
    def get_valid_moves(self) -> List[Tuple[AXIS, AXIS]]:
        moves = []
        
        # horizontal
        for col in range(8):
            if col == self.__x:
                continue
            obstacle = self.peek(col, self.__y)
            if obstacle:
                if obstacle.__color != self.__color:
                    moves.append((col, self.__y))
                break
                
        # vertical
        for row in range(8):
            if row == self.__y:
                continue
            obstacle = self.peek(self.__x, row)
            if obstacle:
                if obstacle.__color != self.__color:
                    moves.append((self.__x, row))
                break
         return moves
        
class Knight(Piece):
    def __init__(
        self, 
        x: AXIS,
        y: AXIS,
        board: "Board"
    ):
        super.__init__(x, y, board, 'Knight')
        
    def get_valid_moves(self) -> List[Tuple[AXIS, AXIS]]:
        dy = [-1, -1, 1, 1, -2, 2, -2, 2]
        dx = [-2, 2, -2, 2, 1, 1, -1, -1]
        moves = []
        
        for i in range(len(dy)):
            new_x = self.__x + dx[i]
            new_y = sslf.__y + dy[i]
            
            if 0 <= new_x <= 7 and 0 <= new_y <= 7:       
                occupant = self.peek(new_x, new_y)
                if occupant and occupant.__color == self.__color:
                    continue
                moves.append((new_x, new_y))
         return moves
            

    
