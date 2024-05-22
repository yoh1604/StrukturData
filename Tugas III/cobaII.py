import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
WIDTH = 1000
HEIGHT = 800
SCREEN = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Hanoi Tower's Yohana")

SCREEN.fill(WHITE)

def draw_tower(pole, x, y):
    for i, disk in enumerate(pole):
        width = disk * 30
        height = 20
        color = pygame.Color(50 + i * 30, 100 + i * 30, 200 + i * 10)
        pygame.draw.rect(SCREEN, color, (x - width // 2, y - i * 30, width, height))

def drawBasePole():
    pygame.draw.rect(SCREEN, (139, 69, 19), (200, 600, 600, 50))

def draw_screen(pole):
    SCREEN.fill(WHITE)
    for i, key in enumerate(pole.keys()):
        x = (i + 1) * WIDTH // 4
        y = HEIGHT - 50
        draw_tower(pole[key], x, y)
    pygame.display.flip()

def drawPole(pole, x, y):
    for i, disk in enumerate(pole):
        width = disk * 30
        height = 20
        color = pygame.Color(50 + i * 30, 100 + i * 30, 200 + i * 10)
        pygame.draw.rect(SCREEN, color, (x - width // 2, y - i * 30, width, height))

def game(n, sourcepole, spacepole, targetpole, pole):
    if n == 1:
        # Pindahkan disk dari source ke destination
        disk = pole[sourcepole].pop()
        pole[targetpole].append(disk)
        draw_screen(pole)
        pygame.time.delay(10000)
        return
    game(n - 1, sourcepole, targetpole, spacepole, pole)
    disk = pole[sourcepole].pop()
    pole[targetpole].append(disk)
    draw_screen(pole)
    pygame.time.delay(10000)
    game(n - 1, spacepole, sourcepole, targetpole, pole)
    
    # if n == 1:
    #     targetpole.append(sourcepole.pop())
    #     draw_screen(pole)
    #     pygame.time.delay(1000)
    #     return
    # game(n - 1, sourcepole, targetpole, spacepole, pole)
    # targetpole.append(sourcepole.pop())
    # draw_screen(pole)
    # pygame.time.delay(1000)
    # game(n - 1, spacepole, targetpole, sourcepole, pole)

# n = int(input("Input jumlah stack: ")) # Ubah ke integer
n = 5
pole = {
    'A': list(range(n, 0, -1)),
    'B': [],
    'C': []
}

play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    # drawBasePole()
    draw_screen(pole)
    pygame.display.flip()

    game(n, pole['A'], pole['B'], pole['C'], pole) # Gunakan nilai 'n' yang sudah dalam bentuk integer

pygame.quit()
sys.exit()
