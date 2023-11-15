import pygame
from president import President
from sys import exit

#Initializing PyGame and Screen
pygame.init()
screen = pygame.display.set_mode((1000, 570))
pygame.display.set_caption('Pocket Presidents')
clock = pygame.time.Clock()
main_font = pygame.font.Font(None, 50)
name_font = pygame.font.Font(None, 35)

#Game States
home_screen = False
president_select = False
battle = False

#Menu Screen
menu_title = pygame.image.load('graphics/pokemon_title.png').convert_alpha()
menu_title = pygame.transform.rotozoom(menu_title, 0, 0.2)
menu_title_rect = menu_title.get_rect(center = (500, 200))

#Battle Screen
battle_field = pygame.image.load('graphics/pokemon_battlefield2.webp').convert_alpha()

#Object Oriented Enemy & Player Instantiation
enemy = pygame.sprite.GroupSingle()
enemy.add(President('enemy', 'Donald Trump'))

player = pygame.sprite.GroupSingle()
player.add(President('player', 'Donald Trump'))

#Player and Enemy Boxes
enemy_box = pygame.Rect((200, 50), (325, 100))
enemy_health_bar = pygame.Rect((213, 80), (300, 35))
player_box = pygame.Rect((650, 450), (325, 100))
player_health_bar = pygame.Rect((663, 480), (300, 35))

player_name = name_font.render(player.sprites()[0].name, False, 'Black')
enemy_name = name_font.render(enemy.sprites()[0].name, False, 'Black')

#Game Loop
while True:
    for event in pygame.event.get():
        #Close PyGame
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if home_screen:
        screen.blit(menu_title, (200, 150))

    else:
        #Places the Battlefiled & Presidents On the Screen
        screen.blit(battle_field, (0, 0))
        enemy.draw(screen)
        enemy.update()
        player.draw(screen)
        player.update()
        #screen.blit(joe_biden_scaled, (-40, 100))
        #Places the Boxes On the Screen
        pygame.draw.rect(screen, '#e1d9d1', player_box)
        pygame.draw.rect(screen, 'Green', player_health_bar)
        pygame.draw.rect(screen, '#e1d9d1', enemy_box)
        pygame.draw.rect(screen, 'Green', enemy_health_bar)

        screen.blit(player_name, (655, 455))
        screen.blit(enemy_name, (205, 55))
    
    pygame.display.update()
    clock.tick(60)
