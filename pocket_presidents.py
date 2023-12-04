import pygame
from president import President, BillClinton
from button import Button
from move import Move
from battle import what_will_you_do, are_you_sure, compare_speed, calculate_dmg, calculate_heals
import random
from sys import exit

#Initializing PyGame and Screen
pygame.init()
screen = pygame.display.set_mode((1000, 570))
pygame.display.set_caption('Pocket Presidents')
clock = pygame.time.Clock()

BATTLE_MUSIC = [pygame.mixer.Sound('audio/Battle-Chairman_Rose.flac'),
                pygame.mixer.Sound('audio/Battle-Marnie.flac'),
                pygame.mixer.Sound('audio/B&W-Battle_Gym_Leader.mp3'),
                pygame.mixer.Sound('audio/B&W-Battle_Wild.mp3'),
                pygame.mixer.Sound('audio/B&W-Battle_Team_Plasma.mp3')]

VICTORY_MUSIC = [pygame.mixer.Sound('audio/Marnie-Victory.flac'),
                 pygame.mixer.Sound('audio/B&W-Team_Plasma_Victory.mp3')]

#Fonts
main_font = pygame.font.Font(None, 50)
name_font = pygame.font.Font(None, 35)
title_font = pygame.font.Font(None, 100)
move_font = pygame.font.Font(None, 30)

#Game States
home_screen = False
president_select = False
battle = True
what_do = True
move_select = False
confirmation = False
attacks = False
player_deals_damage = False
enemy_deals_damage = False
win = False
lose = False

#Object Oriented Enemy & Player Instantiation
enemy_president = President('enemy', 'Abraham Lincoln')
enemy = pygame.sprite.GroupSingle()
enemy.add(enemy_president)

player_president = President('player', 'Donald Trump')
player = pygame.sprite.GroupSingle()
player.add(player_president)

#Buttons:
#Home Screen Start Button
start_button_sound = pygame.mixer.Sound('audio/start_button_click.mp3')
start_button_image = pygame.image.load('graphics/start_button1.png').convert_alpha()
start_button_hover = pygame.image.load('graphics/start_button2.png').convert_alpha()
start_button = Button(500, 285, start_button_image, screen, 1, start_button_sound)
#Battle Menu Buttons
button_audio = pygame.mixer.Sound('audio/battle_button_click.mp3') # Also used for move buttons
presidents_button_image = pygame.image.load('graphics/button_presidents1.png').convert_alpha()
presidents_hover_button = pygame.image.load('graphics/button_presidents2.png').convert_alpha()
fight_button_image = pygame.image.load('graphics/button_fight1.png').convert_alpha()
fight_hover_button = pygame.image.load('graphics/button_fight2.png').convert_alpha()
presidents_button = Button(650, 500, presidents_button_image, screen, 1, button_audio)
fight_button = Button(850, 500, fight_button_image, screen, 1, button_audio)
#Move Buttons
move1_button_image = pygame.image.load('graphics/button_move1-1.png').convert_alpha()
move1_button_hover = pygame.image.load('graphics/button_move1-2.png').convert_alpha()
move1_button = Button(610, 485, move1_button_image, screen, 1, button_audio)
move1_text = move_font.render(player_president.move_list[0].name, False, 'Black')

move2_button_image = pygame.image.load('graphics/button_move2-1.png').convert_alpha()
move2_button_hover = pygame.image.load('graphics/button_move2-2.png').convert_alpha()
move2_button = Button(810, 485, move2_button_image, screen, 1, button_audio)
move2_text = move_font.render(player_president.move_list[1].name, False, 'Black')

move3_button_image = pygame.image.load('graphics/button_move3-1.png').convert_alpha()
move3_button_hover = pygame.image.load('graphics/button_move3-2.png').convert_alpha()
move3_button = Button(610, 542, move3_button_image, screen, 1, button_audio)
move3_text = move_font.render(player_president.move_list[2].name, False, 'Black')

move4_button_image = pygame.image.load('graphics/button_move4-1.png').convert_alpha()
move4_button_hover = pygame.image.load('graphics/button_move4-2.png').convert_alpha()
move4_button = Button(810, 542, move4_button_image, screen, 1, button_audio)
move4_text = move_font.render(player_president.move_list[3].name, False, 'Black')

back_button_image = pygame.image.load('graphics/button_back1.png').convert_alpha()
back_button_image = pygame.transform.rotozoom(back_button_image, 0, 0.6)
back_button_hover = pygame.image.load('graphics/button_back2.png').convert_alpha()
back_button_hover = pygame.transform.rotozoom(back_button_hover, 0, 0.6)
back_button = Button(935, 510, back_button_image, screen, 1, button_audio)

confirm_button_image = pygame.image.load('graphics/button_confirm1.png').convert_alpha()
confirm_button_hover = pygame.image.load('graphics/button_confirm2.png').convert_alpha()
confirm_button = Button(800, 510, confirm_button_image, screen, 1, button_audio)

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

#President Select Screen
choose_your_character = title_font.render('Choose your Character', False, 'Black')
choose_box = pygame.Rect((100, 30), (800, 75))

#Battle Screen
#Background
battle_field = pygame.image.load('graphics/pokemon_battlefield2.webp').convert_alpha()

#Player and Enemy Boxes
enemy_box = pygame.Rect((200, 50), (325, 100))
enemy_black_bar = pygame.Rect((213, 80), (300, 35))
enemy_health_bar = pygame.Rect((213, 80), (300, 35))
player_box = pygame.Rect((650, 350), (325, 100))
player_black_bar = pygame.Rect((663, 380), (300, 35))
player_health_bar = pygame.Rect((663, 380), (300, 35))
#Names on Boxes
player_name = name_font.render(player_president.name, False, 'Black')
enemy_name = name_font.render(enemy_president.name, False, 'Black')
#Health on Boxes
player_health_card = name_font.render(f'HP: {player_president.health}/{player_president.max_health}', False, 'Black')
enemy_health_card = name_font.render(f'HP: {enemy_president.health}/{enemy_president.max_health}', False, 'Black')
#Text Card
battle_text_box = pygame.image.load('graphics/battle_text_box.png').convert_alpha()
battle_text_rect = battle_text_box.get_rect()
battle_text_rect.center = (390, 505)

#Music
battle_music = None # To be chosen randomly later

#Trackers & Determinators
selected_move = "" # Used to track the player's move selection during battle
enemy_moves = enemy_president.move_list # Used to hold the enemy's moves
enemy_selected_move = "" # Used to track the enemy's move selection during battle
damage_to_deal = 0 # Used to determine damage in combat
healing_to_do = 0 # Used to determine healing in combat
count_damage_health = -100 # Used to track the damage or healing done in combat
count_president_health = 0 # Used to increment/decrement health on name card
player_is_faster = None # Used to determine who moves first
turns_left = 2 # Used to prevent Player & Enemy from continuously damaging one anthother
can_calc_speed = True # Used so speed is only calculated once in battle
turn_can_change = True # Used to properly swap turns in battle
can_calc_dmg_heals = True # Used to only calculate damage and heals once each turn
first_iteration = True # Needed so music won't loop over itself.
player_move_is_status_move = False # Used to determine if a player move affects stats rather than health
enemy_move_is_status_move = False # Used to determine if an enemy move affects stats rather than health
can_change_stats = True # Used to only change a president's stats once


#Game Loop
while True:
    #Checking for every pygame event:
    for event in pygame.event.get():
        #Close PyGame
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        #Transition from Home Screen to President Select
        if home_screen:
            if start_button.is_clicked():
                menu_music.fadeout(1000) # Fades out music over time passed (miliseconds)
                first_iteration = True
                battle = True
                home_screen = False

        #Battle Menu
        if battle:
            #Pick Music
            if first_iteration:
                battle_music = random.choice(BATTLE_MUSIC)
                battle_music.play()
                first_iteration = False
            #Battle Phases
            if what_do:
                if presidents_button.is_clicked():
                    print('Test Successful')
                elif fight_button.is_clicked():
                    #Booleans to Determine Battle Menu Display
                    what_do = False
                    move_select = True
            elif move_select:
                if move1_button.is_clicked():
                    selected_move = player_president.move_list[0]
                    move_select = False
                    confirmation = True
                elif move2_button.is_clicked():
                    selected_move = player_president.move_list[1]
                    move_select = False
                    confirmation = True
                elif move3_button.is_clicked():
                    selected_move = player_president.move_list[2]
                    move_select = False
                    confirmation = True
                elif move4_button.is_clicked():
                    selected_move = player_president.move_list[3]
                    move_select = False
                    confirmation = True
                elif back_button.is_clicked():
                    selected_move = ""
                    move_select = False
                    what_do = True
            elif confirmation:
                if confirm_button.is_clicked():
                    confirmation = False
                    attacks = True
                    enemy_selected_move = random.choice(enemy_moves)
                elif back_button.is_clicked():
                    confirmation = False
                    move_select = True

    #Home Screen
    if home_screen:
        #Blits background and "Pokemon"
        screen.blit(menu_background, (0, 0))
        screen.blit(menu_title, menu_title_rect)
        #Plays Music Once
        if first_iteration:
            menu_music.play(loops=-1)
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
        player.draw(screen)
        if not win:
            enemy.update()
        if not lose:
            player.update()

        #Places the Boxes & Health Bars On the Screen
        pygame.draw.rect(screen, '#e1d9d1', player_box)
        pygame.draw.rect(screen, '#e1d9d1', enemy_box)
        pygame.draw.rect(screen, 'Black', player_black_bar)
        if player_health_bar.width > 150:
            pygame.draw.rect(screen, 'Green', player_health_bar)
        elif player_health_bar.width > 75:
            pygame.draw.rect(screen, 'Orange', player_health_bar)
        else:
            pygame.draw.rect(screen, 'Red', player_health_bar)
        pygame.draw.rect(screen, 'Black', enemy_black_bar)
        if enemy_health_bar.width > 150:
            pygame.draw.rect(screen, 'Green', enemy_health_bar)
        elif enemy_health_bar.width > 75:
            pygame.draw.rect(screen, 'Orange', enemy_health_bar)
        else:
            pygame.draw.rect(screen, 'Red', enemy_health_bar)
        #Changes President Cards Acoording to Health
        player_health_card = name_font.render(f'HP: {int(player_president.health)}/{player_president.max_health}', False, 'Black')
        enemy_health_card = name_font.render(f'HP: {int(enemy_president.health)}/{enemy_president.max_health}', False, 'Black')
        #Blit President Cards
        screen.blit(player_name, (655, 355))
        screen.blit(player_health_card, (655, 420))
        screen.blit(enemy_name, (205, 55))
        screen.blit(enemy_health_card, (205, 120))

        #Battle Menu Display
        if what_do:
            what_will_you_do(screen)
            presidents_button.draw(presidents_button_image, presidents_hover_button)
            fight_button.draw(fight_button_image, fight_hover_button)
        #Player Selects Move:
        elif move_select:
            what_will_you_do(screen)
            move1_button.draw(move1_button_image, move1_button_hover)
            screen.blit(move1_text, (535, 477))
            move2_button.draw(move2_button_image, move2_button_hover)
            screen.blit(move2_text, (735, 477))
            move3_button.draw(move3_button_image, move3_button_hover)
            screen.blit(move3_text, (535, 534))
            move4_button.draw(move4_button_image, move4_button_hover)
            screen.blit(move4_text, (735, 534))
            back_button.draw(back_button_image, back_button_hover)
        #Player Confirms Actions:
        elif confirmation:
            are_you_sure(screen)
            confirm_button.draw(confirm_button_image, confirm_button_hover)
            back_button.draw(back_button_image, back_button_hover)
        elif attacks:
            #Determine Who Moves First:
            if turns_left == 2 and can_calc_speed:
                player_is_faster = compare_speed(player_president, enemy_president)
                can_calc_speed = False
            elif turns_left == 1 and turn_can_change:
                player_is_faster = not player_is_faster
                turn_can_change = False
            
            if player_is_faster:
            #Display Message of Move Being Used
                if not player_move_is_status_move or count_damage_health < 0: # If move isn't status or provide a time buffer if it is
                    battle_text1 = name_font.render(f'{player_president.name} used ', False, 'Black')
                    battle_text2 = name_font.render(f'{selected_move.name}!', False, 'Black')
                screen.blit(battle_text_box, (battle_text_rect.x, battle_text_rect.y))
                screen.blit(battle_text1, (170, 470))
                screen.blit(battle_text2, (170, 490))

                #Check if move is a status move
                if selected_move.stat_change: # Stat Change is None if nonexistant
                    player_move_is_status_move = True

                #Calculate Damage Once
                if can_calc_dmg_heals:
                    damage_to_deal = calculate_dmg(selected_move, player_president, enemy_president) # Player will deal this damage to enemy
                    healing_to_do = calculate_heals(selected_move, player_president) # Player will heal this much health
                    can_calc_dmg_heals = False

                player_deals_damage = True # Player will now deal damage

            else:
                if not enemy_move_is_status_move or count_damage_health < 0:
                    battle_text1 = name_font.render(f'The opposing {enemy_president.name}', False, 'Black')
                    battle_text2 = name_font.render(f'used {enemy_selected_move.name}!', False, 'Black')
                screen.blit(battle_text_box, (battle_text_rect.x, battle_text_rect.y))
                screen.blit(battle_text1, (170, 470))
                screen.blit(battle_text2, (170, 490))

                #Check if move is a status move
                if enemy_selected_move.stat_change: # Stat Change is None if nonexistant
                    enemy_move_is_status_move = True

                #Calculate Damage Once
                if can_calc_dmg_heals:
                    damage_to_deal = calculate_dmg(enemy_selected_move, enemy_president, player_president) # Enemy will deal this damage to player
                    healing_to_do = calculate_heals(enemy_selected_move, enemy_president) # Player will heal this much health
                    can_calc_dmg_heals = False

                enemy_deals_damage = True # Player will now deal damage

            if player_deals_damage:
                #Reduce Width of Enemy Health Bar According to Damage Taken
                screen.blit(battle_text_box, (battle_text_rect.x, battle_text_rect.y))
                screen.blit(battle_text1, (170, 470))
                screen.blit(battle_text2, (170, 490))

                #Determine what stat to change if move effects status
                if player_move_is_status_move and count_damage_health < 100:
                    count_damage_health += 1
                    if count_damage_health >= 0:
                        if selected_move.stat_change == 'Attack Up':
                            battle_text1 = name_font.render(f"{player_president.name}'s attack", False, 'Black')
                            battle_text2 = name_font.render('increased!', False, 'Black')
                            if can_change_stats:
                                player_president.attack *= 1.5
                                can_change_stats = False
                        elif selected_move.stat_change == 'Defense Up':
                            battle_text1 = name_font.render(f"{player_president.name}'s defense", False, 'Black')
                            battle_text2 = name_font.render('increased!', False, 'Black')
                            if can_change_stats:
                                player_president.defense *= 1.5
                                can_change_stats = False
                        elif selected_move.stat_change == 'Speed Up':
                            battle_text1 = name_font.render(f"{player_president.name}'s speed", False, 'Black')
                            battle_text2 = name_font.render('increased!', False, 'Black')
                            if can_change_stats:
                                player_president.speed *= 1.5
                                can_change_stats = False
                        elif selected_move.stat_change == 'Attack Down':
                            battle_text1 = name_font.render(f"The opposing {enemy_president.name}'s", False, 'Black')
                            battle_text2 = name_font.render('attack decreased!', False, 'Black')
                            if can_change_stats:
                                enemy_president.attack = enemy_president.attack * (2 / 3)
                                can_change_stats = False
                        elif selected_move.stat_change == 'Defense Down':
                            battle_text1 = name_font.render(f"The opposing {enemy_president.name}'s", False, 'Black')
                            battle_text2 = name_font.render('defense decreased!', False, 'Black')
                            if can_change_stats:
                                enemy_president.defense = enemy_president.defense * (2 / 3)
                                can_change_stats = False
                        elif selected_move.stat_change == 'Speed Down':
                            battle_text1 = name_font.render(f"The opposing {enemy_president.name}'s", False, 'Black')
                            battle_text2 = name_font.render('speed decreased!', False, 'Black')
                            if can_change_stats:
                                enemy_president.speed = enemy_president.speed * (2 / 3)
                                can_change_stats = False
                        
                #Damage or Healing Move
                #Slowly reduces Enemy Health Bar Width
                elif (count_damage_health < damage_to_deal) and (count_damage_health >= 0) and (healing_to_do == 0):
                    if count_damage_health < damage_to_deal:
                        enemy_health_bar.width -= enemy_president.damage_healing_multiplier
                        if  enemy_president.health > 0:
                            enemy_president.health -= 1
                        count_damage_health += 1

                #Slowly increases Player Health Bar Width
                elif (count_damage_health < healing_to_do) and (count_damage_health >= 0):
                        if player_health_bar.width < 300:
                            player_health_bar.width += player_president.damage_healing_multiplier
                            if player_president.health < player_president.max_health:
                                player_president.health += 1
                        count_damage_health += 1

                #Provides a Buffer Before Damage or Stat Change
                elif count_damage_health < 0:
                    count_damage_health += 1

                #Transition to Next Phase
                else:
                    #If the Enemy Dies
                    if enemy_health_bar.width <= 0:
                        attacks = False
                        first_iteration = True
                        win = True

                    #If the Enemy Survives
                    else:
                        damage_to_deal = 0
                        count_damage_health = -100
                        turns_left -= 1
                        can_calc_dmg_heals = True
                        can_change_stats = True
                        player_move_is_status_move = False
                        if not turns_left:
                            turns_left = 2
                            attacks = False
                            player_deals_damage = False
                            enemy_deals_damage = False
                            can_calc_speed = True
                            turn_can_change = True
                            can_calc_dmg_heals = True
                            what_do = True
                        else:
                            player_deals_damage = False
                            enemy_deals_damage = True

            elif enemy_deals_damage:
                #Reduce Width of Player Health Bar According to Damage Taken
                screen.blit(battle_text_box, (battle_text_rect.x, battle_text_rect.y))
                screen.blit(battle_text1, (170, 470))
                screen.blit(battle_text2, (170, 490))

                #Determine what stat to change if move effects status
                if enemy_move_is_status_move and count_damage_health < 100:
                    print('test 1')
                    count_damage_health += 1
                    print(count_damage_health)
                    if count_damage_health >= 0:
                        print('test 2')
                        if enemy_selected_move.stat_change == 'Attack Up':
                            print('test 3')
                            battle_text1 = name_font.render(f"The opposing {enemy_president.name}'s", False, 'Black')
                            battle_text2 = name_font.render('attack increased!', False, 'Black')
                            if can_change_stats:
                                enemy_president.attack *= 1.5
                                can_change_stats = False
                        elif enemy_selected_move.stat_change == 'Defense Up':
                            battle_text1 = name_font.render(f"The opposing {enemy_president.name}'s", False, 'Black')
                            battle_text2 = name_font.render('defense increased!', False, 'Black')
                            if can_change_stats:
                                enemy_president.defense *= 1.5
                                can_change_stats = False
                        elif enemy_selected_move.stat_change == 'Speed Up':
                            battle_text1 = name_font.render(f"The opposing {enemy_president.name}'s", False, 'Black')
                            battle_text2 = name_font.render('speed increased!', False, 'Black')
                            if can_change_stats:
                                enemy_president.speed *= 1.5
                                can_change_stats = False
                        elif enemy_selected_move.stat_change == 'Attack Down':
                            battle_text1 = name_font.render(f"{player_president.name}'s attack", False, 'Black')
                            battle_text2 = name_font.render('decreased!', False, 'Black')
                            if can_change_stats:
                                player_president.attack = player_president.attack * (2 / 3)
                                can_change_stats = False
                        elif enemy_selected_move.stat_change == 'Defense Down':
                            battle_text1 = name_font.render(f"{player_president.name}'s defense", False, 'Black')
                            battle_text2 = name_font.render('decreased!', False, 'Black')
                            if can_change_stats:
                                player_president.defense = player_president.defense * (2 / 3)
                                can_change_stats = False
                        elif enemy_selected_move.stat_change == 'Speed Down':
                            battle_text1 = name_font.render(f"{player_president.name}'s speed", False, 'Black')
                            battle_text2 = name_font.render('decreased!', False, 'Black')
                            if can_change_stats:
                                player_president.speed = player_president.speed * (2 / 3)
                                can_change_stats = False

                #Slowly reduces Player Health Bar Width
                elif (count_damage_health < damage_to_deal) and (count_damage_health >= 0) and (healing_to_do == 0):
                    player_health_bar.width -= player_president.damage_healing_multiplier
                    if player_president.health > 0:
                        player_president.health -= 1 # Changes player health on card
                    count_damage_health += 1

                #Slowly increases Enemy Health Bar Width
                elif (count_damage_health < healing_to_do) and (count_damage_health >= 0):
                    if enemy_health_bar.width < 300:
                        enemy_health_bar.width += enemy_president.damage_healing_multiplier
                        if enemy_president.health < enemy_president.max_health:
                            enemy_president.health += 1 # Changes enemy health on card
                    count_damage_health += 1

                #Provides a Buffer Before Damage Reduction
                elif count_damage_health < 0:
                    count_damage_health += 1

                #Transition to Next Phase
                else:
                    #If the Player Dies
                    if player_health_bar.width <= 0:
                        attacks = False
                        lose = True

                    #If the Player Survives
                    else:
                        damage_to_deal = 0
                        count_damage_health = -100
                        turns_left -= 1
                        can_calc_dmg_heals = True
                        can_change_stats = True
                        enemy_move_is_status_move = False
                        if not turns_left:
                            turns_left = 2
                            attacks = False
                            enemy_deals_damage = False
                            player_deals_damage = False
                            can_calc_speed = True
                            turn_can_change = True
                            can_calc_dmg_heals = True
                            what_do = True
                        else:
                            enemy_deals_damage = False
                            player_deals_damage = True

        #Displays a Win Message
        elif win:
            if first_iteration:
                battle_music.stop()
                random.choice(VICTORY_MUSIC).play()
                first_iteration = False
            if enemy_president.rect.y < 620:
                enemy_president.move_down()

            battle_text1 = name_font.render('Congradulations! You Won!', False, 'Black')
            screen.blit(battle_text_box, (battle_text_rect.x, battle_text_rect.y))
            screen.blit(battle_text1, (170, 470))
            player_president.stat_reset()
            enemy_president.stat_reset()
        
        #Diplays a Loss Message
        elif lose:
            if player_president.rect.y < 620:
                player_president.move_down()

            battle_text1 = name_font.render('Unfortunate. You Lost.', False, 'Black')
            screen.blit(battle_text_box, (battle_text_rect.x, battle_text_rect.y))
            screen.blit(battle_text1, (170, 470))
            player_president.stat_reset()
            enemy_president.stat_reset()

 
    pygame.display.update()
    clock.tick(60)
