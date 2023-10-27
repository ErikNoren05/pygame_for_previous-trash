from .components.position import PositionComponent
from .components.direction import DirectionComponent
from .components.render import RenderComponent
from .components.tail import TailComponent
from .entities.entity import Entity
import random

# INITIALIZE
import pygame



pygame.init()


##config

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
CELL_SIZE = 10


#GAME WINDOW

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ECS Snake Game")
clock = pygame.time.Clock()

#Snake came to being
snake = Entity()
snake.add_component(PositionComponent(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
snake.add_component(DirectionComponent(CELL_SIZE, 0))
snake.add_component(RenderComponent(pygame.Color("green")))
snake.add_component(TailComponent())

#food came to being

food = Entity()
food.add_component(PositionComponent(random.randint(0,(SCREEN_WIDTH//CELL_SIZE)-1)*CELL_SIZE, 
                                     random.randint(0,(SCREEN_HEIGHT//CELL_SIZE)-1)*CELL_SIZE))


Entity = [snake, food]

movement_system = movementSystem() 
render_system = renderSystem() 
collision_system = collisionSystem()


# GAME LOOP'
running = True
while running
    for event in pygame.event.get():
        if event.type == pygame.quit():
            running = False
        if event.key == pygame.keydown:
            dir = snake.components[DirectionComponent]
pygame.quit()


