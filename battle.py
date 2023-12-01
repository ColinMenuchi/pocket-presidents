import pygame
from president import President
from button import Button

def what_will_you_do(battle_screen):
    screen = battle_screen
    # blit battle menu with buttons
    what_do = pygame.image.load('graphics/what_will_you_do.png').convert_alpha()
    what_do_rect = what_do.get_rect()
    what_do_rect.center = (555, 400)
    screen.blit(what_do, (what_do_rect.x, what_do_rect.y))
    # allow for user to make their move choice
    # do a damage sequence
    # start the next turn
