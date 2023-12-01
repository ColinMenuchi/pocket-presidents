import pygame

class President(pygame.sprite.Sprite):
    def __init__(self, team, name):
        super().__init__()
        self.team = team
        self.name = name
        self.animation_index = 0
        #Presidential Sprite Creation
        #Determines Team
        if self.team == 'player':
            #Picks From Player Presidential Sprites
            match self.name:
                case 'Donald Trump':
                    self.idle = DonaldTrump('player').idle

                case 'Joe Biden':
                    joe_biden_idle1 = pygame.image.load('graphics/joe_biden1.png').convert_alpha
                case _:
                    print('Invalid Name')
            
            self.image = self.idle[self.animation_index]
            self.screen_coords = (57, 160)
            self.rect = self.image.get_rect(topleft = self.screen_coords)

        elif self.team == 'enemy':
            #Picks From Enemy Presidential Sprites
            match self.name:
                case 'Obama':
                    obama_idle1 = pygame.image.load('graphics/obama1.png').convert_alpha()
                    obama_idle2 = pygame.image.load('graphics/obama2.png').convert_alpha()
                    obama_idle3 = pygame.image.load('graphics/obama3.png').convert_alpha()
                    obama_idle4 = pygame.image.load('graphics/obama4.png').convert_alpha()
                    self.idle = [obama_idle1, obama_idle2, obama_idle3, 
                                 obama_idle4, obama_idle3, obama_idle2]
                    
                case 'Bill Clinton':
                    clinton_idle1 = pygame.image.load('graphics/clinton1.png').convert_alpha()
                    clinton_idle2 = pygame.image.load('graphics/clinton2.png').convert_alpha()
                    clinton_idle3 = pygame.image.load('graphics/clinton3.png').convert_alpha()
                    self.idle = [clinton_idle1, clinton_idle2, clinton_idle3, clinton_idle2]

                case 'Donald Trump':
                    self.idle = DonaldTrump('enemy').idle
                    
                case 'Abraham Lincoln':
                    self.idle = AbrahamLincoln('enemy').idle
                    
            self.image = self.idle[self.animation_index]
            self.screen_coords = (630, 90)
            self.rect = self.image.get_rect(topleft = self.screen_coords)
        
        else:
            print('Invalid Team')


    def animation_state(self):
        self.animation_index += 0.065
        if self.animation_index >= len(self.idle):
            self.animation_index = 0

        self.image = self.idle[int(self.animation_index)]
        self.rect = self.image.get_rect(topleft = self.screen_coords)
            
    
    def update(self):
        self.animation_state()

class AbrahamLincoln():
    def __init__(self, lincolns_team):
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
            lincoln_idle2 = pygame.image.load('graphics/player_lincoln2.png').convert_alpha()
            lincoln_idle3 = pygame.image.load('graphics/player_lincoln3.png').convert_alpha()
            lincoln_idle4 = pygame.image.load('graphics/player_lincoln4.png').convert_alpha()
            lincoln_idle5 = pygame.image.load('graphics/player_lincoln5.png').convert_alpha()

class BillClinton():
    def __init__(self):
        self.head = pygame.image.load('graphics/head_bill_clinton.png').convert_alpha()

class DonaldTrump():
    def __init__(self, trumps_team):
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