import pygame
from ..components.position import PositionComponent
from ..components.render import RenderComponent

CELL_SIZE = 10

class RenderSystem:
    def update(self, entity, screen):
        pos = entity.components[PositionComponent]
        render = entity.components[RenderComponent]
        ##
        pygame.draw.rect(screen, render.color, (pos.x, pos.t, CELL_SIZE, CELL_SIZE))
        ##