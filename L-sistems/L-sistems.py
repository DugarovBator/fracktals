import pygame
import math

# Инициализация pygame
pygame.init()

# Настройки окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("L-системы")

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)

# Параметры L-системы
class LSystem:
    def __init__(self):
        self.angle = 25
        self.length = 5
        self.rules = {}
        self.axiom = ""
        self.positions = []
        self.color = GREEN

# Примеры L-систем
def create_system(choice):
    system = LSystem()
    
    if choice == 1:  # Бинарное дерево
        system.axiom = "0"
        system.rules = {
            "1": "11",
            "0": "1[0]0"
        }
        system.angle = 45
        system.length = 8
        system.start_pos = (width//2, height-50)
        system.start_angle = 90
        
    elif choice == 2:  # Кривая дракона
        system.axiom = "FX"
        system.rules = {
            "X": "X+YF+",
            "Y": "-FX-Y"
        }
        system.angle = 90
        system.length = 5
        system.start_pos = (width//3, height//2)
        system.start_angle = 0
        
    elif choice == 3:  # Куст
        system.axiom = "F"
        system.rules = {
            "F": "FF+[+F-F-F]-[-F+F+F]"
        }
        system.angle = 25
        system.length = 5
        system.start_pos = (width//2, height-50)
        system.start_angle = 90
        system.color = BROWN
        
    return system

# Генерация строки по правилам L-системы
def generate_lsystem(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        result = "".join([rules.get(c, c) for c in result])
    return result

# Отрисовка L-системы
def draw_lsystem(surface, system, lstring, iterations):
    x, y = system.start_pos
    angle = system.start_angle
    stack = []
    length = system.length
    
    for cmd in lstring:
        if cmd == "F":
            new_x = x + length * math.cos(math.radians(angle))
            new_y = y - length * math.sin(math.radians(angle))
            pygame.draw.line(surface, system.color, (x, y), (new_x, new_y), 2)
            x, y = new_x, new_y
        elif cmd == "+":
            angle += system.angle
        elif cmd == "-":
            angle -= system.angle
        elif cmd == "[":
            stack.append((x, y, angle, length))
            length *= 0.7  # Уменьшаем длину для ветвей
        elif cmd == "]":
            x, y, angle, length = stack.pop()

# Основной цикл
def main():
    clock = pygame.time.Clock()
    iterations = 5
    current_system = 1
    system = create_system(current_system)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    iterations = max(1, iterations - 1)
                elif event.key == pygame.K_RIGHT:
                    iterations = min(100, iterations + 1)
                elif event.key == pygame.K_1:
                    current_system = 1
                    system = create_system(current_system)
                elif event.key == pygame.K_2:
                    current_system = 2
                    system = create_system(current_system)
                elif event.key == pygame.K_3:
                    current_system = 3
                    system = create_system(current_system)
        
        screen.fill(BLACK)
        
        lstring = generate_lsystem(system.axiom, system.rules, iterations)
        draw_lsystem(screen, system, lstring, iterations)
        
        # Отображаем информацию
        font = pygame.font.SysFont(None, 24)
        info = f"Система: {current_system} | Итерации: {iterations} | Команд: {len(lstring)}"
        text = font.render(info, True, (255, 255, 255))
        screen.blit(text, (10, 10))
        
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()