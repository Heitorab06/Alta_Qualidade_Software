import pygame

from settings import Settings # type: ignore
from ship import Ship # type: ignore


def test_ship_move_esquerda():
    pygame.init()
    
    screen = pygame.display.set_mode((800, 600))
    settings = Settings()
    
    ship = Ship(screen, settings)
    
    x_inicial = ship.x
    
    ship.moving_left = True
    ship.update()
    
    assert ship.x < x_inicial