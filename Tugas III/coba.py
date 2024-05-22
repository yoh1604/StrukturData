import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ukuran layar
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower of Hanoi's Yohana")

# Fungsi untuk menggambar tumpukan disk
def draw_tower(tower, x, y):
    for i, disk in enumerate(tower):
        width = disk * 30  # Lebar disk
        height = 20  # Tinggi disk
        color = pygame.Color(50 + i * 2, 100 + i * 2, 200 + i * 2)
        pygame.draw.rect(SCREEN, color, (x - width // 2, y - i * 30, width, height))

# Fungsi untuk menggambar layar
def draw_screen(towers):
    SCREEN.fill(WHITE)
    for i, key in enumerate(towers.keys()):
        x = (i + 1) * WIDTH // 4
        y = HEIGHT - 50
        draw_tower(towers[key], x, y)
    pygame.display.flip()

# Fungsi Tower of Hanoi rekursif
def TowerOfHanoi(n, source, auxiliary, destination, towers):
    if n == 1:
        # Pindahkan disk dari source ke destination
        disk = towers[source].pop()
        towers[destination].append(disk)
        draw_screen(towers)
        pygame.time.delay(100)
        return
    TowerOfHanoi(n - 1, source, destination, auxiliary, towers)
    disk = towers[source].pop()
    towers[destination].append(disk)
    draw_screen(towers)
    pygame.time.delay(100)
    TowerOfHanoi(n - 1, auxiliary, source, destination, towers)

# Inisialisasi tumpukan awal
n = 8
towers = {
    'A': list(range(n, 0, -1)),
    'B': [],
    'C': []
}

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill(WHITE)
    draw_screen(towers)
    pygame.display.flip()

    # Mulai permainan Tower of Hanoi
    TowerOfHanoi(n, 'A', 'B', 'C', towers)

pygame.quit()
sys.exit()