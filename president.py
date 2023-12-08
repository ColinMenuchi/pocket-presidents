import pygame
from random import randint
from move import Move

class President(pygame.sprite.Sprite):
    def __init__(self, team, name):
        super().__init__()
        self.team = team
        self.name = name
        self.idle = []
        self.move_list = []
        self.animation_index = 0
        self.health = 0
        self.max_health = 0
        self.damage_healing_multiplier = 0 # Allows for dynamic health bars
        self.attack = 0
        self.defense = 0
        self.speed = 0
        self.is_selected = False
        #Presidential Sprite Creation
        #Determines Team
        if self.team == 'player':
            #Picks From Player Presidential Sprites
            match self.name:
                case 'Abraham Lincoln':
                    self.health = 100
                    self.max_health = 100
                    self.attack = 42.5
                    self.defense = 35
                    self.speed = 37.5
                    self.idle = AbrahamLincoln('player').idle
                    self.move_list = [Move('Emancipate', 0, 33, None), Move('Four Score', 20, 0, None),
                                      Move('Divided House', 25, 0, None), Move('For The Union', 0, 0, 'Attack Up')]

                case 'Bill Clinton':
                    self.health = 100
                    self.max_health = 100
                    self.attack = 30
                    self.defense = 42.5
                    self.speed = 40
                    self.idle = BillClinton('player').idle
                    self.move_list = [Move('Sign NAFTA', 0, 0, 'Attack Up'), Move('Ms. Lewinsky?', 0, 0, 'Defense Up'),
                                      Move('Send in Hillary', 30, 0, None), Move('Egg McMuffin', 0, 33, None)]

                case 'Donald Trump':
                    self.health = 150
                    self.max_health = 150
                    self.attack = 30
                    self.defense = 35
                    self.speed = 20
                    self.idle = DonaldTrump('player').idle
                    self.move_list = [Move("You're Fired", 20, 0, None), Move('Build a Wall', 0, 0, 'Defense Up'),
                                      Move('Fake News', 0, 0, 'Defense Down'), Move('Uuuuuuge', 0, 50, None)]

                case 'Joe Biden':
                    self.health = 150
                    self.max_health = 150
                    self.attack = 40
                    self.defense = 30
                    self.speed = 30
                    self.idle = JoeBiden('player').idle
                    self.move_list = [Move('Biden Blast', 25, 0, None), Move('Choclate Chip', 0, 50, None),
                                      Move('Sniff', 0, 0, 'Attack Down'), Move('Asufutimaeh-', 0, 0, 'Speed Up')]

                case 'Obama':
                    self.health = 100
                    self.max_health = 100
                    self.attack = 40
                    self.defense = 35
                    self.speed = 50
                    self.idle = Obama('player').idle
                    self.move_list = [Move('Obamacare', 0, 33, None), Move('Obamehameha', 25, 0, None),
                                      Move('Let Me Be Clear', 0, 0, 'Attack Up'), Move("Michelle Lunch", 0, 0, 'Defense Down')]
                    

                case 'George Washington':
                    self.health = 75
                    self.max_health = 75
                    self.attack = 50
                    self.defense = 40
                    self.speed = 60
                    self.idle = GeorgeWashington('player').idle
                    self.move_list = [Move('Cross Delaware', 0, 0, 'Attack Up'), Move('Tar and Feather', 0, 0, 'Speed Down'),
                                      Move('Valley Forge', 0, 50, None), Move('Bayonet Charge', 25, 0, None)]
                case _:
                    print('Invalid Name')
            
            self.image = self.idle[self.animation_index]
            self.screen_coords = (57, 160)
            self.rect = self.image.get_rect(topleft = self.screen_coords)
            self.original_x = self.rect.x

        elif self.team == 'enemy':
            #Picks From Enemy Presidential Sprites
            match self.name:
                case 'Abraham Lincoln':
                    self.health = 100
                    self.max_health = 100
                    self.attack = 42.5
                    self.defense = 35
                    self.speed = 37.5
                    self.idle = AbrahamLincoln('enemy').idle
                    self.move_list = [Move('Emancipate', 0, 33, None), Move('Four Score', 20, 0, None),
                                      Move('Divided House', 25, 0, None), Move('For The Union', 0, 0, 'Attack Up')]

                case 'Bill Clinton':
                    self.health = 100
                    self.max_health = 100
                    self.attack = 30
                    self.defense = 42.5
                    self.speed = 40
                    self.idle = BillClinton('enemy').idle
                    self.move_list = [Move('Sign NAFTA', 0, 0, 'Attack Up'), Move('Ms. Lewinsky?', 0, 0, 'Defense Up'),
                                      Move('Send in Hillary', 30, 0, None), Move('Egg McMuffin', 0, 33, None)]


                case 'Donald Trump':
                    self.health = 150
                    self.max_health = 150
                    self.attack = 30
                    self.defense = 35
                    self.speed = 20
                    self.idle = DonaldTrump('enemy').idle
                    self.move_list = [Move("You're Fired", 20, 0, None), Move('Build a Wall', 0, 0, 'Defense Up'),
                                      Move('Fake News', 0, 0, 'Defense Down'), Move('Uuuuuuge', 0, 50, None)]
                    
                case 'Joe Biden':
                    self.health = 150
                    self.max_health = 150
                    self.attack = 40
                    self.defense = 30
                    self.speed = 30
                    self.idle = JoeBiden('enemy').idle
                    self.move_list = [Move('Biden Blast', 25, 0, None), Move('Choclate Chip', 0, 50, None),
                                      Move('Sniff', 0, 0, 'Attack Down'), Move('Asufutimaeh-', 0, 0, 'Speed Up')]

                    
                case 'Obama':
                    self.health = 100
                    self.max_health = 100
                    self.attack = 40
                    self.defense = 35
                    self.speed = 50
                    self.idle = Obama('enemy').idle
                    self.move_list = [Move('Obamacare', 0, 33, None), Move('Obamehameha', 25, 0, None),
                                      Move('Let Me Be Clear', 0, 0, 'Attack Up'), Move("Michelle Lunches", 0, 0, 'Defense Down')]
                    

                case 'George Washington':
                    self.health = 75
                    self.max_health = 75
                    self.attack = 50
                    self.defense = 40
                    self.speed = 60
                    self.idle = GeorgeWashington('enemy').idle
                    self.move_list = [Move('Cross Delaware', 0, 0, 'Attack Up'), Move('Tar and Feather', 0, 0, 'Speed Down'),
                                      Move('Valley Forge', 0, 50, None), Move('Bayonet Charge', 25, 0, None)]
                    
            self.image = self.idle[self.animation_index]
            self.screen_coords = (630, 90)
            self.rect = self.image.get_rect(topleft = self.screen_coords)
            self.original_x = self.rect.x
        
        else:
            print('Invalid Team')
        
        self.damage_healing_multiplier = 300 / self.health
        self.base_stats = [self.health, self.attack, self.defense, self.speed]


    def animation_state(self):
        if not(self.animation_index == None):
            self.animation_index += 0.085
            if self.animation_index >= len(self.idle):
                self.animation_index = 0

            self.image = self.idle[int(self.animation_index)]
            self.rect = self.image.get_rect(topleft = self.screen_coords)

    def animation_pause(self):
        self.animation_index = None

    def animation_unpause(self):
        self.animation_index = 0.085

    def stat_reset(self):
        self.attack = self.base_stats[1]
        self.defense = self.base_stats[2]
        self.speed = self.base_stats[3]

    def health_reset(self):
        self.health = self.base_stats[0]

    def move_left(self):
        self.rect.x -= 5

    def move_right(self):
        self.rect.x += 5

    def move_center(self):
        self.rect.x = self.original_x

    def move_down(self):
        self.rect.y += 10
            
    def update(self):
        self.animation_state()

class AbrahamLincoln():
    def __init__(self, lincolns_team):
        self.selection_image = pygame.image.load('graphics/enemy_lincoln3.png').convert_alpha()
        self.selection_image = pygame.transform.rotozoom(self.selection_image, 0, 1.3)
        if lincolns_team == 'enemy':
            lincoln_idle1 = pygame.image.load('graphics/enemy_lincoln1.png').convert_alpha()
            lincoln_idle2 = pygame.image.load('graphics/enemy_lincoln2.png').convert_alpha()
            lincoln_idle3 = pygame.image.load('graphics/enemy_lincoln3.png').convert_alpha()
            lincoln_idle4 = pygame.image.load('graphics/enemy_lincoln4.png').convert_alpha()
            lincoln_idle5 = pygame.image.load('graphics/enemy_lincoln5.png').convert_alpha()
            lincoln_idle6 = pygame.image.load('graphics/enemy_lincoln6.png').convert_alpha()

            self.idle = [lincoln_idle1, lincoln_idle2, lincoln_idle3, lincoln_idle3, 
                         lincoln_idle3, lincoln_idle2, lincoln_idle1, lincoln_idle4, 
                         lincoln_idle5, lincoln_idle5, lincoln_idle6, lincoln_idle5,
                         lincoln_idle5, lincoln_idle6, lincoln_idle5, lincoln_idle4]
            
        elif lincolns_team == 'player':
            lincoln_idle1 = pygame.image.load('graphics/player_lincoln1.png').convert_alpha()
            lincoln_idle1 = pygame.transform.rotozoom(lincoln_idle1, 0, 2)
            lincoln_idle2 = pygame.image.load('graphics/player_lincoln2.png').convert_alpha()
            lincoln_idle2 = pygame.transform.rotozoom(lincoln_idle2, 0, 2)
            lincoln_idle3 = pygame.image.load('graphics/player_lincoln3.png').convert_alpha()
            lincoln_idle3 = pygame.transform.rotozoom(lincoln_idle3, 0, 2)
            lincoln_idle4 = pygame.image.load('graphics/player_lincoln4.png').convert_alpha()
            lincoln_idle4 = pygame.transform.rotozoom(lincoln_idle4, 0, 2)
            lincoln_idle5 = pygame.image.load('graphics/player_lincoln5.png').convert_alpha()
            lincoln_idle5 = pygame.transform.rotozoom(lincoln_idle5, 0, 2)

            self.idle = [lincoln_idle1, lincoln_idle2, lincoln_idle3, lincoln_idle3, 
                         lincoln_idle3, lincoln_idle2, lincoln_idle1, lincoln_idle4, 
                         lincoln_idle5, lincoln_idle5, lincoln_idle5, lincoln_idle5,
                         lincoln_idle5, lincoln_idle5, lincoln_idle5, lincoln_idle4]

class BillClinton():
    def __init__(self, clintons_team):
        self.selection_image = clinton_idle1 = pygame.image.load('graphics/enemy_clinton1.png').convert_alpha()
        self.selection_image = pygame.transform.rotozoom(self.selection_image, 0, 1.3)
        if clintons_team == 'enemy':
            clinton_idle1 = pygame.image.load('graphics/enemy_clinton1.png').convert_alpha()
            clinton_idle2 = pygame.image.load('graphics/enemy_clinton2.png').convert_alpha()
            clinton_idle3 = pygame.image.load('graphics/enemy_clinton3.png').convert_alpha()

            self.idle = [clinton_idle1, clinton_idle2, clinton_idle3, clinton_idle2]

        elif clintons_team == 'player':
            clinton_idle1 = pygame.image.load('graphics/player_clinton1.png').convert_alpha()
            clinton_idle1 = pygame.transform.rotozoom(clinton_idle1, 0, 2)
            clinton_idle2 = pygame.image.load('graphics/player_clinton2.png').convert_alpha()
            clinton_idle2 = pygame.transform.rotozoom(clinton_idle2, 0, 2)
            clinton_idle3 = pygame.image.load('graphics/player_clinton3.png').convert_alpha()
            clinton_idle3 = pygame.transform.rotozoom(clinton_idle3, 0, 2)

            self.idle = [clinton_idle1, clinton_idle2, clinton_idle3, clinton_idle2]

class DonaldTrump():
    def __init__(self, trumps_team):
        self.selection_image = pygame.image.load('graphics/enemy_trump1.png').convert_alpha()
        self.selection_image = pygame.transform.rotozoom(self.selection_image, 0, 1.3)
        if trumps_team == 'enemy':
            trump_idle1 = pygame.image.load('graphics/enemy_trump1.png').convert_alpha()
            trump_idle2 = pygame.image.load('graphics/enemy_trump2.png').convert_alpha()
            trump_idle3 = pygame.image.load('graphics/enemy_trump3.png').convert_alpha()
            trump_idle4 = pygame.image.load('graphics/enemy_trump4.png').convert_alpha()
            trump_idle5 = pygame.image.load('graphics/enemy_trump5.png').convert_alpha()
            trump_idle6 = pygame.image.load('graphics/enemy_trump6.png').convert_alpha()
            
            self.idle = [trump_idle1, trump_idle2, trump_idle3, trump_idle2,
                         trump_idle4, trump_idle5, trump_idle6, trump_idle5]
            
        elif trumps_team == 'player':
            trump_idle1 = pygame.image.load('graphics/player_trump.png').convert_alpha()
            trump_idle1 = pygame.transform.rotozoom(trump_idle1, 0, 2)
            trump_idle2 = pygame.image.load('graphics/player_trump2.png').convert_alpha()
            trump_idle2 = pygame.transform.rotozoom(trump_idle2, 0, 2)
            trump_idle3 = pygame.image.load('graphics/player_trump3.png').convert_alpha()
            trump_idle3 = pygame.transform.rotozoom(trump_idle3, 0, 2)
            
            self.idle = [trump_idle1, trump_idle2, trump_idle3, trump_idle2, 
                         trump_idle3, trump_idle1, trump_idle1, trump_idle1]

class JoeBiden():
    def __init__(self, bidens_team):
        self.selection_image = pygame.image.load('graphics/enemy_biden9.png').convert_alpha()
        self.selection_image = pygame.transform.rotozoom(self.selection_image, 0, 1.3)
        if bidens_team == 'enemy':
            biden_idle1 = pygame.image.load('graphics/enemy_biden1.png').convert_alpha()
            biden_idle2 = pygame.image.load('graphics/enemy_biden2.png').convert_alpha()
            biden_idle3 = pygame.image.load('graphics/enemy_biden3.png').convert_alpha()
            biden_idle4 = pygame.image.load('graphics/enemy_biden4.png').convert_alpha()
            biden_idle5 = pygame.image.load('graphics/enemy_biden5.png').convert_alpha()
            biden_idle6 = pygame.image.load('graphics/enemy_biden6.png').convert_alpha()
            biden_idle7 = pygame.image.load('graphics/enemy_biden7.png').convert_alpha()
            biden_idle8 = pygame.image.load('graphics/enemy_biden8.png').convert_alpha()
            biden_idle9 = pygame.image.load('graphics/enemy_biden9.png').convert_alpha()
            biden_idle10 = pygame.image.load('graphics/enemy_biden10.png').convert_alpha()

            self.idle = [biden_idle1, biden_idle2, biden_idle3, biden_idle4, biden_idle5,
                         biden_idle6, biden_idle7, biden_idle8, biden_idle9, biden_idle10,
                         biden_idle9, biden_idle10, biden_idle9, biden_idle8, biden_idle7,
                         biden_idle6, biden_idle5, biden_idle4, biden_idle3, biden_idle2,
                         biden_idle1, biden_idle1]
            
        elif bidens_team == 'player':
            biden_idle1 = pygame.image.load('graphics/player_biden1.png').convert_alpha()
            biden_idle1 = pygame.transform.rotozoom(biden_idle1, 0, 2)
            biden_idle2 = pygame.image.load('graphics/player_biden2.png').convert_alpha()
            biden_idle2 = pygame.transform.rotozoom(biden_idle2, 0, 2)
            biden_idle3 = pygame.image.load('graphics/player_biden3.png').convert_alpha()
            biden_idle3 = pygame.transform.rotozoom(biden_idle3, 0, 2)
            biden_idle4 = pygame.image.load('graphics/player_biden4.png').convert_alpha()
            biden_idle4 = pygame.transform.rotozoom(biden_idle4, 0, 2)
            biden_idle5 = pygame.image.load('graphics/player_biden5.png').convert_alpha()
            biden_idle5 = pygame.transform.rotozoom(biden_idle5, 0, 2)
            biden_idle6 = pygame.image.load('graphics/player_biden6.png').convert_alpha()
            biden_idle6 = pygame.transform.rotozoom(biden_idle6, 0, 2)
            biden_idle7 = pygame.image.load('graphics/player_biden7.png').convert_alpha()
            biden_idle7 = pygame.transform.rotozoom(biden_idle7, 0, 2)
            biden_idle8 = pygame.image.load('graphics/player_biden8.png').convert_alpha()
            biden_idle8 = pygame.transform.rotozoom(biden_idle8, 0, 2)
            
            self.idle = [biden_idle1, biden_idle2, biden_idle3, biden_idle4, biden_idle5,
                         biden_idle6, biden_idle7, biden_idle8, biden_idle1, biden_idle1,
                         biden_idle1, biden_idle1, biden_idle1, biden_idle8, biden_idle7,
                         biden_idle6, biden_idle5, biden_idle4, biden_idle3, biden_idle2,
                         biden_idle1, biden_idle1]

class Obama():
    def __init__(self, obamas_team):
        self.selection_image = pygame.image.load('graphics/enemy_obama1.png').convert_alpha()
        self.selection_image = pygame.transform.rotozoom(self.selection_image, 0, 1.3)
        if obamas_team == 'enemy':
            obama_idle1 = pygame.image.load('graphics/enemy_obama1.png')
            obama_idle2 = pygame.image.load('graphics/enemy_obama2.png')
            obama_idle3 = pygame.image.load('graphics/enemy_obama3.png')
            obama_idle4 = pygame.image.load('graphics/enemy_obama4.png')

            self.idle = [obama_idle1, obama_idle2, obama_idle3, obama_idle4,
                         obama_idle3, obama_idle2]
            
        elif obamas_team == 'player':
            obama_idle1 = pygame.image.load('graphics/player_obama1.png')
            obama_idle1 = pygame.transform.rotozoom(obama_idle1, 0, 2)
            obama_idle2 = pygame.image.load('graphics/player_obama2.png')
            obama_idle2 = pygame.transform.rotozoom(obama_idle2, 0, 2)
            obama_idle3 = pygame.image.load('graphics/player_obama3.png')
            obama_idle3 = pygame.transform.rotozoom(obama_idle3, 0, 2)
            obama_idle4 = pygame.image.load('graphics/player_obama4.png')
            obama_idle4 = pygame.transform.rotozoom(obama_idle4, 0, 2)

            self.idle = [obama_idle1, obama_idle2, obama_idle3, obama_idle4,
                         obama_idle3, obama_idle2]

class GeorgeWashington():
    def __init__(self, washingtons_team):
        self.selection_image = pygame.image.load('graphics/enemy_washington8.png').convert_alpha()
        self.selection_image = pygame.transform.rotozoom(self.selection_image, 0, 1.3)
        if washingtons_team == 'enemy':
            washington_idle1 = pygame.image.load('graphics/enemy_washington1.png').convert_alpha()
            washington_idle2 = pygame.image.load('graphics/enemy_washington2.png').convert_alpha()
            washington_idle3 = pygame.image.load('graphics/enemy_washington3.png').convert_alpha()
            washington_idle4 = pygame.image.load('graphics/enemy_washington4.png').convert_alpha()
            washington_idle5 = pygame.image.load('graphics/enemy_washington5.png').convert_alpha()
            washington_idle6 = pygame.image.load('graphics/enemy_washington6.png').convert_alpha()
            washington_idle7 = pygame.image.load('graphics/enemy_washington7.png').convert_alpha()
            washington_idle8 = pygame.image.load('graphics/enemy_washington8.png').convert_alpha()
            washington_idle9 = pygame.image.load('graphics/enemy_washington9.png').convert_alpha()
            
            self.idle = [washington_idle1, washington_idle2, washington_idle3, washington_idle2,
                         washington_idle1, washington_idle4, washington_idle5, washington_idle6,
                         washington_idle7, washington_idle8, washington_idle8, washington_idle9,
                         washington_idle9, washington_idle7, washington_idle6, washington_idle5,
                         washington_idle4, washington_idle1]
            
        elif washingtons_team == 'player':
            washington_idle1 = pygame.image.load('graphics/player_washington1.png').convert_alpha()
            washington_idle1 = pygame.transform.rotozoom(washington_idle1, 0, 2)
            washington_idle2 = pygame.image.load('graphics/player_washington2.png').convert_alpha()
            washington_idle2 = pygame.transform.rotozoom(washington_idle2, 0, 2)
            washington_idle3 = pygame.image.load('graphics/player_washington3.png').convert_alpha()
            washington_idle3 = pygame.transform.rotozoom(washington_idle3, 0, 2)
            washington_idle4 = pygame.image.load('graphics/player_washington4.png').convert_alpha()
            washington_idle4 = pygame.transform.rotozoom(washington_idle4, 0, 2)
            washington_idle5 = pygame.image.load('graphics/player_washington5.png').convert_alpha()
            washington_idle5 = pygame.transform.rotozoom(washington_idle5, 0, 2)
            washington_idle6 = pygame.image.load('graphics/player_washington6.png').convert_alpha()
            washington_idle6 = pygame.transform.rotozoom(washington_idle6, 0, 2)
            washington_idle7 = pygame.image.load('graphics/player_washington7.png').convert_alpha()
            washington_idle7 = pygame.transform.rotozoom(washington_idle7, 0, 2)
            washington_idle8 = pygame.image.load('graphics/player_washington8.png').convert_alpha()
            washington_idle8 = pygame.transform.rotozoom(washington_idle8, 0, 2)
            washington_idle9 = pygame.image.load('graphics/player_washington9.png').convert_alpha()
            washington_idle9 = pygame.transform.rotozoom(washington_idle9, 0, 2)

            self.idle = [washington_idle1, washington_idle2, washington_idle3, washington_idle2,
                         washington_idle1, washington_idle4, washington_idle5, washington_idle6,
                         washington_idle7, washington_idle8, washington_idle8, washington_idle9,
                         washington_idle9, washington_idle7, washington_idle6, washington_idle5,
                         washington_idle4, washington_idle1]