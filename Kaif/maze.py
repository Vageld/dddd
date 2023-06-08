from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed

class Enemy (GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 615:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall (sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_width = wall_width
        self.height = wall_height
        self.image = Surface((self.wall_width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("Maze")
background  = transform.scale(image.load('background.jpg'),(win_width,win_height))

player = Player('hero.png', 10, 400, 4)
monster = Enemy('cyborg.png', 600, 280, 2)
gold = GameSprite('treasure.png', 580, 420, 0)

w1 = Wall(154, 205, 50, 100, 20 , 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)
w4 = Wall(154, 205, 50, 200, 130, 10, 350)
w5 = Wall(154, 205, 50, 450, 130, 10, 360)
w6 = Wall(154, 205, 50, 300, 20, 10, 350)
w7 = Wall(154, 205, 50, 390, 120, 130, 10)

game = True 

speed = 10
clock = time.Clock()
FPS = 24

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (255, 215, 0))


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
finish = False
while  game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()
        player.reset()
        monster.reset()
        gold.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
    
    if (sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1)
        or sprite.collide_rect(player, w2)or sprite.collide_rect(player, w3)):
        finish = True
        window.blit(lose, (200, 200))

    if sprite.collide_rect(player, gold):
        finish = True
        window.blit(win, (200, 208))


    window.blit(background,(0, 0))
    player.update()
    monster.update()

    player.reset()
    monster.reset()
    gold.reset()

    display.update()
    clock.tick(FPS)



        