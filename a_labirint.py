from pygame import *
from random import *

window = display.set_mode((850, 500))
display.set_caption('Game || Maze')
back = (107, 105, 94)
window.fill(back)
mixer.init()
font.init()

coins_count = 0
text = font.SysFont('Verdana', 48).render(str(coins_count), True, (0,0,0))

class Card(sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__()
        self.rect = Rect(x, y, w, h)
        self.fill = color

    def draw(self):
        draw.rect(window, self.fill, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Pic(sprite.Sprite):
    def __init__(self, pic, x, y, w, h):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(pic), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self): #Отрисовка изображений на экране
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Pic):
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x < 760 and not finish:
            self.rect.x += 8
        elif keys[K_a] and self.rect.x > 0 and not finish:
            self.rect.x -= 8
        elif keys[K_s] and self.rect.y < 400 and not finish:    
            self.rect.y += 8
        elif keys[K_w] and self.rect.y > 5 and not finish:
            self.rect.y -= 8

    def fire(self):
        bullet = Bullet("m_bullet.png", self.rect.right, self.rect.centery, 45,40)
        bullets.add(bullet)

class Bullet(Pic): #пули
    def update(self):
        self.rect.x += 12
        if self.rect.x == 850:
            self.kill()
bullets = sprite.Group()

class Enemy(Pic): 
    side = 'top'
    def __init__(self, pic, x, y, w, h, speed_y):
        Pic.__init__(self,  pic, x, y, w, h)
        self.speed_y = speed_y

    def update(self):
        if self.side == 'top':
            self.rect.y -= self.speed_y
        if self.side == 'bottom':
            self.rect.y += self.speed_y
            
        if self.rect.y <= 40:
            self.side = 'bottom'
        if self.rect.y >= 235:
            self.side = 'top'

player = Player('player.png', 20, 50, 60, 90)
goal = Pic('chest2.png', 710, 370, 110, 110)
enemy = Enemy('enemy.png', 380, 235, 60, 90, 6)
enemies = sprite.Group()
enemies.add(enemy)

coins = sprite.Group()
coin1 = Pic('coin1.png', 45, 180, 32,32)
coins.add(coin1)
coin2 = Pic('coin1.png', 45, 300, 32,32)
coins.add(coin2)
coin3 = Pic('coin1.png', 45, 400, 32,32)
coins.add(coin3)
coin4 = Pic('coin1.png', 200, 250, 32,32)
coins.add(coin4)
coin5 = Pic('coin1.png', 230, 90, 32,32)
coins.add(coin5)
coin6 = Pic('coin1.png', 560, 90, 32,32)
coins.add(coin6)
coin7 = Pic('coin1.png', 590, 250, 32,32)
coins.add(coin7)
coin8 = Pic('coin1.png', 730, 250, 32,32)
coins.add(coin8)
coin9 = Pic('coin1.png', 390, 250, 32, 32)
coins.add(coin9)


walls = sprite.Group()
y = 0
x = 0
for w in range (17):
    wall = Pic('wall-.png', x, 0, 40, 40)
    x += 40
    walls.add(wall)

y = 40
for w in range(4):
    wall2 = Pic('wall_vert.png', 150, y, 40, 40)
    y += 40
    walls.add(wall2)

y = 370
for w in range(4):
    wall3 = Pic('wall_vert.png', 150, y, 40, 40)
    y += 40
    walls.add(wall3)

x = 150
for w in range(13):
    wall4 = Pic('wall-.png', x, 340, 40, 40)
    x += 40
    walls.add(wall4)

y = 260
for w in range(2):
    wall5 = Pic('wall_vert.png', 310, y, 40, 40)
    y += 40
    walls.add(wall5)

y = 260
for w in range(2):
    wall6 = Pic('wall_vert.png', 480, y, 40, 40)
    y += 40
    walls.add(wall6)

y = 380
for w in range(4):
    wall7 = Pic('wall_vert.png', 630, y, 40, 40)
    y += 40
    walls.add(wall7)

y = 0
for w in range(4):
    wall8 = Pic('wall_vert.png', 670, y, 40, 40)
    y += 40
    walls.add(wall8)

x = 670
for w in range(5):
    wall9 = Pic('wall-.png', x, 160, 40, 40)
    x +=40
    walls.add(wall9)



win = transform.scale(image.load('m_win.jpg'), (850, 500))
loose = transform.scale(image.load('m_lose.jpg'), (850, 500))
restart = transform.scale(image.load('m_restart.png'), (300, 130))
restart_area = Card(270, 370, 300, 130, back)
help_b = transform.scale(image.load('help.png'), (80,80))
help_b_area = Card(770,0, 80,80, back)
help_w = transform.scale(image.load('help_w.png'), (850, 500))
back_b = Card(710, 390, 120, 100, back)




run = True #запущена ли игра
finish = False #достигнута цель
while run:
    if run != False:
        window.fill(back)
        walls.draw(window)
        coins.draw(window)
        enemies.draw(window)
        enemies.update()
        bullets.draw(window)
        bullets.update()
        player.reset()
        player.update()
        goal.reset()
        goal.update()
        
        #window.blit(help_b, (770,0))
        window.blit(text, (725, 20)) #счетчик 
        if sprite.spritecollide(player, enemies, False):
            finish = True
            window.blit(loose, (0, 0))
            window.blit(restart, (270, 370))
            for pers in enemies:
                pers.speed_y = 0
            mixer.music.stop()
            #sound_loose.play()
            
        elif sprite.collide_rect(player, goal):
            window.blit(win, (0, 0))
            window.blit(restart, (270, 370))
            mixer.music.stop()
            #sound_win.play()
            finish = True
        if sprite.spritecollide(player, walls, False):
            player.rect.x = 20
            player.rect.y = 50
        if sprite.spritecollide(player, coins, True):
            coins_count += 1
            text = font.SysFont('Verdana', 48).render(str(coins_count), True, (0,0,0))
            window.blit(text, (725, 20))
        sprite.groupcollide(bullets, walls, True, False)
        sprite.groupcollide(bullets, enemies, True, True)

            

    for e in event.get():
        if e.type == QUIT: #выход из игры
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE: #стрельба
                player.fire()
        elif e.type == MOUSEBUTTONDOWN and e.button == 1: #нажатие мышкой на рестарт
            x, y = e.pos
            if restart_area.collidepoint(x, y):
                finish = False
                player.rect.x = 20
                player.rect.y = 50
                for pers in enemies:
                    pers.rect.x = 380
                    pers.rect.y = 235
            

                if not finish: 
                    for pers in enemies:
                        pers.speed_y = 0
                    for coin in coins:
                        coin.kill()
                    for i in range(3):
                        create = Pic('coin1.png', 45, randint(150,450), 32,32)
                        coins.add(create)
                    for i in range(4):
                        create2 = Pic('coin1.png', randint(230,560), 90, 32,32)
                        coins.add(create2)
                    create3 = Pic('coin1.png', 390, 250, 32, 32)
                    coins.add(create3)
                    coins.draw(window)
                    coins_count = 0
                    text = font.SysFont('Verdana', 48).render(str(coins_count), True, (0,0,0))

                    window.fill(back)
                    walls.draw(window)
                    coins.draw(window)
                    enemies.draw(window)
                    enemies.update()
                    bullets.draw(window)
                    bullets.update()
                    player.reset()
                    player.update()
                    goal.reset()
                    goal.update()
                    #window.blit(help_b, (770,0))
                    window.blit(text, (725, 20)) #счетчик 
                    if sprite.spritecollide(player, enemies, False):
                        finish = True
                        window.blit(loose, (0, 0))
                        window.blit(restart, (270, 370))
                        for pers in enemies:
                            pers.speed_y = 0
                        mixer.music.stop()
                        #sound_loose.play()
                    elif sprite.collide_rect(player, goal):
                        window.blit(win, (0, 0))
                        window.blit(restart, (270, 370))
                        mixer.music.stop()
                        #sound_win.play()
                        finish = True
                    if sprite.spritecollide(player, walls, False):
                        player.rect.x = 20
                        player.rect.y = 50
                    if sprite.spritecollide(player, coins, True):
                        coins_count += 1
                        text = font.SysFont('Verdana', 48).render(str(coins_count), True, (0,0,0))
                        window.blit(text, (725, 20))
                    sprite.groupcollide(bullets, walls, True, False)
                    sprite.groupcollide(bullets, enemies, True, True)
                    enemy = Enemy('enemy.png', 380, 235, 60, 90, 6)
                    enemies = sprite.Group()
                    enemies.add(enemy)
    display.update()
    time.delay(40)

