import pygame 
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, DEFAULT_TYPE, FPS
from game.components.spaceship import Spaceship

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.scream = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.playing = False
        self.game_speed = 10

        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()



    def run(self):
        self.playing = True
        while self.playing:
            self.enents()
            self.update()
            self.draw()
    
    def enents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update = user_input



    def draw(self):
        self.clock.tick(FPS)
        self.scream.fill((255,255,255))
        
        self.draw_background()
        self.player.draw()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.scream.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.scream.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))

        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.scream.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg = self.y_pos_bg + self.game_speed
