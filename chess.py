from typing import List, Literal, Tuple, Optional

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
        self.kings = {}
        board = [[None for _ in range(8)] for _ in range(8)]
        for side in [0, 1]:
            upper_rank = 6 - side * 5
            lower_rank = 7 - side * 7
            for col in range(8):
                board[upper_rank][col] = Pawn(col, upper_rank, self)
    
            # rook
            board[lower_rank][0] = Rook(0, lower_rank, self)
            board[lower_rank][7] = Rook(7, lower_rank, self)

            # knight
            board[lower_rank][1] = Knight(1, lower_rank, self)
            board[lower_rank][6] = Knight(6, lower_rank, self)

            # bishop
            board[lower_rank][2] = Bishop(2, lower_rank, self)
            board[lower_rank][5] = Bishop(5, lower_rank, self)

            # queen & king
            board[lower_rank][3] = Queen(3, lower_rank, self)
            king = King(4, lower_rank, self)
            board[lower_rank][4] = king
            self.kings[king.color] = king

        self.board = board
    
    def get_at_pos(
        self, 
        x: AXIS, 
        y: AXIS
    ) -> "Piece":
        return self.board[y][x]
    
    def move_piece(
        self, 
        x: AXIS,
        y: AXIS,
        piece: "Piece"
    ) -> bool:
        if (x, y) in piece.get_valid_moves():
            self.board[piece.y][piece.x] = None
            piece.x = x
            piece.y = y
            occupant = self.board[y][x]
            if occupant:
                occupant.captured = True
            self.board[y][x] = piece
            return True
        return False
    
    def display(self):
        print('  ', end='')
        for i in range(1, 9):
            print('| {: <10}'.format(i), end='')
        print()
        for i, row in enumerate(self.board):
            print(i+1, end=' ')
            for col in row:
                print('| {: <10}'.format(str(col) if col else ''), end='')
            print()
        print()

class Piece:
    def __init__(
        self, 
        x: AXIS, 
        y: AXIS,
        board: "Board",
        name: str
    ):
        self.x = x
        self.y = y
        self.color = 'b' if y > 5 else 'w'
        self.board = board
        self.name = name
        self.captured = False

    def get_valid_moves(self) -> List[Tuple[AXIS, AXIS]]:
        return []

    def peek(
        self, 
        x: AXIS, 
        y: AXIS
    ) -> "Piece":
        return self.board.get_at_pos(x, y)

    def __str__(self):
        return f'{self.name}-{self.color}-{self.x}'

class Pawn(Piece):
    def __init__(
        self, 
        x: AXIS,
        y: AXIS,
        board: "Board"
    ):
        super().__init__(x, y, board, 'Pawn')
        self.start_y = self.y
        
    def get_valid_moves(self) -> List[Tuple[AXIS, AXIS]]:
        direction = 1 if self.color == 'w' else -1
        moves = []
        
        if not 0 <= self.y + direction <= 7:
            return []
            
        is_blocked = self.peek(self.x, self.y+direction) != None
        
        if not is_blocked:
            moves.append((self.x, self.y + direction))

            # first pawn move can be 2 steps
            if self.y == self.start_y:
                y_fwd_fwd = self.y + 2* direction
                if 0 <= (y_fwd_fwd) <= 7 and not self.peek(self.x, y_fwd_fwd):
                    moves.append((self.x, y_fwd_fwd))

        y_fwd = self.y + direction
        front_left = self.peek(self.x-1, y_fwd) 
        front_right = self.peek(self.x+1, y_fwd)
        
        if front_left and front_left.color != self.color:
            moves.append((self.x-1, y_fwd))
        if front_right and front_right.color != self.color:
            moves.append((self.x+1, y_fwd))
        return moves

class Rook(Piece):
    def __init__(
        self, 
        x: AXIS,
        y: AXIS,
        board: "Board"
    ):
        super().__init__(x, y, board, 'Rook')
        
    def get_valid_moves(self) -> List[Tuple[AXIS, AXIS]]:
        moves = []
        
        # horizontal
        for steps in [
            list(range(self.x-1, -1, -1)), 
            list(range(self.x+1, 8))
        ]:
            for col in steps:
                obstacle = self.peek(col, self.y)
                if obstacle:
                    if obstacle.color != self.color:
                        moves.append((col, self.y))
                    break
                moves.append((col, self.y))
        # vertical
        for steps in [
            list(range(self.y-1, -1, -1)), 
            list(range(self.y+1, 8))
        ]:
            for row in steps:
                obstacle = self.peek(self.x, row)
                if obstacle:
                    if obstacle.color != self.color:
                        moves.append((self.x, row))
                    break
                moves.append((self.x, row))
        return moves
        
class Knight(Piece):
    def __init__(
        self, 
        x: AXIS,
        y: AXIS,
        board: "Board"
    ):
        super().__init__(x, y, board, 'Knight')
        
    def get_valid_moves(self) -> List[Tuple[AXIS, AXIS]]:
        dy = [-1, -1, 1, 1, -2, 2, -2, 2]
        dx = [-2, 2, -2, 2, 1, 1, -1, -1]
        moves = []
        
        for i in range(len(dy)):
            new_x = self.x + dx[i]
            new_y = self.y + dy[i]
            
            if 0 <= new_x <= 7 and 0 <= new_y <= 7:       
                occupant = self.peek(new_x, new_y)
                if occupant and occupant.color == self.color:
                    continue
                moves.append((new_x, new_y))
        return moves
    
class Bishop(Piece):
    def __init__(
        self, 
        x: AXIS,
        y: AXIS,
        board: "Board"
    ):
        super().__init__(x, y, board, 'Bishop')
    
    def get_valid_moves(self) -> List[Tuple[AXIS, AXIS]]:
        moves = []

        # diagonal
        max_nw = min(self.x, self.y)
        max_se = 7 - max(self.x, self.y)
        max_ne = min(7 - self.x, self.y)
        max_sw = min(self.x, 7 - self.y)

        # NW - SE
        for steps in [
            [_ for _ in range(-1, -max_nw-1, -1)],
            [_ for _ in range(1, max_se+1)]
        ]:
            for diag in steps:
                if diag == 0:
                    continue
                
                new_x, new_y = self.x + diag, self.y + diag
                obstacle = self.peek(new_x, new_y)
                if obstacle:
                    if obstacle.color != self.color:
                        moves.append((new_x, new_y))
                    break
                moves.append((new_x, new_y))
        # NE - SW
        for steps in [
            [_ for _ in range(-1, -max_sw-1, -1)],
            [_ for _ in range(1, max_ne+1)]
        ]:
            for diag in steps:
                if diag == 0:
                    continue
                
                new_x, new_y = self.x + diag, self.y - diag
                obstacle = self.peek(new_x, new_y)
                if obstacle:
                    if obstacle.color != self.color:
                        moves.append((new_x, new_y))
                    break
                moves.append((new_x, new_y))
        return moves
            
class King(Piece):
    def __init__(
        self, 
        x: AXIS,
        y: AXIS,
        board: "Board"
    ):
        super().__init__(x, y, board, 'King')
    
    def get_valid_moves(self) -> List[Tuple[AXIS, AXIS]]:
        moves = []
        dxy = [-1, 0, 1]
        for dx in dxy:
            for dy in dxy:
                if dx == dy == 0:
                    continue 
                
                new_x, new_y = self.x + dx, self.y + dy
                if 0 <= new_x <= 7 and 0 <= new_y <= 7:
                    occupant = self.peek(new_x, new_y)
                    if not occupant or occupant.color != self.color:
                        moves.append((new_x, new_y))
        return moves
    
class Queen(Piece):
    def __init__(
        self, 
        x: AXIS,
        y: AXIS,
        board: "Board"
    ):
        super().__init__(x, y, board, 'Queen')
    
    def get_valid_moves(self) -> List[Tuple[AXIS, AXIS]]:
        moves = []
        
        # horizontal
        for steps in [
            list(range(self.x-1, -1, -1)), 
            list(range(self.x+1, 8))
        ]:
            for col in steps:
                obstacle = self.peek(col, self.y)
                if obstacle:
                    if obstacle.color != self.color:
                        moves.append((col, self.y))
                    break
                moves.append((col, self.y))
        # vertical
        for steps in [
            list(range(self.y-1, -1, -1)), 
            list(range(self.y+1, 8))
        ]:
            for row in steps:
                obstacle = self.peek(self.x, row)
                if obstacle:
                    if obstacle.color != self.color:
                        moves.append((self.x, row))
                    break
                moves.append((self.x, row))

        # diagonal
        max_nw = min(self.x, self.y)
        max_se = 7 - max(self.x, self.y)
        max_ne = min(7 - self.x, self.y)
        max_sw = min(self.x, 7 - self.y)

        # NW - SE
        for steps in [
            [_ for _ in range(-1, -max_nw-1, -1)],
            [_ for _ in range(1, max_se+1)]
        ]:
            for diag in steps:
                if diag == 0:
                    continue
                
                new_x, new_y = self.x + diag, self.y + diag
                obstacle = self.peek(new_x, new_y)
                if obstacle:
                    if obstacle.color != self.color:
                        moves.append((new_x, new_y))
                    break
                moves.append((new_x, new_y))
        # NE - SW
        for steps in [
            [_ for _ in range(-1, -max_sw-1, -1)],
            [_ for _ in range(1, max_ne+1)]
        ]:
            for diag in steps:
                if diag == 0:
                    continue
                
                new_x, new_y = self.x + diag, self.y - diag
                obstacle = self.peek(new_x, new_y)
                if obstacle:
                    if obstacle.color != self.color:
                        moves.append((new_x, new_y))
                    break
                moves.append((new_x, new_y))
        return moves
    

def validate_input(s: str, board: Board, color: Optional[str]) -> str:
    try:
        x, y = s.split()
    except:
        return 'Invalid input format. Please enter 2 space separated digits.'
    
    for val in [x, y]:
        if not val.isdigit():
            return 'Do not provide non-integers'
        if not 1 <= int(val) <= 8:
            return 'Invalid input value. Value out of range. Values should be from 1 to 8, inclusive.'
    
    if color:
        piece = board.get_at_pos(int(x)-1, int(y)-1)
        if not piece:
            return 'No chess piece at the given coordinate.' 
        if piece.color != color:
            return 'You cannot move your opponent\'s piece'
        if not piece.get_valid_moves():
            return 'This piece has no valid moves. Choose another piece'

def get_coords_input(board: Board, color: Optional[str] = None) -> Tuple[AXIS, AXIS]:
    while 1:
        s = input('[X Y]: ')
        error = validate_input(s, board, color)
        if error:
            print(error)
        else:
            return list(map(lambda c:int(c)-1, s.split()))
    

def start_game():
    b = Board()
    colors = {1: 'w', 2: 'b'}
    w_king = b
    player = 1
    print('Please enter all coordinates as space seperated integers from 1 to 8, inclusive. E.g., 3 6\n')
    b.display()

    while 1:
        col = colors[player]

        print('=================')
        print(f'Player ({col})\'s turn')
        print('=================')
        print()
        print('+-----------+')
        print('|  To move  |')
        print('+-----------+')
        x, y = get_coords_input(b, col)
        piece = b.get_at_pos(x, y)

        print()
        print('+------------------+')
        print('|  Target location |')
        print('+------------------+')
        print(f'{str(piece)}\'s valid moves:')
        for (x, y) in piece.get_valid_moves():
            print('>', x+1, y+1, b.get_at_pos(x, y) or '')
        while 1:
            x, y = get_coords_input(b)
            if b.move_piece(x, y, piece):
                break
            else:
                print('Invalid move')

        b.display()

        # switch player
        # toggle from 1 -> 2, 2 -> 1
        player = 3 - player

        if b.kings[colors[player]].captured:
            print(f'Player ({col}) won!')
            break
        
start_game()