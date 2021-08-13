from settings import Settings
from rocket import Rocket

import sys
import pygame

class RocketFly:
    def __init__(self):
        # 初始化pygame模块
        pygame.init()
        # 初始化settings
        self.settings=Settings()
        # 初始化screen
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height
        self.bg_color=self.settings.bg_color
        # 初始化title
        pygame.display.set_caption("Rocket Fly")
        # 初始化rocket
        self.rocket=Rocket(self)
    def run_game(self):
        # 主循环程序
        while True:
            self._check_events()
            self._update_screen()
            self.rocket.update()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    sys.exit()
                if event.key==pygame.K_RIGHT:
                    self.rocket.moving_right=True
                if event.key==pygame.K_LEFT:
                    self.rocket.moving_left=True
                if event.key==pygame.K_UP:
                    self.rocket.moving_up=True
                if event.key==pygame.K_DOWN:
                    self.rocket.moving_down=True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    self.rocket.moving_right=False
                if event.key==pygame.K_LEFT:
                    self.rocket.moving_left=False
                if event.key==pygame.K_UP:
                    self.rocket.moving_up=False
                if event.key==pygame.K_DOWN:
                    self.rocket.moving_down=False

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.rocket.blitme()
        pygame.display.update()

if __name__=="__main__":
    rf=RocketFly()
    rf.run_game()
        