import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x,y,radius)
    #self.position = pygame.Vector2(x,y)
    #self.radius = radius

  def draw(self, screen):
    pygame.draw.circle(screen, "white",self.position,self.radius,width=2)

  def update(self, dt):
    self.position += (self.velocity * dt)

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    random_angle = random.uniform(20.0, 50.0)
    p1 = self.velocity.rotate(random_angle)
    p2 = self.velocity.rotate(-random_angle)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    obj1 = Asteroid(self.position.x, self.position.y, new_radius)
    obj2 = Asteroid(self.position.x, self.position.y, new_radius)
    obj1.velocity = p1 * 1.2
    obj2.velocity = p2 * 1.2

    