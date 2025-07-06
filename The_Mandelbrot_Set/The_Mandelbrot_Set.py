import pygame
import sys

# Инициализация pygame
pygame.init()

# Настройки окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Множество Мандельброта")

# Параметры фрактала
max_iter = 100  # Максимальное количество итераций
zoom = 300      # Масштаб
move_x, move_y = -0.5, 0  # Смещение центра

# Цветовая палитра
def get_color(iter):
    if iter < max_iter:
        color_int = int(255 * iter / max_iter)
        return (color_int, color_int, color_int)
    return (0, 0, 0)  # Черный цвет для точек внутри множества

# Функция для проверки принадлежности к множеству Мандельброта
def mandelbrot(c, max_iter):
    z = complex(0, 0)
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return i
    return max_iter

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # Управление клавишами
            elif event.key == pygame.K_LEFT:
                move_x -= 0.1
            elif event.key == pygame.K_RIGHT:
                move_x += 0.1
            elif event.key == pygame.K_UP:
                move_y -= 0.1
            elif event.key == pygame.K_DOWN:
                move_y += 0.1
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                zoom *= 1.1
            elif event.key == pygame.K_MINUS:
                zoom /= 1.1
    
    # Отрисовка множества
    for x in range(width):
        for y in range(height):
            # Преобразование координат экрана в комплексные числа
            c = complex(
                (x - width / 2) / zoom + move_x,
                (y - height / 2) / zoom + move_y
            )
            # Вычисление количества итераций
            iter = mandelbrot(c, max_iter)
            # Получение цвета
            color = get_color(iter)
            # Рисование пикселя
            screen.set_at((x, y), color)
    
    pygame.display.flip()

pygame.quit()
sys.exit()