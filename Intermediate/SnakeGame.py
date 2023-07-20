import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)
        
        if new_head in self.body:
            return False
        
        self.body.insert(0, new_head)
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        
        return True

    def change_direction(self, dx, dy):
        self.direction = (dx, dy)

    def grow_snake(self):
        self.grow = True

    def draw(self, surface):
        for x, y in self.body:
            pygame.draw.rect(surface, GREEN, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        return random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

    def draw(self, surface):
        x, y = self.position
        pygame.draw.rect(surface, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Main function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(1, 0)

        if not snake.move():
            pygame.quit()
            sys.exit()

        if snake.body[0] == food.position:
            snake.grow_snake()
            food.position = food.randomize_position()

        # Drawing
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

if __name__ == "__main__":
    main()
