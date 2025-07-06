import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Треугольник Серпинского")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Вершины равностороннего треугольника (центрированы)
triangle_vertices = [
    (WIDTH // 2, 100),                # Верхняя вершина
    (WIDTH // 4, HEIGHT - 100),       # Левая нижняя
    (3 * WIDTH // 4, HEIGHT - 100)    # Правая нижняя
]

# Начальная случайная точка
current_point = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

# Основной цикл
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Отрисовка вершин треугольника (красные точки)
    for vertex in triangle_vertices:
        pygame.draw.circle(screen, RED, vertex, 3)
    
    # Выбираем случайную вершину
    chosen_vertex = random.choice(triangle_vertices)
    
    # Вычисляем середину между текущей точкой и выбранной вершиной
    new_x = (current_point[0] + chosen_vertex[0]) // 2
    new_y = (current_point[1] + chosen_vertex[1]) // 2
    current_point = (new_x, new_y)
    
    # Рисуем новую точку (белая)
    pygame.draw.circle(screen, WHITE, current_point, 1)
    
    pygame.display.flip()
    clock.tick(1000)  # Ограничение FPS (можно убрать)

pygame.quit()
sys.exit()