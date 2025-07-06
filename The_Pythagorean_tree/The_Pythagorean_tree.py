import pygame
import math

# Инициализация pygame
pygame.init()

# Настройки окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Дерево Пифагора")

# Цвета
BROWN = (139, 69, 19)
GREEN = (0, 128, 0)
BACKGROUND = (255, 255, 255)

# Параметры дерева
angle = math.pi / 4  # 45 градусов
length_ratio = 0.7   # Отношение длин ветвей
min_length = 5       # Минимальная длина ветви

def draw_pythagoras_tree(surface, x, y, length, angle, depth):
    if depth == 0 or length < min_length:
        return
    
    # Вычисляем конечную точку ствола/ветви
    x_end = x - length * math.sin(angle)
    y_end = y - length * math.cos(angle)
    
    # Рисуем текущую ветвь
    color = BROWN if depth > 3 else GREEN  # Меняем цвет на листья
    thickness = max(1, depth // 2)
    pygame.draw.line(surface, color, (x, y), (x_end, y_end), thickness)
    
    # Вычисляем новые точки для ветвления
    new_length = length * length_ratio
    
    # Рекурсивно рисуем две новые ветви
    draw_pythagoras_tree(surface, x_end, y_end, new_length, angle + math.pi/4, depth-1)
    draw_pythagoras_tree(surface, x_end, y_end, new_length, angle - math.pi/4, depth-1)

# Основной цикл
def main():
    clock = pygame.time.Clock()
    depth = 10  # Начальная глубина рекурсии
    angle_offset = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP and depth < 15:
                    depth += 1
                elif event.key == pygame.K_DOWN and depth > 1:
                    depth -= 1
                elif event.key == pygame.K_LEFT:
                    angle_offset -= 0.1
                elif event.key == pygame.K_RIGHT:
                    angle_offset += 0.1
        
        screen.fill(BACKGROUND)
        
        # Рисуем дерево из центра нижней части экрана
        start_length = 120
        start_angle = angle + angle_offset
        draw_pythagoras_tree(screen, width//2, height-50, start_length, start_angle, depth)
        
        # Отображаем информацию
        font = pygame.font.SysFont(None, 36)
        info = f"Глубина: {depth} | Угол: {angle_offset:.1f}"
        text = font.render(info, True, (0, 0, 0))
        screen.blit(text, (10, 10))
        
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()