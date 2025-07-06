import pygame
import math

# Инициализация pygame
pygame.init()

# Настройки окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Снежинка Коха")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Начальные параметры
depth = 4  # Глубина рекурсии
length = 400  # Длина начальной линии

def draw_koch_snowflake(surface, depth, length, pos):
    x, y = pos
    # Три начальные точки равностороннего треугольника
    points = [
        (x, y),
        (x + length * math.cos(math.pi/3), y - length * math.sin(math.pi/3)),
        (x + length, y),
        (x, y)
    ]
    
    # Рисуем три стороны снежинки
    for i in range(3):
        p1 = points[i]
        p2 = points[i+1]
        koch_curve(surface, depth, p1, p2)

def koch_curve(surface, depth, p1, p2):
    if depth == 0:
        pygame.draw.line(surface, BLUE, p1, p2, 2)
    else:
        # Вычисляем промежуточные точки
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        
        # Точки, делящие отрезок на 3 части
        a = (p1[0] + dx / 3, p1[1] + dy / 3)
        b = (p1[0] + 2 * dx / 3, p1[1] + 2 * dy / 3)
        
        # Точка вершины равностороннего треугольника
        angle = math.atan2(dy, dx)
        new_length = math.sqrt((dx/3)**2 + (dy/3)**2)
        c = (
            a[0] + new_length * math.cos(angle - math.pi/3),
            a[1] + new_length * math.sin(angle - math.pi/3)
        )
        
        # Рекурсивно рисуем 4 отрезка
        koch_curve(surface, depth-1, p1, a)
        koch_curve(surface, depth-1, a, c)
        koch_curve(surface, depth-1, c, b)
        koch_curve(surface, depth-1, b, p2)

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)
    
    # Рисуем снежинку по центру экрана
    start_pos = (width//2 - length//2, height//2 + length//3)
    draw_koch_snowflake(screen, depth, length, start_pos)
    
    pygame.display.flip()

pygame.quit()