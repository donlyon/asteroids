import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            angle1 = self.velocity.rotate(angle)
            angle2 = self.velocity.rotate(-angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, radius)
            a1.velocity = angle1 * 1.2
            a2 = Asteroid(self.position.x, self.position.y, radius)
            a2.velocity = angle2 * 1.2

        
