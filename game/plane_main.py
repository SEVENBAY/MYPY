from plane_sprites import *


class Game(object):
    """主游戏类"""

    score = 0

    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # 播放背景音乐
        game_music = pygame.mixer.Sound("D:\Python\myproject2\sounds\game_music.wav")
        game_music.set_volume(0.2)
        game_music.play(1000)
        # 初始化创建敌机的事件
        pygame.time.set_timer(ENEMY_EVENT, 1000)
        # 初始化创建超级子弹buff的事件
        pygame.time.set_timer(SUPERBULLETBUFF, random.randint(2000, 40000))
        # 是否暂停
        self.is_pause = False


    def __create__(self):
        # 创建背景并添加至精灵组
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)

        # 创建英雄飞机并添加至精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建超级子弹buff精灵组
        self.superbulletbuff_group = pygame.sprite.Group()

    def __update__(self):
        # 绘制背景
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        # 绘制敌机
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        # 绘制英雄飞机
        self.hero_group.update()
        self.hero_group.draw(self.screen)

        # 绘制子弹
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

        # 绘制超级子弹buff
        self.superbulletbuff_group.update()
        self.superbulletbuff_group.draw(self.screen)

    def __ifhit__(self):
        # 判断敌机是否与子弹相撞，如果是，则销毁子弹，并将敌机检测碰撞的参数设置非空以绘制动态毁灭效果
        for enemy in self.enemy_group.sprites():
            for bullet in self.hero.bullet_group.sprites():

                ishit = pygame.sprite.collide_mask(enemy, bullet)
                if ishit:
                    enemy.ishit = ishit
                    # 播放敌机毁灭的声音
                    enemydown_music = pygame.mixer.Sound("D:\Python\myproject2\sounds\enemy1_down.wav")
                    enemydown_music.set_volume(2)
                    enemydown_music.play()

                    bullet.kill()

        # 判断敌机是否与英雄相撞，如果是，则将敌机与英雄飞机检测碰撞的参数设置非空，实现毁灭的动态效果
        for enemy in self.enemy_group.sprites():
            isherohit = pygame.sprite.collide_mask(enemy, self.hero)
            if isherohit:
                # 播放游戏结束的声音
                gameover_music = pygame.mixer.Sound("D:\Python\myproject2\sounds\game_over.wav")
                gameover_music.set_volume(0.5)
                gameover_music.play()

                self.hero.ishit = isherohit
                enemy.ishit = isherohit

        # 判断英雄飞机是否获得超级子弹buff
        for superbulletbuff in self.superbulletbuff_group.sprites():
            isget = pygame.sprite.collide_mask(superbulletbuff, self.hero)
            if isget:
                getbuff_music = pygame.mixer.Sound("D:\Python\myproject2\sounds\get_bomb.wav")
                getbuff_music.set_volume(2)
                getbuff_music.play()
                self.hero.getsuperbullet = isget
                superbulletbuff.kill()


    def __event__(self):
        # 获取事件列表，判断是否退出游戏，以及创建敌机并添加至精灵组
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                Game.game_over()
            elif event.type == ENEMY_EVENT:
                self.enemy = Enemy()
                self.enemy_group.add(self.enemy)
            elif event.type == SUPERBULLETBUFF:
                self.superbulletbuff = SuperBulletBuff()
                self.superbulletbuff_group.add(self.superbulletbuff)
            # 实现发射子弹
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # 创建发射子弹的声音
                fire_music = pygame.mixer.Sound(r"D:\Python\myproject2\sounds\bullet.wav")
                fire_music.set_volume(2)
                fire_music.play()
                self.hero.fire()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.is_pause = True


        # 实现飞机的左右移动控制
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.hero.rect.x += -4
        elif key[pygame.K_RIGHT]:
            self.hero.rect.x += 4

    def __game_pause__(self):
        if self.is_pause:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.is_pause = False
                if not self.is_pause:
                    break

    def start_game(self):
        # 游戏开始主方法
        self.__create__()
        while True:
            clock.tick(80)

            # 绘制
            self.__update__()

            # 事件监听
            self.__event__()

            # 碰撞检测
            self.__ifhit__()

            # 暂停游戏功能
            self.__game_pause__()

            pygame.display.update()



    @staticmethod
    def game_over():
        print("游戏结束...")

        exit()
        pygame.quit()

        # while True:
        #     print("阿道夫")
        #     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        #     image = pygame.image.load(r"D:\Python\myproject2\images\background.png")
        #     screen.blit(, (0, 0))
        #     pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.start_game()



