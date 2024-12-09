import sys
import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable,)
  Shot.containers = (shots, updatable, drawable)

  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  player_obj = Player(x, y)
  asteroid_field = AsteroidField()
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill(color="black")

    updatable.update(dt)
    for asteroid in asteroids:
      if asteroid.checkCollisions(player_obj):
        print("Game over!")
        sys.exit()
      for shot in shots:
        if asteroid.checkCollisions(shot):
          asteroid.kill()
          shot.kill()
    for sprite in drawable:
      sprite.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60)/1000


if __name__ == "__main__":
  main()