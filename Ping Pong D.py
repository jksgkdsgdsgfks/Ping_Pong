from pygame import *

window = display.set_mode((700, 500))
display.set_caption("-----------------------------------------------Пинг Понг--------------------------------------------")
background = transform.scale(image.load("Фон.jpg"), (700, 500))

font.init()
font1 = font.SysFont('Arial', 35)


font2 = font.SysFont('Arial', 35)
FPS = 60
clock= time.Clock()

speed_x = 3
speed_y = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_weidth, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_weidth, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):

        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
            
    def update_r(self):

        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
    
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed

raketka_l = Player("fgb.png", 50, 250, 10, 20, 70)
raketka_r = Player("fgb.png", 650, 250, 10, 20, 70)
mych = GameSprite("Мяч1.png", 350, 250, 10, 50 ,50)


game = True
Finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if Finish != True:
        window.blit(background, (0, 0))
        mych.rect.x += speed_x
        mych.rect.y += speed_y

        
        
        if sprite.collide_rect(raketka_l, mych) or  sprite.collide_rect(raketka_r, mych):
            speed_x *= -1

        if mych.rect.y < 0 or mych.rect.y > 450:
            speed_y *= -1
        
        if mych.rect.x < 0:
            
            Finish = True
            losed = font1.render('Проиграл Левый!', True, (255, 0, 0))
            window.blit(losed, (225, 250))
            

        if mych.rect.x > 650:
            
            Finish = True
            lose = font2.render('Проиграл Правый!',True, (255, 0, 0))
            window.blit(lose, (225, 250))
    

        



        
        raketka_l.reset()
        raketka_r.reset()
        raketka_l.update_l()
        raketka_r.update_r()
        mych.reset()
        mych.update()




    display.update()
    clock.tick(FPS)
