"""
The game state and logic (model component) of 512, 
a game based on 2048 with a few changes. 
This is the 'model' part of the model-view-controller
construction plan.  It must NOT depend on any
particular view component, but it produces event 
notifications to trigger view updates. 
"""

from game_element import GameElement, GameEvent, EventKind
from typing import List, Tuple, Optional
import random

# Configuration constants
GRID_SIZE = 4

class Vec():
    """A Vec is an (x,y) or (row, column) pair that
    represents distance along two orthogonal axes.
    Interpreted as a position, a Vec represents
    distance from (0,0).  Interpreted as movement,
    it represents distance from another position.
    Thus we can add two Vecs to get a Vec.
    """
    #Fixme:  We need a constructor, and __add__ method, and __eq__.

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vec({self.x}, {self.y})"



class Tile(GameElement):
    """A slidy numbered thing."""

    def __init__(self):
        super().__init__()






















class Board(GameElement):
    """The game grid.  Inherits 'add_listener' and 'notify_all'
    methods from game_element.GameElement so that the game
    can be displayed graphically.
    """
    def __init__(self, rows=4, cols=4):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.tiles = [ ]
        for row in range(rows):
            row_tiles = [ ]
            for col in range(cols):
                row_tiles.append(None)
            self.tiles.append(row_tiles)
        
    def has_empty(self) -> bool:
        """Is there at least one grid element without a tile?"""
        for row in range(self.height):
            for col in range(self.width):
                if self.tiles[row][col] is None:
                    return True
        return False






    def from_list(self, values:List[List[int]]):
        self.size = len(values)
        self.tiles = [[None for _ in range(self.size)] for _ in range(self.size)]

        for i, row in enumerate(values):
            for j, value in enumerate(row):
                if value != 0:
                    tile = Tile(value)
                    self.tiles[i][j] = tile
    
    def to_list(self, values:List[List[int]]):
        result = [ ]
        for row in self.tiles:
            row_values = []
            for col in row:
                if col is None:
                    row_values.append(0)
                else:
                    row_values.append(col.value)
            result.append(row_values)
        return result

    def from_list(self, values:List[List[int]]):
        self.size = len(values)
        self.tiles = [[None for _ in range(self.size)] for _ in range(self.size)]

        for i, row in enumerate(values):
            for j, value in enumerate(row):
                if value != 0:
                    tile = Tile()
                    tile.value = value
                    self.tiles[i][j] = tile


    def from_list(self, values:List[List[int]]):
        if len(values) != self.rows or any(len(row) != self.cols for row in values):
            raise ValueError("Input list dimensions do not match board dimensions")

        for row in range(self.rows):
            for col in range(self.cols):
                if values[row][col] == 0:
                    self.tiles[row][col] = None
                else:
                    self.tiles[row][col] = values[row][col]










    def in_bounds(self, pos:Vec) -> bool:
        return 0 <= pos.x < self.size and 0 <= pos.y , self.size
      










    def slide(self, pos: Vec, dir: Vec):
        if self[pos] is None:
            return 
        while True:
            new_pos = pos + dir
            if not self. in_bounds(new_pos) :
                break
            
            if self[new_pos] is None:
                self._move_tile(pos, new_pos) 
            
            elif self[pos] == self[new_pos]:
                self [pos].merge(self[new_pos]) 
                self._move_tile(pos, new_pos)
                break # Stop moving when we merge with another tile 
            else:
                break
            pos = new_pos
    
    
    def slide(self, pos: Vec, dir: Vec):
        if not self.in_bounds(pos):
            raise ValueError("Position is out of bounds")

        tile = self.tiles[pos.x][pos.y]

        if tile is None:
            return  # No tile to slide

        while True:
            new_pos = pos + dir
            if not self.in_bounds(new_pos):
                break  # Reached board edge

            new_tile = self.tiles[new_pos.x][new_pos.y]

            if new_tile is None:
                # Slide to an empty space
                self.tiles[new_pos.x][new_pos.y] = tile
                self.tiles[pos.x][pos.y] = None
                pos = new_pos
            elif new_tile == tile:
                # Merge with the same value
                tile.merge(new_tile)
                self.tiles[pos.x][pos.y] = None
                break  # Stop moving after merge
            else:
                break  # Stop when encountering a different tile





    def _move_tile(self, old_pos: Vec, new_pos: Vec):
        if not self.in_bounds(old_pos) or not self.in_bounds(new_pos):
            raise ValueError("Positions are out of bounds")

        if old_pos == new_pos:
            return  

        old_tile = self.tiles[old_pos.x][old_pos.y]

        if old_tile is None:
            return 

        new_tile = self.tiles[new_pos.x][new_pos.y]

        if new_tile is None or new_tile == old_tile:
            self.tiles[new_pos.x][new_pos.y] = old_tile
            self.tiles[old_pos.x][old_pos.y] = None
            if new_tile is not None and new_tile != old_tile:
                old_tile.merge(new_tile)




    
    
    def place_tile(self):
        """Place a tile on a randomly chosen empty square."""
        if not self.has_empty():
            return  # No empty squares available to place a tile

        # List all empty positions
        empty_positions = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.tiles[row][col] is None:
                    empty_positions.append(Vec(row, col))

        # Choose a random empty position
        new_pos = random.choice(empty_positions)

        # Place a new tile (assuming Tile class exists and can be instantiated)
        self.tiles[new_pos.x][new_pos.y] = Tile()  #




    def score(self) -> int:
        """Calculate a score from the board.
        (Differs from classic 1024, which calculates score
        based on sequence of moves rather than state of
        board.
        """
        return 0
        #FIXME


