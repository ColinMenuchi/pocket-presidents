import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_surface = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
        player_surface2 = pygame.image.load('graphics/player_walk_2.png').convert_alpha()
        self.player_walk = [player_surface, player_surface2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 512))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.4)
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if game_active and keys[pygame.K_SPACE] and self.rect.bottom >= 512:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 512:
            self.rect.bottom = 512

    def animation_state(self):
        if self.rect.bottom < 512:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == 'fly':
            fly_frame_1 = pygame.image.load('graphics/Fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load('graphics/Fly2.png')
            self.frames = [fly_frame_1, fly_frame_2]
            self.obstacle_type = 'fly'
            self.speed_list = [6, 10, 12]
            self.speed = choice(self.speed_list)
            y_pos = 362
        else:
            snail_frame_1 = pygame.image.load('graphics/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('graphics/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            self.obstacle_type = 'snail'
            self.speed_list = [4, 6]
            self.speed = choice(self.speed_list)
            y_pos = 512
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        #Obstacle Movement
        if self.obstacle_type == 'fly':
            self.rect.x -= self.speed
        else:
            self.rect.x -= self.speed
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time:,}', False, (255, 255, 255))
    score_rect = score_surface.get_rect(center = (800, 75))
    if game_active:
        screen.blit(score_surface, score_rect)
    return current_time


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True


#Initialize PyGame, Instantiate Display, Clock, and Font
pygame.init() # initializes pygame
screen = pygame.display.set_mode((1000, 600)) # tuple(width, height) of display window
pygame.display.set_caption("Runner") # Sets title of display window
clock = pygame.time.Clock() # Clock object controls fps
test_font = pygame.font.Font(None, 50) # Creates a font that can be used for text (Font_File, Size)
start_time = 0
score = 0
background_music = pygame.mixer.Sound('audio/music.wav')
background_music.play(loops = -1)

#Creates a group that contains a sprite of the player
player = pygame.sprite.GroupSingle()
player.add(Player())

#Creates a group that contains sptries of the obstacles
obstacle_group = pygame.sprite.Group()

#Game States
game_active = False

#Sky & Ground Surfaces
sky_surface = pygame.image.load('graphics/pixel_night_sky.jpeg').convert_alpha()
ground_surface = pygame.image.load('graphics/pixel_ground.jpeg').convert_alpha() # Loads an image we want to display later

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
        
        if not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
        
        if game_active:
            #Checking Obstacle Spawn Updates
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail'])))
    
    if game_active:
       
        #Display Sky & Ground
        screen.blit(ground_surface, (0, 150))
        screen.blit(sky_surface, (0, 0)) # Places passed surface on the display at given coordinates

        #Draw and update player
        player.draw(screen)
        player.update()

        #Draw and update obstacles
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        #Collision
        game_active = collision_sprite()

        #Displaying the Score in game    
        score = display_score()
    
    #Displays Start/Game Over Screen
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand_scaled, player_stand_rect)

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
