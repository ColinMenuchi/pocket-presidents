"""
Game Developed By Colin Menuchi
cmenuchi@uvm.edu
Project For CS1210-A
Pocket Presidents / Pokemon Left & Right
Pocket Presidents is a turn based game based off of the popular website
Pokemon Showdown. Build a team of presidents and see if you can defend
the constitution better than your opponent. Or don't. Not all presidents
were known for that *wink* *wink* *nudge* nudge*.
"""
import pygame
from president import President, GeorgeWashington, AbrahamLincoln, BillClinton, Obama, DonaldTrump, JoeBiden
from button import Button
from move import Move
from battle import what_will_you_do, are_you_sure, compare_speed, calculate_dmg, calculate_heals
import random
from sys import exit


def refill_enemy_choices(enemy_team_, enemy_choices_):
    for president in enemy_team_:
        enemy_choices_.append(president)


#Initializing Pygame and Game Screen
pygame.init()
screen = pygame.display.set_mode((1000, 570))
pygame.display.set_caption('Pocket Presidents')
clock = pygame.time.Clock()

#Creating the Fonts Used for Displaying Text in Game
main_font = pygame.font.Font(None, 50)
name_font = pygame.font.Font(None, 35)
title_font = pygame.font.Font(None, 100)
move_font = pygame.font.Font(None, 30)

#Instantiate Enemy and Enemy Sprites
enemy_choices = [President('enemy', 'George Washington'),
              President('enemy', 'Abraham Lincoln'),
              President('enemy', 'Bill Clinton'),
              President('enemy', 'Obama'),
              President('enemy', 'Donald Trump'),
              President('enemy', 'Joe Biden')] # List that holds presidents the opponent can pick from

enemy_team = [] # Will hold the presidents on the enemy's team
enemy_president = enemy_choices.pop(random.randint(0, 5)) # enemy_president resident is used to represent the enemy character in calculations.

enemy_team.append(enemy_choices.pop(random.randint(0, 4))) # append presidents from enemy_choices to enemy_team
enemy_team.append(enemy_choices.pop(random.randint(0, 3))) # Use .pop() in this process so enemy cannot have repeat presidents on their team.

first_enemy_president = pygame.sprite.GroupSingle() # Create a sprite Group to hold each of the enemy's presidents
second_enemy_president = pygame.sprite.GroupSingle()
third_enemy_president = pygame.sprite.GroupSingle()

first_enemy_president.add(enemy_president) # Add the presidents on the enemy's team to the sprite groups
second_enemy_president.add(enemy_team[0]) # Adding them to the sprite groups lets them be displayed on screen.
third_enemy_president.add(enemy_team[1])

refill_enemy_choices(enemy_team, enemy_choices) # Important if player chooses to player multiple times

#Object Oriented Player Instantiation
player_choices = [President('player', 'George Washington'),
              President('player', 'Abraham Lincoln'),
              President('player', 'Bill Clinton'),
              President('player', 'Obama'),
              President('player', 'Donald Trump'),
              President('player', 'Joe Biden')] # List that holds presidents the player can pick from

player_team = [] # Will hold the presidents on the player's team
player_president = None # To Be Used as the player character in calculations
first_player_president = pygame.sprite.GroupSingle()
second_player_president = pygame.sprite.GroupSingle()
third_player_president = pygame.sprite.GroupSingle() # Used as the player sprite

#Buttons:
button_audio = pygame.mixer.Sound('audio/battle_button_click.mp3') # Audio used for most buttons
#Home Screen Start Button
start_button_sound = pygame.mixer.Sound('audio/start_button_click.mp3')
start_button_image = pygame.image.load('graphics/start_button1.png').convert_alpha()
start_button_hover = pygame.image.load('graphics/start_button2.png').convert_alpha()
start_button = Button(500, 285, start_button_image, screen, 1, start_button_sound)
#Character Select Screen Buttons:
#Scroll Buttons
left_arrow_image = pygame.image.load('graphics/button_left_arrow1.png').convert_alpha()
left_arrow_hover = pygame.image.load('graphics/button_left_arrow2.png').convert_alpha()
right_arrow_image = pygame.image.load('graphics/button_right_arrow1.png').convert_alpha()
right_arrow_hover = pygame.image.load('graphics/button_right_arrow2.png').convert_alpha()
left_button = Button(50, 285, left_arrow_image, screen, 1, button_audio)
right_button = Button(950, 285, right_arrow_image, screen, 1, button_audio)
#Select Button
select_button_image = pygame.image.load('graphics/button_select1.png').convert_alpha()
select_button_hover = pygame.image.load('graphics/button_select2.png').convert_alpha()
select_button = Button(290, 150, select_button_image, screen, 1, button_audio)
#Unselect Button
unselect_button_image = pygame.image.load('graphics/button_unselect1.png').convert_alpha()
unselect_button_hover = pygame.image.load('graphics/button_unselect2.png').convert_alpha()
unselect_button = Button(760, 150, unselect_button_image, screen, 1, button_audio)
#Go Button
go_button_image = pygame.image.load('graphics/button_go1.png').convert_alpha()
go_button_hover = pygame.image.load('graphics/button_go2.png').convert_alpha()
go_button = Button(500, 285, go_button_image, screen, 1, start_button_sound)

#Battle Menu Buttons:
#Fight Button:
fight_button_image = pygame.image.load('graphics/button_fight1.png').convert_alpha()
fight_hover_button = pygame.image.load('graphics/button_fight2.png').convert_alpha()
fight_button = Button(850, 500, fight_button_image, screen, 1, button_audio)
#Move1 Button
move1_button_image = pygame.image.load('graphics/button_move1-1.png').convert_alpha()
move1_button_hover = pygame.image.load('graphics/button_move1-2.png').convert_alpha()
move1_button = Button(610, 485, move1_button_image, screen, 1, button_audio)

#Move2 Button
move2_button_image = pygame.image.load('graphics/button_move2-1.png').convert_alpha()
move2_button_hover = pygame.image.load('graphics/button_move2-2.png').convert_alpha()
move2_button = Button(810, 485, move2_button_image, screen, 1, button_audio)

#Move3 Button
move3_button_image = pygame.image.load('graphics/button_move3-1.png').convert_alpha()
move3_button_hover = pygame.image.load('graphics/button_move3-2.png').convert_alpha()
move3_button = Button(610, 542, move3_button_image, screen, 1, button_audio)

#Move4 Button
move4_button_image = pygame.image.load('graphics/button_move4-1.png').convert_alpha()
move4_button_hover = pygame.image.load('graphics/button_move4-2.png').convert_alpha()
move4_button = Button(810, 542, move4_button_image, screen, 1, button_audio)

#Back Button
back_button_image = pygame.image.load('graphics/button_back1.png').convert_alpha()
back_button_image = pygame.transform.rotozoom(back_button_image, 0, 0.6)
back_button_hover = pygame.image.load('graphics/button_back2.png').convert_alpha()
back_button_hover = pygame.transform.rotozoom(back_button_hover, 0, 0.6)
back_button = Button(935, 510, back_button_image, screen, 1, button_audio)

#Confirm Actions Button
confirm_button_image = pygame.image.load('graphics/button_confirm1.png').convert_alpha()
confirm_button_hover = pygame.image.load('graphics/button_confirm2.png').convert_alpha()
confirm_button = Button(800, 510, confirm_button_image, screen, 1, button_audio)

#Menu Screen:
#Pokemon Title Card
menu_title = pygame.image.load('graphics/pokemon_title.png').convert_alpha()
menu_title = pygame.transform.rotozoom(menu_title, 0, 0.18)
menu_title_rect = menu_title.get_rect(center = (500, 600))

#Menu Background
menu_background = pygame.image.load('graphics/menu_background.jpeg').convert_alpha()
menu_background = pygame.transform.rotozoom(menu_background, 0, 1.025)

#Game Name Title Card
game_name_box1 = pygame.Rect((145, 410), (140, 60))
game_name_box2 = pygame.Rect((690, 410), (180, 72))
game_name_1 = title_font.render('Left', False, 'Red')
game_name_2 = title_font.render('Right', False, 'Blue')

#Ampersand Title Card
ampersand_box = pygame.Rect((430, 360), (140, 140))
ampersand = pygame.image.load('graphics/ampersand.png').convert_alpha()
ampersand = pygame.transform.rotozoom(ampersand, 0, 0.09)
ampersand_rect = ampersand.get_rect(center = (500, 430))

#-President Select Screen-
#Background
president_select_music = pygame.mixer.Sound('audio/spb.mp3')
president_select_music.set_volume(0.6)
can_play_president_select_music = True
team_size = 0
build_your_team = title_font.render(f'Build Your Team! ({team_size}/3)', False, 'White')
build_box = pygame.Rect((100, 25), (800, 75))
oval_office = pygame.image.load('graphics/oval_office.jpeg').convert_alpha()
oval_office = pygame.transform.rotozoom(oval_office, 0, 0.17)
oval_office_rect = oval_office.get_rect()
oval_office_rect.center = (500, 285)
#Presidents
team = []
current_president = player_choices[0]
president_name_box = pygame.Rect((0, 0), (240, 75))
president_name_box.center = (525, 155)
president_number = 0 # Used to determine which president is on screen
selection_timer = 100 # Needed to prevent unselect button from being pressed right after the select button.

#-Battle Screen-
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
enemy_name = name_font.render(enemy_president.name, False, 'Black')
#Health on Boxes
enemy_health_card = name_font.render(f'HP: {enemy_president.health}'
                                     f'/{enemy_president.max_health}', False, 'Black')
#Card that Displays Text in Battle (Ex: Obama used <INSERT_MOVE_NAME_HERE>!)
battle_text_box = pygame.image.load('graphics/battle_text_box.png').convert_alpha()
battle_text_rect = battle_text_box.get_rect()
battle_text_rect.center = (390, 505)

#Music & Sounds
menu_music = pygame.mixer.Sound('audio/menu_song.mp3') # Menu Music
possible_battle_musics = [pygame.mixer.Sound('audio/Battle-Chairman_Rose.flac'),
                pygame.mixer.Sound('audio/Battle-Marnie.flac'),
                pygame.mixer.Sound('audio/B&W-Battle_Gym_Leader.mp3'),
                pygame.mixer.Sound('audio/B&W-Battle_Wild.mp3'),
                pygame.mixer.Sound('audio/B&W-Battle_Team_Plasma.mp3')]
battle_music = random.choice(possible_battle_musics) # To be chosen randomly later
battle_music.set_volume(0.8)
possible_victory_musics = [pygame.mixer.Sound('audio/Marnie-Victory.flac'),
                 pygame.mixer.Sound('audio/B&W-Team_Plasma_Victory.mp3')]
victory_music = random.choice(possible_victory_musics)
defeat_music = pygame.mixer.Sound('audio/spb_piano.mp3')
heal_sound = pygame.mixer.Sound('audio/heal_sound.mp3')
stat_raise_sound = pygame.mixer.Sound('audio/stat_raise.mp3')
stat_drop_sound = pygame.mixer.Sound('audio/stat_drop.mp3')

#Game States
home_screen = True # True if the home screen is being displayed
president_select = False # True if the president select screen is being displayed
battle = False # True if the battle screen is being displayed
what_do = True # True if the player is being asked what they'll do in battle
fight = False # True if the player has clicked the fight button
confirmation = False # True when the player selects a move. Asks them to confirm actions
attacks = False # True when the player clicks confirm button. Commences attacks in battle.
player_deals_damage = False # True if it is the player's turn to use a move in battle.
enemy_deals_damage = False # True if it is the enemy's turn to use a move in battle.
next_player_president = False # True if the player's president fainted and they have to swap to a new one.
next_enemy_president = False # True if the enemy's president fainted and they have to swap to a new one.
win = False # True if the player defeated all of the enemy's presidents and won.
lose = False # True if the enemy defeated all of the player's presidents.

#Trackers & Determinators For Battle
selected_move = None # Used to track the player's move selection during battle.
enemy_moves = enemy_president.move_list # Used to hold the enemy's moves.
enemy_selected_move = None # Used to track the enemy's move selection during battle.
damage_to_deal = 0 # Used to hold the damage that must be dealt in a turn.
healing_to_do = 0 # Used to hold the healing that must be done in a turn.
can_play_heal_sound = True # Used so the heal sound is only played once when a heal move is used.
count_damage_health = -100 # Used to track the damage or healing done in combat. Also used as a timer so text is displayed for longer in battle.
count_president_health = 0 # Used to increment/decrement health on a president's name card in battle.
can_calc_dmg_heals = True # Used to only calculate damage and heals once each turn.
can_calc_speed = True # Used so speed is only calculated once before attacks commence in battle.
player_is_faster = None # Used to determine who moves first in battle.
turns_left = 2 # Used to prevent Player & Enemy from continuously damaging one anthother by giving them each one turn per move selection.
turn_can_change = True # Used to properly swap turns in battle.
first_iteration = True # Needed so music won't loop over itself.
player_move_is_status_move = False # Used to determine if a player move affects stats rather than hitpoints.
enemy_move_is_status_move = False # Used to determine if an enemy move affects stats rather than hitpoints.
can_change_stats = True # Used to only change a president's stats once and only play stat change sound once.
running = True # Conventionally used variable for a pygame game loop. Should always equal True.

#Game Loop
while running:
    #Checking for every pygame event:
    for event in pygame.event.get():
        #Close PyGame
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        #Checking for Possible Home Screen Events
        if home_screen:
            #Transition to President Select Screen
            if start_button.is_clicked() and home_screen:
                menu_music.fadeout(1000) # Fades out menu music over time passed (miliseconds)
                first_iteration = True
                home_screen = False
                president_select = True

        #Checking for Possible President Select Screen Events
        elif president_select:
            #If the Left Arrow Button is Clicked
            if left_button.is_clicked() and president_select and team_size < 3:
                president_number -= 1
                if president_number == -1:
                    president_number = 5
            #If the Right Arrow Button is Clicked
            if right_button.is_clicked() and president_select and team_size < 3:
                president_number += 1
                if president_number == 6:
                    president_number = 0

            #If a President's Select Button is Clicked
            if select_button.is_clicked() and not current_president.is_selected and team_size < 3:
                current_president.is_selected = True
                player_team.append(current_president)
                team_size += 1
            #If a President's Unselect Button is Clicked
            if unselect_button.is_clicked() and current_president.is_selected and team_size > 0:
                current_president.is_selected = False
                player_team.pop()
                team_size -= 1

            #If the Go Button is Clicked (Transition from President Select to Battle)
            if go_button.is_clicked() and team_size == 3:
                president_select_music.stop()
                #Add the Selected Presidents to the Predefined Sprite Groups
                first_player_president.add(player_team[0])
                second_player_president.add(player_team[1])
                third_player_president.add(player_team[2])
                #Assign Player President (Object that Represents the Player) and Player Sprite (Player Character's Image on Screen)
                player_president = player_team[0]
                player_team.pop(0) # player_team now only holds the presidents not currently battling
                #Assign Text for the Move Buttons
                move1_text = move_font.render(player_president.move_list[0].name, False, 'Black')
                move2_text = move_font.render(player_president.move_list[1].name, False, 'Black')
                move3_text = move_font.render(player_president.move_list[2].name, False, 'Black')
                move4_text = move_font.render(player_president.move_list[3].name, False, 'Black')
                #Assign Text for the Player Card Displayed in Battle
                player_name = name_font.render(player_president.name, False, 'Black')
                player_health_card = name_font.render(f'HP: {player_president.health}/{player_president.max_health}', False, 'Black')
                #Change Game State from President Select to Battle
                president_select = False
                battle = True
                
        #CHecking for Possible Battle Menu Events
        elif battle:
            #Play Battle Music
            if first_iteration:
                battle_music.play(loops=-1)
                first_iteration = False
            #Checking for Possible "What Will You Do" Events
            if what_do:
                #
                if fight_button.is_clicked() and what_do:
                    what_do = False
                    fight = True
            
            elif fight:
                if move1_button.is_clicked() and fight:
                    selected_move = player_president.move_list[0]
                    fight = False
                    confirmation = True
                elif move2_button.is_clicked() and fight:
                    selected_move = player_president.move_list[1]
                    fight = False
                    confirmation = True
                elif move3_button.is_clicked() and fight:
                    selected_move = player_president.move_list[2]
                    fight = False
                    confirmation = True
                elif move4_button.is_clicked() and fight:
                    selected_move = player_president.move_list[3]
                    fight = False
                    confirmation = True
                elif back_button.is_clicked() and fight:
                    selected_move = None
                    fight = False
                    what_do = True
            elif confirmation:
                if confirm_button.is_clicked() and confirmation:
                    confirmation = False
                    attacks = True
                    enemy_selected_move = random.choice(enemy_moves)
                elif back_button.is_clicked() and confirmation:
                    confirmation = False
                    fight = True

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
        #President Select Screen Background
        if can_play_president_select_music:
            president_select_music.play(loops=-1)
            can_play_president_select_music = False
        screen.blit(oval_office, oval_office_rect)
        pygame.draw.rect(screen, 'Black', build_box)
        build_your_team = title_font.render(f'Build Your Team! ({team_size}/3)', False, 'White')
        screen.blit(build_your_team, (110, 30))
        left_button.draw(left_arrow_image, left_arrow_hover)
        right_button.draw(right_arrow_image, right_arrow_hover)

        #Determination for Which Buttons to Display
        if current_president.is_selected:
            unselect_button.draw(unselect_button_image, unselect_button_hover)
        else:
            select_button.draw(select_button_image, select_button_hover)

        #Logic For Scrolling Through President Select Menu
        if president_number == 0:
            current_president = player_choices[0]
            president_name = name_font.render(current_president.name, False, 'Black')
            pygame.draw.rect(screen, 'White', president_name_box)
            screen.blit(president_name, (410, 140))
            screen.blit(GeorgeWashington('player').selection_image, (345, 175))

        elif president_number == 1:
            current_president = player_choices[1]
            president_name = name_font.render(current_president.name, False, 'Black')
            pygame.draw.rect(screen, 'White', president_name_box)
            screen.blit(president_name, (410, 140))
            screen.blit(AbrahamLincoln('player').selection_image, (345, 170))

        elif president_number == 2:
            current_president = player_choices[2]
            president_name = name_font.render(current_president.name, False, 'Black')
            pygame.draw.rect(screen, 'White', president_name_box)
            screen.blit(president_name, (410, 140))
            screen.blit(BillClinton('player').selection_image, (345, 170))

        elif president_number == 3:
            current_president = player_choices[3]
            president_name = name_font.render(current_president.name, False, 'Black')
            pygame.draw.rect(screen, 'White', president_name_box)
            screen.blit(president_name, (410, 140))
            screen.blit(Obama('player').selection_image, (345, 170))

        elif president_number == 4:
            current_president = player_choices[4]
            president_name = name_font.render(current_president.name, False, 'Black')
            pygame.draw.rect(screen, 'White', president_name_box)
            screen.blit(president_name, (410, 140))
            screen.blit(DonaldTrump('player').selection_image, (345, 170))

        elif president_number == 5:
            current_president = player_choices[5]
            president_name = name_font.render(current_president.name, False, 'Black')
            pygame.draw.rect(screen, 'White', president_name_box)
            screen.blit(president_name, (410, 140))
            screen.blit(JoeBiden('player').selection_image, (345, 170))

        if team_size == 3:
            go_button.draw(go_button_image, go_button_hover)

    elif battle: # Battle Screen

        #Places the Battlefiled On the Screen
        screen.blit(battle_field, (0, 0))
        
        #Determines which President to Display for Eeach Team
        if len(enemy_team) == 2:
            first_enemy_president.draw(screen)
            if not win and not next_enemy_president:
                first_enemy_president.update()
        elif len(enemy_team) == 1:
            second_enemy_president.draw(screen)
            if not win and not next_enemy_president:
                second_enemy_president.update()
        else:
            third_enemy_president.draw(screen)
            if not win and not next_enemy_president:
                third_enemy_president.update()

        if len(player_team) == 2:
            first_player_president.draw(screen)
            if not lose and not next_player_president:
                first_player_president.update()
        elif len(player_team) == 1:
            second_player_president.draw(screen)
            if not lose and not next_player_president:
                second_player_president.update()
        else:
            third_player_president.draw(screen)
            if not lose and not next_player_president:
                third_player_president.update()

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

        #Display Battle Menu
        if what_do:
            what_will_you_do(screen) # Function from battle file
            fight_button.draw(fight_button_image, fight_hover_button)

        #Player Selects a Move to Use in Battle:
        elif fight:
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

        elif attacks: # Attack Sequence
            #Determine Who Moves First:
            if turns_left == 2 and can_calc_speed:
                player_is_faster = compare_speed \
                    (player_president, enemy_president)
                can_calc_speed = False
            elif turns_left == 1 and turn_can_change:
                player_is_faster = not player_is_faster
                turn_can_change = False
            
            if player_is_faster:
            #-Display Message of Move Being Used-
            #If move isn't stat changing or provide a time buffer if it is
                if not player_move_is_status_move or count_damage_health < 0:
                    battle_text1 = name_font.render(f'{player_president.name} used ', False, 'Black')
                    battle_text2 = name_font.render (f'{selected_move.name}!', False, 'Black')
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
                                stat_raise_sound.play()
                                can_change_stats = False
                        elif selected_move.stat_change == 'Defense Up':
                            battle_text1 = name_font.render(f"{player_president.name}'s defense", False, 'Black')
                            battle_text2 = name_font.render('increased!', False, 'Black')
                            if can_change_stats:
                                player_president.defense *= 1.5
                                stat_raise_sound.play()
                                can_change_stats = False
                        elif selected_move.stat_change == 'Speed Up':
                            battle_text1 = name_font.render(f"{player_president.name}'s speed", False, 'Black')
                            battle_text2 = name_font.render('increased!', False, 'Black')
                            if can_change_stats:
                                player_president.speed *= 1.5
                                stat_raise_sound.play()
                                can_change_stats = False
                        elif selected_move.stat_change == 'Attack Down':
                            battle_text1 = name_font.render(f"The opposing {enemy_president.name}'s", False, 'Black')
                            battle_text2 = name_font.render('attack decreased!', False, 'Black')
                            if can_change_stats:
                                enemy_president.attack = enemy_president.attack * (2 / 3)
                                stat_drop_sound.play()
                                can_change_stats = False
                        elif selected_move.stat_change == 'Defense Down':
                            battle_text1 = name_font.render(f"The opposing {enemy_president.name}'s", False, 'Black')
                            battle_text2 = name_font.render('defense decreased!', False, 'Black')
                            if can_change_stats:
                                enemy_president.defense = enemy_president.defense * (2 / 3)
                                stat_drop_sound.play()
                                can_change_stats = False
                        elif selected_move.stat_change == 'Speed Down':
                            battle_text1 = name_font.render(f"The opposing {enemy_president.name}'s", False, 'Black')
                            battle_text2 = name_font.render('speed decreased!', False, 'Black')
                            if can_change_stats:
                                enemy_president.speed = enemy_president.speed * (2 / 3)
                                stat_drop_sound.play()
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

                #If healing move, play sound once
                elif healing_to_do and can_play_heal_sound:
                    if player_health_bar.width < 300:
                        heal_sound.play()
                    can_play_heal_sound = False
                    count_damage_health += 1

                #Provides a Buffer Before Damage or Stat Change
                elif count_damage_health < 0:
                    count_damage_health += 1

                #Transition to Next Phase
                else:
                    #If the Enemy Dies
                    if enemy_health_bar.width <= 0:
                        attacks = False
                        player_deals_damage = False
                        enemy_deals_damage = False
                        if len(enemy_team) == 0:
                            first_iteration = True
                            win = True
                        else:
                            attacks = False
                            next_enemy_president = True

                    #If the Enemy Survives
                    else:
                        damage_to_deal = 0
                        count_damage_health = -100
                        turns_left -= 1
                        can_calc_dmg_heals = True
                        can_change_stats = True
                        can_play_heal_sound = True
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
                    count_damage_health += 1
                    if count_damage_health >= 0:
                        if enemy_selected_move.stat_change == 'Attack Up':
                            battle_text1 = name_font.render(f"The opposing {enemy_president.name}'s", False, 'Black')
                            battle_text2 = name_font.render('attack increased!', False, 'Black')
                            if can_change_stats:
                                enemy_president.attack *= 1.5
                                stat_raise_sound.play()
                                can_change_stats = False
                        elif enemy_selected_move.stat_change == 'Defense Up':
                            battle_text1 = name_font.render(f"The opposing {enemy_president.name}'s", False, 'Black')
                            battle_text2 = name_font.render('defense increased!', False, 'Black')
                            if can_change_stats:
                                enemy_president.defense *= 1.5
                                stat_raise_sound.play()
                                can_change_stats = False
                        elif enemy_selected_move.stat_change == 'Speed Up':
                            battle_text1 = name_font.render(f"The opposing {enemy_president.name}'s", False, 'Black')
                            battle_text2 = name_font.render('speed increased!', False, 'Black')
                            if can_change_stats:
                                enemy_president.speed *= 1.5
                                stat_raise_sound.play()
                                can_change_stats = False
                        elif enemy_selected_move.stat_change == 'Attack Down':
                            battle_text1 = name_font.render(f"{player_president.name}'s attack", False, 'Black')
                            battle_text2 = name_font.render('decreased!', False, 'Black')
                            if can_change_stats:
                                player_president.attack = player_president.attack * (2 / 3)
                                stat_drop_sound.play()
                                can_change_stats = False
                        elif enemy_selected_move.stat_change == 'Defense Down':
                            battle_text1 = name_font.render(f"{player_president.name}'s defense", False, 'Black')
                            battle_text2 = name_font.render('decreased!', False, 'Black')
                            if can_change_stats:
                                player_president.defense = player_president.defense * (2 / 3)
                                stat_drop_sound.play()
                                can_change_stats = False
                        elif enemy_selected_move.stat_change == 'Speed Down':
                            battle_text1 = name_font.render(f"{player_president.name}'s speed", False, 'Black')
                            battle_text2 = name_font.render('decreased!', False, 'Black')
                            if can_change_stats:
                                player_president.speed = player_president.speed * (2 / 3)
                                stat_drop_sound.play()
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

                #If healing move, play sound once
                elif healing_to_do and can_play_heal_sound:
                    if enemy_health_bar.width < 300:
                        heal_sound.play()
                    can_play_heal_sound = False
                    count_damage_health += 1

                #Provides a Buffer Before Damage Reduction
                elif count_damage_health < 0:
                    count_damage_health += 1

                #Transition to Next Phase
                else:
                    #If the Player Dies
                    if player_health_bar.width <= 0:
                        attacks = False
                        player_deals_damage = False
                        enemy_deals_damage = False
                        if len(player_team) == 0:
                            lose = True
                        else:
                            attacks = False
                            next_player_president = True

                    #If the Player Survives
                    else:
                        damage_to_deal = 0
                        count_damage_health = -100
                        turns_left -= 1
                        can_calc_dmg_heals = True
                        can_change_stats = True
                        can_play_heal_sound = True
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
            
        #Swap in Player's Next President
        elif next_player_president:
            battle_text1 = name_font.render(f'{player_president.name} fainted!', False, 'Black')
            screen.blit(battle_text_box, (battle_text_rect.x, battle_text_rect.y))
            screen.blit(battle_text1, (170, 470))

            if player_president.rect.y < 620:
                player_president.move_down()
            else:
                damage_to_deal = 0
                count_damage_health = -100
                turns_left = 2
                can_calc_dmg_heals = True
                can_change_stats = True
                can_play_heal_sound = True
                enemy_move_is_status_move = False
                enemy_deals_damage = False
                player_deals_damage = False
                can_calc_speed = True
                turn_can_change = True
                can_calc_dmg_heals = True
                what_do = True
                next_player_president = False
                player_president = player_team[0]
                player_team.pop(0)
                player_health_bar.width = 300
                move1_text = move_font.render(player_president.move_list[0].name, False, 'Black')
                move2_text = move_font.render(player_president.move_list[1].name, False, 'Black')
                move3_text = move_font.render(player_president.move_list[2].name, False, 'Black')
                move4_text = move_font.render(player_president.move_list[3].name, False, 'Black')
                player_name = name_font.render(player_president.name, False, 'Black')
                player_health_card = name_font.render(f'HP: {player_president.health}'
                                      f'/{player_president.max_health}', False, 'Black')

        #Swap in Enemy's Next President     
        elif next_enemy_president:
            battle_text1 = name_font.render(f'The opposing {enemy_president.name}', False, 'Black')
            battle_text2 = name_font.render('fainted!', False, 'Black')
            screen.blit(battle_text_box, (battle_text_rect.x, battle_text_rect.y))
            screen.blit(battle_text1, (170, 470))
            screen.blit(battle_text2, (170, 490))

            if enemy_president.rect.y < 620:
                enemy_president.move_down()
            else:
                #Reset Trackers
                damage_to_deal = 0
                count_damage_health = -100
                turns_left = 2
                can_calc_dmg_heals = True
                can_change_stats = True
                can_play_heal_sound = True
                enemy_move_is_status_move = False
                enemy_deals_damage = False
                player_deals_damage = False
                can_calc_speed = True
                turn_can_change = True
                can_calc_dmg_heals = True
                what_do = True
                next_enemy_president = False
                #Switch President On Screen
                enemy_president = enemy_team[0]
                enemy_team.pop(0)
                enemy_health_bar.width = 300
                enemy_moves = enemy_president.move_list
                enemy_name = name_font.render(enemy_president.name, False, 'Black')
                enemy_health_card = name_font.render(f'HP: {enemy_president.health}'
                                      f'/{enemy_president.max_health}', False, 'Black')

        #Displays a Win Message
        elif win:
            if first_iteration:
                battle_music.stop()
                victory_music.play()
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
            if first_iteration:
                battle_music.stop()
                defeat_music.play()

            if player_president.rect.y < 620:
                player_president.move_down()

            battle_text1 = name_font.render('Unfortunate. You Lost.', False, 'Black')
            screen.blit(battle_text_box, (battle_text_rect.x, battle_text_rect.y))
            screen.blit(battle_text1, (170, 470))
            player_president.stat_reset()
            enemy_president.stat_reset()

    pygame.display.update()
    clock.tick(60)
