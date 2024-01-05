from curses import KEY_DOWN, KEY_EXIT, KEY_LEFT, KEY_RESET, KEY_RIGHT, KEY_UP
from gettext import install
import time
import random
import pygame,sys
from pygame.math import Vector2
SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)
#Try

class Eat:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("mon.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

class Dora:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("dora.jpg").convert()
        self.direction = 'right'

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Doremon Eat Apple")

        pygame.mixer.init()
        self.play_background_music()

        self.surface = pygame.display.set_mode((1500, 800))
        self.dora = Dora(self.surface)
        self.dora.draw()
        self.eat = Eat(self.surface)
        self.eat.draw()

    def play_background_music(self):
        pygame.mixer.music.load('B.mp3')
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        if sound_name == "oh_no":
            sound = pygame.mixer.Sound("oh_no.mp3")
        elif sound_name == 'haha':
            sound = pygame.mixer.Sound("haha.wav")

        pygame.mixer.Sound.play(sound)

    def reset(self):
        self.dora = Dora(self.surface)
        self.eat = Eat(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self):
        bg = pygame.image.load("bag.jpg")
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_background()
        self.dora.walk()
        self.eat.draw()
        self.display_score()
        pygame.display.flip()

        # snake eating apple scenario
        if self.is_collision(self.dora.x[0], self.dora.y[0], self.eat.x, self.eat.y):
            self.play_sound("haha")
            self.dora.increase_length()
            self.eat.move()

        # snake colliding with itself
        for i in range(3, self.dora.length):
            if self.is_collision(self.dora.x[0], self.dora.y[0], self.dora.x[i], self.dora.y[i]):
                self.play_sound('oh_no')
                raise "Takkar"

    def display_score(self):
        font = pygame.font.SysFont('cursive',30)
        score = font.render(f"Rank- {self.dora.length}",True,(200,200,200))
        self.surface.blit(score,(850,20))

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('cursive', 30)
        line1 = font.render(f"Khatam! Score is--{self.dora.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("Play Again press Enter \n For exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEY_DOWN:
                    if event.key == KEY_EXIT:
                        running = False

                    if event.key == KEY_RESET:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == KEY_LEFT:
                            self.dora.move_left()

                        if event.key == KEY_RIGHT:
                            self.dora.move_right()

                        if event.key == KEY_UP:
                            self.dora.move_up()

                        if event.key == KEY_DOWN:
                            self.dora.move_down()

                elif event.type == quit:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.25)

if __name__ == '__main__':
    game = Game()
    game.run()