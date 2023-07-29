import math
from typing import List, Tuple

from utils import get_perimeter_x


"""Constants. Do not edit."""

RED = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'


"""Helper functions. Do not edit."""

def get_perimeter_x(y: int, radius: float, center_x: int, center_y: int) -> Tuple[float, float]:
    """
    Helper function to calculate X value of a circle's perimeter given Y value and radius. 
    
    Parameters
    ----------
    y : int
        Y coordinate of a point
    radius: float
        Radius of circle
    center_x : int
        X coordinate of circle center
    center_y: int
        Y coordinate of circle center

    Returns
    -------
    Tuple[float, float]
        2 posisble X coordinates of point if it lies within the circle, else raise ValueError

    Raises
    ------
    ValueError
        If point lies outside of circle
    """

    if y > center_y + radius or y < center_y - radius:
        raise ValueError(f'Point lies outside of circle. Y coordinate should be within {center_y - radius} to {center_y + radius}')

    x_minus_h = (radius**2 - (y-center_y)**2)**0.5
    return (center_x - x_minus_h, center_x + x_minus_h)


def display_grid(height: int, width: int, pokemons: List["Pokemon"], players: List["Player"]):
    """
    Display a grid with Pokemons and Players in it

    Parameters
    ----------
    height : int
        Height of grid
    width : int
        Width of grid
    pokemons : List[Pokemon]
        List of Pokemon instances
    players : List[Player]
        List of Player instances
    """

    locs = {}
    for p in pokemons:
        locs[p.get_pos()] = p.get_symbol()

    for p in players:
        px, py = p.get_pos()
        r = p.get_lvl()
        locs[(px, py)] = GREEN + p.get_symbol() + ENDC
        
        if isinstance(p, PremiumPlayer):
            prev_x_left = None
            prev_x_right = None

            for y in range(max(0, py-r), min(py+r+1, height)):
                x_left, x_right = get_perimeter_x(y, r, px, py)
                x_left = math.ceil(x_left)
                x_right = math.floor(x_right)
                coords_left = (x_left, y)
                coords_right = (x_right, y)

                locs[coords_left] = GREEN + locs.get(coords_left, '*') + ENDC
                locs[coords_right] = GREEN + locs.get(coords_right, '*') + ENDC

                temp_x_left, temp_x_right = prev_x_left, prev_x_right
                prev_x_left = x_left
                prev_x_right = x_right

                if temp_x_left != None and temp_x_right != None:
                    if x_left - temp_x_left > 1:
                        iy = y-1
                    elif temp_x_left - x_left > 1:
                        iy = y
                    else:
                        continue

                    for ixl in range(min(temp_x_left, x_left)+1, max(temp_x_left, x_left)):
                        locs[(ixl, iy)] = GREEN + locs.get((ixl, iy), '*') + ENDC
                    for ixr in range(min(temp_x_right, x_right)+1, max(temp_x_right, x_right)):
                        locs[(ixr, iy)] = GREEN + locs.get((ixr, iy), '*') + ENDC

        elif isinstance(p, NonPremiumPlayer):
            for y in range(max(0, py - r), min(py + r + 1, height)):
                coord_left = (px - r, y)
                coord_right = (px + r, y)
                locs[coord_left] = GREEN + locs.get(coord_left, '*') + ENDC
                locs[coord_right] = GREEN + locs.get(coord_right, '*') + ENDC
            for x in range(max(0, px - r), min(px + r, width)):
                coord_top = (x, py-r)
                coord_btm = (x, py+r)
                locs[coord_top] = GREEN + locs.get(coord_top, '*') + ENDC
                locs[coord_btm] = GREEN + locs.get(coord_btm, '*') + ENDC

    for y in range(height):
        for x in range(width):
            print(f'{locs.get((x,y), ".")} ', end='')
        print()


class Entity:
    def __init__(self, x: int, y: int, symbol: str, is_player: bool):
        """
        Parameters
        ----------
        x : int
            X coordinate
        y : int
            Y coordinate
        symbol : str 
            Single character representation of this entity, to be displayed on the grid
        is_player : bool
            True if entity is a player. False is entity is a pokemon
        """
        self.__x = x
        self.__y = y
        self.__symbol = symbol
        self.__is_player = is_player


    def is_player(self) -> bool:
        """Returns whether entity is player or not"""
        return self.__is_player


    def get_pos(self) -> Tuple[int, int]:
        """Get position (x, y coordinates) of entity"""
        return self.__x, self.__y
    

    def get_symbol(self) -> str:
        """Get entity symbol"""
        return self.__symbol


class Pokemon(Entity):
    def __init__(self, x: int, y: int, symbol: str):
        """
        Parameters
        ----------
        x : int
            X coordinate
        y : int
            Y coordinate
        symbol : str 
            Single character representation of this entity, to be displayed on the grid
        """
        super().__init__(x, y, symbol, False)

    
    def __str__(self) -> str:
        x, y = self.get_pos()
        return f"Pokemon {self.get_symbol()} @ (x={x}, y={y})"


class Player(Entity):
    def __init__(self, x: int, y: int, symbol: str, lvl: int, premium: bool):
        """
        Parameters
        ----------
        x : int
            X coordinate
        y : int
            Y coordinate
        symbol : str 
            Single character representation of this entity, to be displayed on the grid
        lvl : int 
            Player level. Used in calculation of field of vision to determine which Pokemons are available for catching
        premium : bool
            Whether player is premium player
        """

        #######################
        ##   YOUR CODE HERE  ##
        #######################

        pass

    
    def get_lvl(self) -> int:
        """
        Getter method for Player's level
        
        Returns
        -------
        int 
            Player's level
        """

        #######################
        ##   YOUR CODE HERE  ##
        #######################

        pass

    
    def get_available_pokemons(self, pokemons: List["Pokemon"]) -> List["Pokemon"]:
        """
        Get list of Pokemon instances that lie within a Player's field of vision.
        This method is empty here because it will be overriden in the subclasses.

        Parameters
        ----------
        pokemons : List[Pokemon]
            List of Pokemon instances
        
        Returns
        -------
        List[Pokemon]
            List of availbale Pokemon instances for capture
        """
        pass


    def __str__(self) -> str:
        x, y = self.get_pos()
        return f"{'(Premium) ' if self.__premium else ''}Player {self.get_symbol()} @ (x={x}, y={y})"


class NonPremiumPlayer(Player):
    def __init__(self, x: int, y: int, symbol: str, lvl: int):
        """
        Parameters
        ----------
        x : int
            X coordinate
        y : int
            Y coordinate
        symbol : str 
            Single character representation of this entity, to be displayed on the grid
        lvl : int 
            Player level. Used in calculation of field of vision to determine which Pokemons are available for catching
        premium : bool
            Whether player is premium player
        """
        
        #######################
        ##   YOUR CODE HERE  ##
        #######################

        pass
    

class PremiumPlayer(Player):
    def __init__(self, x: int, y: int, symbol: str, lvl: int):
        """
        Parameters
        ----------
        x : int
            X coordinate
        y : int
            Y coordinate
        symbol : str 
            Single character representation of this entity, to be displayed on the grid
        lvl : int 
            Player level. Used in calculation of field of vision to determine which Pokemons are available for catching
        premium : bool
            Whether player is premium player
        """

        #######################
        ##   YOUR CODE HERE  ##
        #######################

        pass


"""TEST CASE"""

GRID_HEIGHT = 15
GRID_WIDTH = 50

pokemons = []
pokemons.append(Pokemon(2,4,'A'))
pokemons.append(Pokemon(2,3,'B'))
pokemons.append(Pokemon(6,4,'C'))
pokemons.append(Pokemon(5,4,'D'))
pokemons.append(Pokemon(9,1,'E'))
pokemons.append(Pokemon(14,2,'F'))
pokemons.append(Pokemon(3,1,'G'))
pokemons.append(Pokemon(11,11,'H'))
pokemons.append(Pokemon(3,2,'I'))
pokemons.append(Pokemon(39,13,'J'))
pokemons.append(Pokemon(41,10,'K'))
pokemons.append(Pokemon(45,2,'L'))

players = []
players.append(NonPremiumPlayer(5,5,'1',4))
players.append(PremiumPlayer(39,8,'2',8))
               
display_grid(GRID_HEIGHT, GRID_WIDTH, pokemons, players)

for player in players:
    print(f'Player {player.get_symbol()}')
    for pokemon in player.get_available_pokemons(pokemons):
        print(pokemon.get_pos(), pokemon.get_symbol())