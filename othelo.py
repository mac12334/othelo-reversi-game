import pygame
from collections import Counter as c
import os

pygame.init()


inf = pygame.display.Info()
width, height = inf.current_w, inf.current_h
bg = 0, 153, 0

h = height / 10
piece_w, piece_h = h / 2, h / 2
h_b = h * 8

WIN = pygame.display.set_mode((width, height))
PATH = os.path.abspath('.') + '/'

WHITE = pygame.image.load(PATH + "othelo_assets/white.png")
white = pygame.transform.scale(WHITE, (piece_w, piece_h))
BLACK = pygame.image.load(PATH + "othelo_assets/black.png")
black = pygame.transform.scale(BLACK, (piece_w, piece_h))
font = pygame.font.SysFont("arialblack", 32)

b = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

def tup(lst, x, y, color, o_color, d_x, d_y):
    a = x
    b = y
    z = 0
    xl = []
    yl = []
    for i in range(len(lst)):
        if 8 > x > -1 and 8 > y > -1:
            if lst[y][x] != 0:
                if lst[y][x] == color:
                    xl.append(x)
                    yl.append(y)
                    z += 1
                x += d_x
                y += d_y
            else:
                break
        else:
            break
    
    if z >= 2:
        m = xl[1]
        n = yl[1]
        for i in range(len(lst)):
            if 8 > a > -1 and 8 > b > -1:
                if a != m or b != n:
                    if lst[b][a] == o_color:
                        lst[b][a] = color
                    a += d_x
                    b += d_y
                else:
                    break
            else:
                break

sting = ""
color = (255, 255, 255)
def two(t):
    if t % 2 == 1:
        incrimint = None
        c = 1
        o = 2
        pos = pygame.mouse.get_pos()
        mx, my = pos
        x, y = (mx / h) - 5, (my / h) - 1
        x = int(x)
        y = int(y)
        if b[y][x] == 0:
            b[y][x] = c
            tup(b, x, y, c, o, 0, 1)
            tup(b, x, y, c, o, 0, -1)
            tup(b, x, y, c, o, 1, 0)
            tup(b, x, y, c, o, -1, 0)
            tup(b, x, y, c, o, 1, 1)
            tup(b, x, y, c, o, -1, 1)
            tup(b, x, y, c, o, -1, -1)
            tup(b, x, y, c, o, 1, -1)
            incrimint = True
        else:
            incrimint = False
        return incrimint

def one(t):
    if t % 2 == 0:
        incrimint = None
        c = 2
        o = 1
        pos = pygame.mouse.get_pos()
        mx, my = pos
        x, y = (mx / h) - 5, (my / h) - 1
        x = int(x)
        y = int(y)
        if b[y][x] == 0:
            b[y][x] = c
            tup(b, x, y, c, o, 0, 1)
            tup(b, x, y, c, o, 0, -1)
            tup(b, x, y, c, o, 1, 0)
            tup(b, x, y, c, o, -1, 0)
            tup(b, x, y, c, o, 1, 1)
            tup(b, x, y, c, o, -1, 1)
            tup(b, x, y, c, o, -1, -1)
            tup(b, x, y, c, o, 1, -1)
            incrimint = True
        else:
            incrimint = False
        return incrimint

def draw(sting, color):
    WIN.fill(bg)
    m, n = (width / 2) - (h_b / 2), (height / 2) - (h_b / 2)
    og_m = m
    px, py = (h / 2) - (piece_w / 2) + m, (h / 2) - (piece_h / 2) + n
    og_x = px
    pygame.draw.rect(WIN, (0,0,0), pygame.Rect(m, n, h_b, h_b), 4)
    for y in range(len(b)):
        px = og_x
        m = og_m
        for x in range(len(b)):
            pygame.draw.rect(WIN, (0,0,0), pygame.Rect(m, n, h, h), 2)
            if b[y][x] == 1:
                WIN.blit(white, (px, py))
            if b[y][x] == 2:
                WIN.blit(black, (px, py))
            m += h
            px += h
        n += h
        py += h
    if sting == "":
        sting = "black's move: "
        color = (255, 255, 255)
    img = font.render(sting, True, color)
    WIN.blit(img, (10, 10))
    
    pygame.display.update()

running = True
t = 0

while running:
    gotEvent = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gotEvent = True

        elif event.type == pygame.MOUSEBUTTONUP:
            gotEvent = True

    if gotEvent and event.type == pygame.MOUSEBUTTONDOWN:
        nz = 0
        for i in range(len(b)):
            count = c(b[i])
            if 0 not in count.keys():
                nz += 1
        if nz == len(b):
            running = False
        else:
            if one(t):
                t += 1
            if two(t):
                t += 1
        if t % 2 == 1:
            sting = "white's move: "
            color = (0, 0, 0)
        if t % 2 == 0:
            sting = "black's move: "
            color = (255, 255, 255)
    draw(sting, color)

pygame.quit()