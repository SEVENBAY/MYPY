import time
import pygame
import random
from plane_main import *


# 定义屏幕的宽高
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 852
# 创建时钟对象
clock = pygame.time.Clock()
# 创建敌机事件
ENEMY_EVENT = pygame.USEREVENT
# 超级子弹buff
SUPERBULLETBUFF = pygame.USEREVENT + 1
# 超级子弹移除事件
SUPERBULLETBUFFOFF = pygame.USEREVENT + 2
pygame.time.set_timer(SUPERBULLETBUFFOFF, 1000)


class GameSprites(pygame.sprite.Sprite):
    """游戏精灵类"""

    def __init__(self, image_path, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        super().update()
        self.rect.y += self.speed


class BackGround(GameSprites):
    """背景精灵类"""

    def __init__(self, is_alt=False):
        super().__init__(r"D:\Python\myproject2\images\background.png")
        self.rect.x = 0
        self.rect.y = 0
        # 判断是否是第二张背景图，如果是，初始位置设定在游戏窗口正上方
        if is_alt:
            self.rect.x = 0
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        # 如果图片在下方离开游戏窗口，就放到窗口正上方
        if self.rect.y > self.rect.height:
            self.rect.y = -self.rect.height


class Hero(GameSprites):
    """英雄飞机类"""

    def __init__(self):
        self.image_path_list = []
        # 加载两张英雄飞机图片，以实现动态效果
        image_path1 = "D:\Python\myproject2\images\hero1.png"
        image_path2 = "D:\Python\myproject2\images\hero2.png"
        self.image_path_list.append(image_path1)
        self.image_path_list.append(image_path2)
        super().__init__(self.image_path_list[0])

        # 创建英雄飞机爆炸图的列表，以实现飞机爆炸动态图
        self.herodown_list = []
        for num in range(1, 5):
            image = pygame.image.load("D:\Python\myproject2\images\hero_blowup_n"+str(num)+".png")
            self.herodown_list.append(image)
        # 设置飞机的初始位置
        self.rect.bottom = SCREEN_HEIGHT - 50
        self.rect.centerx = SCREEN_WIDTH / 2
        # 初始化飞机图片列表的索引值及绘制次数
        self.image_index = 0
        self.times = 0
        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()
        # 初始化判断是否被击中的参数
        self.ishit = None
        # 初始化飞机毁坏图片列表的索引值及绘制次数
        self.index = 0
        self.blowtimes = 0
        # 是否获得超级子弹
        self.getsuperbullet = None
        # 超级子弹数
        self.superbulletnum = 0

    def update(self):
        # 实现飞机飞行的动态效果
        if self.image_index <= 1:
            if self.times < 10:
                self.image = pygame.image.load(self.image_path_list[self.image_index])
                self.times += 1
            else:
                self.times = 0
                self.image_index += 1
        else:
            self.image_index = 0

        # 保证飞机左右飞行不会飞出屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

        # 绘制英雄飞机爆炸效果
        if self.ishit:
            self.image = self.herodown_list[3]
            if self.index < 4:
                if self.blowtimes < 5:
                    self.image = self.herodown_list[self.index]
                    self.blowtimes += 1
                else:
                    self.blowtimes = 0
                    self.index += 1
            else:
                print("英雄牺牲...")
                pygame.time.delay(1000)
                self.kill()
                self.index = 0

                # 显示最终得分
                bg1 = BackGround()
                bg2 = BackGround(True)
                screen = pygame.display.set_mode((0, 0))
                bg_group = pygame.sprite.Group(bg1, bg2)
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                            pygame.quit()
                    bg_group.update()
                    bg_group.draw(screen)
                    # 绘制结束游戏提示文字
                    scoreobj = pygame.font.Font("C:\Windows\Fonts\msyhbd.ttf", 20)
                    gameobj = pygame.font.Font("C:\Windows\Fonts\msyhbd.ttf", 40)
                    gameoversur = gameobj.render("GAME OVER", False, (0, 0, 255))
                    scoreobjsur = scoreobj.render("最终得分：%d" % (Game.score - 1), False, (0, 0, 255))
                    scoreobjrec = scoreobjsur.get_rect()
                    gameoverrec = gameoversur.get_rect()
                    gameoverrec.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100)
                    scoreobjrec.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                    screen.blit(gameoversur, gameoverrec)
                    screen.blit(scoreobjsur, scoreobjrec)
                    pygame.display.update()

    # 飞机发射子弹方法
    def fire(self):
        bullet = Bullets()
        if self.getsuperbullet:
            bullet1 = SuperBullets()
            bullet2 = SuperBullets()
            bullet1.rect.centerx = self.rect.x + 18
            bullet1.rect.bottom = self.rect.centery
            bullet2.rect.centerx = self.rect.x + self.rect.width - 18
            bullet2.rect.bottom = self.rect.centery
            self.bullet_group.add(bullet1, bullet2)
            # 控制超级子弹数量
            self.superbulletnum += 1
            if self.superbulletnum > 10:
                 self.getsuperbullet = None
                 self.superbulletnum = 0

        bullet.rect.centerx = self.rect.centerx
        bullet.rect.bottom = self.rect.y
        self.bullet_group.add(bullet)


class Bullets(GameSprites):
    """子弹类"""

    def __init__(self):
        super().__init__(r"D:\Python\myproject2\images\bullet1.png")
        self.speed = -10

    def update(self):
        # 如果子弹飞出屏幕，就销毁之
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


class SuperBullets(GameSprites):
    """超级子弹类"""
    def __init__(self):
        super().__init__(r"D:\Python\myproject2\images\bullet2.png")
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


class SuperBulletBuff(GameSprites):
    """超级子弹获得BUFF类"""
    def __init__(self):
        super().__init__(r"D:\Python\myproject2\images\ufo1.png")
        self.speed = 10
        self.rect.x = random.randint(0, SCREEN_WIDTH-self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()


class Enemy(GameSprites):
    """敌机类"""

    def __init__(self):
        super().__init__("D:\Python\myproject2\images\enemy1.png")
        # 创建敌机毁灭图片的列表，以实现敌机会毁灭动态效果
        self.enemy_image_list = []
        for num in range(1, 5):
            enemy_image = pygame.image.load("D:\Python\myproject2\images\enemy1_down"+str(num)+".png")
            self.enemy_image_list.append(enemy_image)

        # 控制敌机进入屏幕的位置随机，飞行速度随机
        self.rect.x = random.randint(0, SCREEN_WIDTH-self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1, 3)
        # 初始化敌机是否碰撞参数
        self.ishit = None
        # 初始化敌机敌机毁灭图片列表的索引及绘制次数
        self.index = 0
        self.times = 0

    def update(self):
        # 如果敌机飞出屏幕，则销毁之
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

        # 绘制敌机爆炸效果
        if self.ishit:
            if self.index < 4:
                if self.times < 5:
                    self.image = self.enemy_image_list[self.index]
                    self.times += 1
                else:
                    self.times = 0
                    self.index += 1
            else:
                self.kill()
                Game.score += 1
                self.ishit = None
                self.index = 0
