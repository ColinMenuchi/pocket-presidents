import pygame

class Button():
    def __init__(self, x, y, image, screen_, scale, sound):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.screen = screen_
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.sound = sound
        self.clicked = False

    def draw(self, image, hover_image):
        #Draw Button on Screen
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        #Change image When Hovering Over Button
        pos = pygame.mouse.get_pos() #Gets Mouse Position as a Tuple of Coordinates
        if self.rect.collidepoint(pos):
            self.image = hover_image
        else:
            self.image = image

    def is_clicked(self):
        action = False

        #Get Mouse Position
        pos = pygame.mouse.get_pos()

        #Check Mouseover and Clicked Conditions
        if  self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #If Left Mouse Key is Clicked
                self.sound.play()
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            action = False

        return action


