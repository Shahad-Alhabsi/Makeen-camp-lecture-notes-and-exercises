from math import *
TOTAL_WIDTH = 5
TILE_WIDTH = 5


tiles = TOTAL_WIDTH / TILE_WIDTH # posible tiles number

black_tiles = ceil(tiles/2)
white_tiles = black_tiles - 1
print("black tiles = {} \nwhite tiles = {}".format(black_tiles, white_tiles))

gap = (TOTAL_WIDTH - (black_tiles+white_tiles)*5)/2
print(gap)