import pygame

class Rocket:
    def __init__(self,rf_games):
        # 初始化火箭及屏幕初始位置
        self.screen=rf_games.screen
        self.screen_rect=rf_games.screen.get_rect()
        self.settings=rf_games.settings

        # 加载火箭图像
        self.image=pygame.transform.scale(
            pygame.image.load('image/rocket.bmp'),(60,70))
        self.rect=self.image.get_rect()

        # 设置火箭初始位置,使其置于屏幕中央
        self.rect.center=self.screen_rect.center
        
        # 坐标位置
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

        # 移动标志
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.speed
        elif self.moving_left and self.rect.left>0:
            self.x-=self.settings.speed
        elif self.moving_up and self.rect.top>0:
            self.y-=self.settings.speed
        elif self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.y+=self.settings.speed
        
        self.rect.x=self.x
        self.rect.y=self.y