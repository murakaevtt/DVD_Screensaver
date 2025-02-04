# Imports & inits
import pygame, random
from sys import exit
from screeninfo import get_monitors

pygame.init()

# Getting monitor data
monitor = get_monitors()[0]

# Logging
LOG = False

# Screen
WIDTH = monitor.width
HEIGHT = monitor.height

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('DVD')
pygame.mouse.set_visible(False)

# Time
clock = pygame.time.Clock()
FPS = 30

# icon
dvd_icon_surface = pygame.image.load('images/dvd.png')

# Coordinates
dvd_x_pos = random.randint(0, WIDTH - dvd_icon_surface.get_width())
dvd_y_pos = random.randint(0, HEIGHT - dvd_icon_surface.get_height())

x = WIDTH // 250
y = HEIGHT // 250

# Main cycle
while True:
  
  # Allow window cross to work
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        exit()
      
  # Drawing
  screen.fill('black')
  screen.blit(dvd_icon_surface, (dvd_x_pos, dvd_y_pos))
  
  # Moving
  dvd_x_pos += x
  dvd_y_pos += y

  if dvd_x_pos <= 0 or dvd_x_pos >= WIDTH - dvd_icon_surface.get_width():
    x *= -1
  if dvd_y_pos <= 0 or dvd_y_pos >= HEIGHT - dvd_icon_surface.get_height():
    y *= -1
  
  # Logging
  if LOG:
    print(f'dvd_x_pos: {dvd_x_pos}\tdvd_y_pos: {dvd_y_pos}')
  
  # Render
  pygame.display.update()
  clock.tick(FPS)