from functools import cmp_to_key
from .Vector3D import Vector3D
from .SpriteGroup import SpriteGroup
from .Updateables import *


# Grid used for 3D spatials indexing in the scene,
# to optimize the culling performance of viewport:
class SceneGrid:
    def __init__(self, cell_size, cols, rows):
        self.cell_size = cell_size
        self.cols = cols
        self.rows = rows
        self.cells = []
        self.createCells()

    def createCells(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_position = Vector3D(col * self.cell_size, row * self.cell_size, 0)
                cell = Cell(cell_position, self.cell_size, col, row)
                self.cells.append(cell)

    def shouldMoveSprite(self, old_loc, new_loc):
        old_cell_index = self.calculateCellIndex(old_loc)
        new_cell_index = self.calculateCellIndex(new_loc)
        return old_cell_index != new_cell_index

    def calculateCellIndex(self, location):
        col = (location.x - self.cell_size / 2) // self.cell_size
        row = (location.y - self.cell_size / 2 ) // self.cell_size
        cell_index = row * self.cols + col
        return int(cell_index)


    def addSprite(self, sprite):
        loc = sprite.getLocation()
        cell_index = self.calculateCellIndex(loc)
        print(cell_index)
        self.cells[cell_index].addSprite(sprite)

    def removeSprite(self, sprite):
        loc = sprite.getLocation()
        cell_index = self.calculateCellIndex(loc)
        self.cells[cell_index].removeSprite(sprite)


    def copy(self):
        return SceneGrid(self.cell_size, self.cols, self.rows)


class Cell:
    def __init__(self, position, size, col, row):
        self.position = position
        self.corner_tl = Vector3D(position.x - size / 2, position.y - size / 2)
        self.corner_tr = Vector3D(position.x + size / 2, position.y - size / 2)
        self.corner_bl = Vector3D(position.x - size / 2, position.y + size / 2)
        self.corner_br = Vector3D(position.x + size / 2, position.y + size / 2)
        self.sprites = []
        self.col = col
        self.row = row

    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        self.sprites.remove(sprite)