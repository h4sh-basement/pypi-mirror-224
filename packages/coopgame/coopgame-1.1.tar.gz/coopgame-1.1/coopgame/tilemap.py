import pygame
import numpy as np
from typing import Tuple
from cooptools.colors import Color
import coopgame.pygamehelpers as help
from coopstructs.geometry.rectangle import Rectangle
from typing import List

"""
This implemenation is based off of the description on the pygame website docs at: https://pygame.readthedocs.io/en/latest/tiles/tiles.html
"""
class TileSet:
    def __init__(self, tiles: List[pygame.Surface] = None):
        self.tiles = tiles or []

class FileTileset(TileSet):
    def __init__(self, file, size=(32, 32), margin=1, spacing=1):
        super().__init__()
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.load()

    def load(self):
        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing

        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                self.tiles.append(tile)

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'




class Tilemap:
    def __init__(self,
                 tileset: TileSet,
                 map_size=None,
                 render_on_init: bool = True,
                 surface_size: Tuple[int, int] = None,
                 buffer_tiles: Tuple[int, int] = None,
                 map: np.ndarray = None,
                 pxls: int = 32,
                 outline_tile_color: Color = None):

        self.pxls = pxls
        self._tile_size = (self.pxls, self.pxls)

        if map is not None:
            self.map = map
        elif map_size:
            self.map = np.zeros(map_size, dtype=int)
        else:
            self.map = np.zeros((10, 20), dtype=int)

        self.size = self.map.shape
        self.buffer_tiles = buffer_tiles

        self.tileset = tileset
        self.image = None

        self.render_surface_size = surface_size
        if buffer_tiles is not None:
            self.render_surface_size = (self.render_surface_size[0] + self.buffer_tiles[0] * self._tile_size[0],
                                        self.render_surface_size[1] + self.buffer_tiles[1] * self._tile_size[1])

        self.outline_tile_color = outline_tile_color
        if render_on_init:
            self.render(self.render_surface_size, outline_tiles_color=outline_tile_color)

    def render(self, surface_size: Tuple[int, int], outline_tiles_color: Color = None):
        h, w = self.map.shape
        rows, cols = self.map.shape

        # if self.buffer_tiles is not None:
        #     h -= self.buffer_tiles[1]
        #     w -= self.buffer_tiles[0]

        self.render_surface_size = surface_size
        self.image = pygame.Surface(surface_size)
        self.image.fill(Color.HOT_PINK.value)
        self.image.set_colorkey(Color.HOT_PINK.value)
        self.image.convert_alpha()

        tile_size_w = surface_size[0] / w
        tile_size_h = surface_size[1] / h
        self._tile_size = (tile_size_w, tile_size_h)

        for i in range(w):

            for j in range(h):
                tile = self.tileset.tiles[self.map[j, i]]
                scaled_tile = pygame.transform.scale(tile, (int(tile_size_w), int(tile_size_h)))
                self.image.blit(scaled_tile, (i*tile_size_w,j*tile_size_h))
                if outline_tiles_color is not None:
                    help.draw_box(self.image,
                                  Rectangle(x=i * tile_size_w,
                                            y=j * tile_size_h,
                                            width=tile_size_w,
                                            height=tile_size_h),
                                  color=outline_tiles_color,
                                  width=1)


    def set_value(self, value):
        self.map.fill(value)
        self.render(self.render_surface_size, outline_tiles_color=self.outline_tile_color)

    def set_random(self):
        n = len(self.tileset.tiles)
        self.map = np.random.randint(n, size=self.size)
        self.render(self.render_surface_size, outline_tiles_color=self.outline_tile_color)

    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'

    @property
    def rect(self):
        return self.image.get_rect()

    @property
    def TileSize(self):
        return self._tile_size