from settings import Settings
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
    def run_game(self):
        # 主循环程序
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    sys.exit()
    
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        pygame.display.update()

if __name__=="__main__":
    rf=RocketFly()
    rf.run_game()
        