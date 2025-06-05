import pygame
import random

pygame.font.init()

# Ekran o'lchami
s_width = 300
s_height = 600
block_size = 30

play_width = 10 * block_size
play_height = 20 * block_size

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# Shakllar (7 xil Tetris bo‘lagi)
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255),
                (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

# Har bir tosh obyekt sifatida
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

# Shaklni 2D listga aylantirish
def convert_shape_format(piece):
    positions = []
    shape = piece.shape[piece.rotation % len(piece.shape)]

    for i, line in enumerate(shape):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((piece.x + j, piece.y + i))
    return positions

# O‘yin oynasini chizish
def draw_window(surface):
    surface.fill((0, 0, 0))
    for i in range(20):
        for j in range(10):
            pygame.draw.rect(surface, (128,128,128), (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 1)
    pygame.display.update()

def main():
    win = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption("🧱 Tetris o‘yini")

    locked_positions = {}
    change_piece = False
    run = True
    current_piece = Piece(5, 0, random.choice(shapes))
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        fall_speed = 0.5
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(win)

main()
pygame.quit()
