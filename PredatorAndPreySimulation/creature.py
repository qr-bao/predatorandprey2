import pygame
import random

# maxHealth    =>  integer for health (Out of 100)
# fieldRadius  => integer for field of view
# maxVelocity  => integer value of max Velocity
# position     => a tuple of integers for initial 2D coordinate system
# velocity     => current velocity
# color        => color code
# size         => size of creature

class Creature:
    def __init__(self, maxHealth, fieldRadius, maxVelocity, position, velocity, color, size):
        self.color = color
        self.size = size
        self.points = [(size/2, 0), (size, size), (0, size)]
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.polygon(self.surface, self.color, self.points)
        self.rect = self.surface.get_rect(center=position)
        self.maxHealth = maxHealth
        self.health = self.maxHealth
        self.fieldRadius = fieldRadius
        self.maxVelocity = maxVelocity
        self.velocity = pygame.math.Vector2(velocity)
        self.alive = True

    def draw(self, surface):
        surface.blit(self.surface, self.rect)
    
    def dead(self):
        self.alive = False
    
    def move(self, width, height):
        if(self.velocity.magnitude() > self.maxVelocity):
            self.velocity.scale_to_length(self.maxVelocity)
        
        self.rect.move_ip(self.velocity[0], self.velocity[1])
        
        if (self.rect.left <= 0 or self.rect.right >= width):
            self.velocity.update(-self.velocity[0], self.velocity[1])
            if self.rect.left <= 0:
                self.rect.left = 0
            if self.rect.left >= width:
                self.rect.right = width
        if (self.rect.top <= 0 or self.rect.bottom >= height):
            self.velocity.update(self.velocity[0], -self.velocity[1])
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= height:
                self.rect.bottom = height
    
    # def draw(self, surface):
    #     if(self.alive):
    #         pygame.draw.rect(surface, self.color, self.rect)
    
    def showFieldofView(self):
        pass
        #drawing the field of view circle
        #pygame.draw.circle(surface,(255,255,255),(self.x,self.y),self.fieldRadius)
    
    def details(self, name):
        if(self.alive):
            print(f"The {name}'s max health is {self.maxHealth}")
            print(f"The {name}'s field of view is from ({self.x},{self.y}) to a radius of {self.fieldRadius}")
            print(f"The {name}'s max velocity is {self.maxVelocity}")