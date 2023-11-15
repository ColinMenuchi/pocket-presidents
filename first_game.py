import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time:,}', False, (255, 255, 255))
    score_rect = score_surface.get_rect(center = (800, 75))
    if game_active:
        screen.blit(score_surface, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 512:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        #Changes the list to include only obstacles whose
        #x values are greater than zero.
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else:
        return []


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


def player_animation():
    #Play walking animation if the player is on floor
    #Display the jump surface when player is not on floor
    global player_surface, player_index
    
    if player_rect.bottom < 512:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]


#Initialize PyGame, Instantiate Display, Clock, and Font
pygame.init() # initializes pygame
screen = pygame.display.set_mode((1000, 600)) # tuple(width, height) of display window
pygame.display.set_caption("Runner") # Sets title of display window
clock = pygame.time.Clock() # Clock object controls fps
test_font = pygame.font.Font(None, 50) # Creates a font that can be used for text (Font_File, Size)
start_time = 0
score = 0

#Game States
game_active = False

#Sky & Ground Surfaces
sky_surface = pygame.image.load('graphics/pixel_night_sky.jpeg').convert_alpha()
ground_surface = pygame.image.load('graphics/pixel_ground.jpeg').convert_alpha() # Loads an image we want to display later

#Snail
snail_frame_1 = pygame.image.load('graphics/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]


#Fly
fly_frame_1 = pygame.image.load('graphics/Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('graphics/Fly2.png')
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]


obstacle_rect_list = []

#Player Surface & Rectangle
player_surface = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
player_surface2 = pygame.image.load('graphics/player_walk_2.png').convert_alpha()
player_walk = [player_surface, player_surface2]
player_index = 0
player_jump = pygame.image.load('graphics/jump.png').convert_alpha()
player_walk_animation = player_walk[player_index]

player_rect = player_surface.get_rect(midbottom = (80, 512))



#Creating Gravity Like Isaac Newton
player_gravity = 0

#Intro Screen
player_stand = pygame.image.load('graphics/player_stand.png').convert_alpha()
player_stand_scaled = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand_scaled.get_rect(center = (500, 300))

game_name = test_font.render('Astro Run', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (500, 75))

game_message = test_font.render('Press Space To Run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (500, 500))

#Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 500)

#Game Loop
while True:
    for event in pygame.event.get(): # loops through all game events (player input, etc.)
        if event == pygame.QUIT:
            pygame.quit() # uninitializes pygame
            exit()
        
        if game_active:
            #Jump By Clicking The Player Character
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            #Jump By Pressing Space and On Ground
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 512:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
        
        if game_active:
            #Checking Obstacle Spawn Updates
            if event.type == obstacle_timer:
                if randint(0, 1):
                    obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900, 1100), 512)))
                else: 
                    obstacle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900, 1100), 362)))
            
            #Checking Obstacle Animation Updates
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: 
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]

    if game_active:
       
        #Display Sky & Ground
        screen.blit(ground_surface, (0, 150))
        screen.blit(sky_surface, (0, 0)) # places passed surface on the display at given coordinates

        #Player, Gravity, Floor
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 512:
            player_rect.bottom = 512
        player_animation()
        screen.blit(player_surface, player_rect)

        #Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        #Collision
        game_active = collisions(player_rect, obstacle_rect_list)
            
        score = display_score()
    
    #Displays Start/Game Over Screen
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand_scaled, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.y = 512
        player_gravity = 0

        score_message = test_font.render(f'Your Score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (500, 500))

        screen.blit(game_name, game_name_rect)

        #If no score, display message, otherwise display score
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

        display_score()

    pygame.display.update() # updates display window
    clock.tick(60) # tells pygame this loop should not run faster than 60fps
