import pygame
from president import President
from button import Button
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

"""def first_attack(battle_screen, passed_font, player_character, enemy_character, move):
    screen = battle_screen
    battle_text_box = pygame.image.load('graphics/battle_text_box.png').convert_alpha()
    battle_text_rect = battle_text_box.get_rect()
    battle_text_rect.center = (390, 505)
    text_font = passed_font

    player = player_character
    player_name = player.sprites()[0].name
    enemy = enemy_character
    enemy_name = enemy.sprites()[0].name
    selected_move = move

    attack_text1 = text_font.render(f'{player_name} used ', False, 'Black')
    attack_text2 = text_font.render(f'{selected_move.name}!', False, 'Black')

    screen.blit(battle_text_box, (battle_text_rect.x, battle_text_rect.y))
    screen.blit(attack_text1, (170, 470))
    screen.blit(attack_text2, (170, 490))

    return selected_move.power"""

def compare_speed(player, enemy): #Takes two presidents as arguments, returning True if the first has a higher speed
    if player.speed > enemy.speed:
        return True
    elif player.speed < enemy.speed:
        return False
    else:
        return randint(0, 1)

    # do a damage sequence
    # start the next turn
    
