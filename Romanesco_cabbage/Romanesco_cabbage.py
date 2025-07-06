import pygame
import math

# Инициализация pygame
pygame.init()

# Настройки окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Капуста Романеско")

# Цвета
GREEN = (50, 200, 50)
DARK_GREEN = (0, 100, 0)
BACKGROUND = (0, 0, 0)

# Параметры фрактала
scale = 100
angle = math.pi / 4  # 45 градусов в радианах
depth = 10

def draw_romanesco(surface, x, y, size, angle, depth):
    if depth == 0:
        return
    
    # Рисуем текущий уровень
    points = []
    for i in range(5):
        px = x + size * math.cos(i * 2 * math.pi / 5 + angle)
        py = y + size * math.sin(i * 2 * math.pi / 5 + angle)
        points.append((px, py))
    
    # Заливаем многоугольник
    pygame.draw.polygon(surface, (DARK_GREEN if depth % 2 else GREEN), points)
    pygame.draw.polygon(surface, (0, 0, 0), points, 1)  # Контур
    
    # Рекурсивно рисуем следующие уровни
    new_size = size * 0.5
    for i in range(5):
        nx = x + (size + new_size) * math.cos(i * 2 * math.pi / 5 + angle)
        ny = y + (size + new_size) * math.sin(i * 2 * math.pi / 5 + angle)
        draw_romanesco(surface, nx, ny, new_size, angle + math.pi/10, depth - 1)

# Основной цикл
clock = pygame.time.Clock()
angle_rotation = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BACKGROUND)
    
    # Анимируем вращение
    angle_rotation += 0.01
    
    # Рисуем фрактал в центре экрана
    draw_romanesco(screen, width//2, height//2, scale, angle_rotation, depth)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()