import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Kuş ayarları
bird_x = 50
bird_y = 300
bird_radius = 20
bird_velocity = 0
gravity = 0.5
jump_strength = -10

running = True
while running:
    screen.fill((135, 206, 235))  # Gökyüzü rengi

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Boşluk tuşuyla zıpla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    # Hareket
    bird_velocity += gravity
    bird_y += bird_velocity

    # Kuşu çiz
    pygame.draw.circle(screen, (255, 0, 0), (bird_x, int(bird_y)), bird_radius)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
