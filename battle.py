import pygame
from president import President
from button import Button
from move import Move
from random import randint

def what_will_you_do(battle_screen):
    screen = battle_screen
    # blit battle menu with buttons
    what_do = pygame.image.load('graphics/what_will_you_do.png').convert_alpha()
    what_do_rect = what_do.get_rect()
    what_do_rect.center = (545, 400)
    screen.blit(what_do, (what_do_rect.x, what_do_rect.y))

def are_you_sure(battle_screen):
    screen = battle_screen
    # blit battle menu with buttons
    are_sure = pygame.image.load('graphics/are_you_sure.png').convert_alpha()
    are_sure_rect = are_sure.get_rect()
    are_sure_rect.center = (545, 400)
    screen.blit(are_sure, (are_sure_rect.x, are_sure_rect.y))

def compare_speed(player, enemy): # Takes two presidents as arguments, returning True if the first has a higher speed
    if player.speed > enemy.speed:
        return True
    elif player.speed < enemy.speed:
        return False
    else:
        return randint(0, 1)
    
def calculate_dmg(move, attacker, defender): # Takes two presidents as arguments, returns damage 1st does to 2nd
    damage = int((move.power * (attacker.attack / defender.defense)) * defender.damage_healing_multiplier)
    if damage != 0:
        damage += randint(-10, 5)
    return damage

def calculate_heals(move, attacker): # Takes one president as an argument, returns amount it heals by
    healing = int(move.healing)
    return healing

    # do a damage sequence
    # start the next turn
    
