import pygame
from president import President, BillClinton
from button import Button
from battle import what_will_you_do
from sys import exit

#Initializing PyGame and Screen
pygame.init()
screen = pygame.display.set_mode((1000, 570))
pygame.display.set_caption('Pocket Presidents')
clock = pygame.time.Clock()

#Fonts
main_font = pygame.font.Font(None, 50)
name_font = pygame.font.Font(None, 35)
title_font = pygame.font.Font(None, 100)

#Game States
home_screen = False
president_select = False
battle = False

#Buttons
start_button_sound = pygame.mixer.Sound('audio/start_button_click.mp3')
start_button_image = pygame.image.load('graphics/start_button1.png').convert_alpha()
start_button_hover = pygame.image.load('graphics/start_button2.png').convert_alpha()
start_button = Button(500, 285, start_button_image, screen, 1, start_button_sound)

#Menu Screen
menu_title = pygame.image.load('graphics/pokemon_title.png').convert_alpha()
menu_title = pygame.transform.rotozoom(menu_title, 0, 0.18)
menu_title_rect = menu_title.get_rect(center = (500, 600))

menu_background = pygame.image.load('graphics/menu_background.jpeg').convert_alpha()
menu_background = pygame.transform.rotozoom(menu_background, 0, 1.025)

game_name_box1 = pygame.Rect((145, 410), (140, 60))
game_name_box2 = pygame.Rect((690, 410), (180, 72))
game_name_1 = title_font.render('Left', False, 'Red')
game_name_2 = title_font.render('Right', False, 'Blue')

ampersand_box = pygame.Rect((430, 360), (140, 140))
ampersand = pygame.image.load('graphics/ampersand.png').convert_alpha()
ampersand = pygame.transform.rotozoom(ampersand, 0, 0.09)
ampersand_rect = ampersand.get_rect(center = (500, 430))

menu_music = pygame.mixer.Sound('audio/menu_song.mp3')
first_iteration = True # Needed to play the music just once.

#President Select Screen
choose_your_character = title_font.render('Choose your Character', False, 'Black')
choose_box = pygame.Rect((100, 30), (800, 75))

#Battle Screen
battle_field = pygame.image.load('graphics/pokemon_battlefield2.webp').convert_alpha()

#Object Oriented Enemy & Player Instantiation
enemy = pygame.sprite.GroupSingle()
enemy.add(President('enemy', 'Abraham Lincoln'))

player = pygame.sprite.GroupSingle()
player.add(President('player', 'Donald Trump'))

#Player and Enemy Boxes
enemy_box = pygame.Rect((200, 50), (325, 100))
enemy_health_bar = pygame.Rect((213, 80), (300, 35))
player_box = pygame.Rect((650, 350), (325, 100))
player_health_bar = pygame.Rect((663, 380), (300, 35))

player_name = name_font.render(player.sprites()[0].name, False, 'Black')
enemy_name = name_font.render(enemy.sprites()[0].name, False, 'Black')

#Game Loop
while True:
    #Checking for every pygame event:
    for event in pygame.event.get():
        #Close PyGame
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        #Transition to President Select
        if home_screen:
            if start_button.is_clicked():
                menu_music.fadeout(1000) # Fades out music over time passed (miliseconds)
                home_screen = False

    #Home Screen
    if home_screen:
        #Blits background and "Pokemon"
        screen.blit(menu_background, (0, 0))
        screen.blit(menu_title, menu_title_rect)
        #Plays Music Once
        if first_iteration:
            menu_music.play(loops = -1)
            first_iteration = False
        #"Pokemon" Animation
        if menu_title_rect.y > 25:
            menu_title_rect.y -= 2
        if menu_title_rect.y < 25:
            #Blits Title Backgrounds
            pygame.draw.rect(screen, '#e1d9d1', game_name_box1)
            pygame.draw.rect(screen, '#e1d9d1', game_name_box2)
            pygame.draw.rect(screen, '#e1d9d1', ampersand_box)
            #Blits Titles
            screen.blit(game_name_1, (150, 410))
            screen.blit(game_name_2, (690, 410))
            screen.blit(ampersand, ampersand_rect)
            start_button.draw(start_button_image, start_button_hover)
    
    #President Select Screen
    elif president_select:
        screen.fill((49, 51, 53))
        pygame.draw.rect(screen, '#e1d9d1', choose_box)
        screen.blit(choose_your_character, (110, 30))
        #President Heads
        screen.blit(BillClinton().head, (50, 60))




    else:
        #Places the Battlefiled & Presidents On the Screen
        screen.blit(battle_field, (0, 0))
        enemy.draw(screen)
        enemy.update()
        player.draw(screen)
        player.update()

        #Places the Boxes On the Screen
        pygame.draw.rect(screen, '#e1d9d1', player_box)
        pygame.draw.rect(screen, 'Green', player_health_bar)
        pygame.draw.rect(screen, '#e1d9d1', enemy_box)
        pygame.draw.rect(screen, 'Green', enemy_health_bar)

        screen.blit(player_name, (655, 355))
        screen.blit(enemy_name, (205, 55))

        what_will_you_do(screen)
    
    pygame.display.update()
    clock.tick(60)
