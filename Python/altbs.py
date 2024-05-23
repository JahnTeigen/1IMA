import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player variables
player_pos = [WIDTH // 2, HEIGHT // 2]
player_direction = 0  # 0: North, 90: East, 180: South, 270: West

# Maze variables
exit_pos = [700, 100]

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Maze Game")
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_direction = (player_direction - 90) % 360
            elif event.key == pygame.K_RIGHT:
                player_direction = (player_direction + 90) % 360
            elif event.key == pygame.K_UP:
                # Move forward one block
                movement = [math.cos(math.radians(player_direction)),
                            -math.sin(math.radians(player_direction))]
                player_pos[0] += movement[0]
                player_pos[1] += movement[1]
            elif event.key == pygame.K_DOWN:
                # Calculate distance to exit
                distance = math.sqrt((exit_pos[0] - player_pos[0]) ** 2 + (exit_pos[1] - player_pos[1]) ** 2)
                angle_to_exit = math.degrees(math.atan2(exit_pos[1] - player_pos[1], exit_pos[0] - player_pos[0]))

                # Convert angle to compass direction
                compass_directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
                index = round((angle_to_exit % 360) / 45) % 8
                direction_to_exit = compass_directions[index]

                print(f"{round(distance)} meters in {direction_to_exit} direction")

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (exit_pos[0] - 10, exit_pos[1] - 10, 20, 20))  # Exit marker
    pygame.draw.circle(screen, BLACK, (int(player_pos[0]), int(player_pos[1])), 10)  # Player marker

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
