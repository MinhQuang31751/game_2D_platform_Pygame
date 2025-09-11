
import pygame
#goi event nhanh hon
from pygame.locals import *
from settings import TILE_SIZE

from lava import Lava
from enemy import Enemy
from nextLevel import Nexlevel
from coin import Coin
from levels import *
enemy_group = pygame.sprite.Group()
next_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
class World():
    def __init__(self,data):
        self.tile_list=[]
        dat_img=pygame.image.load('assets/img/dirt.png')
        dat_img = pygame.transform.scale(dat_img, (TILE_SIZE, TILE_SIZE))
        row_count = 0
        for row in data:
            col_count =0
            for col in row:
                if col==1:
                    img_rect = dat_img.get_rect()
                    img_rect.x = col_count*TILE_SIZE
                    img_rect.y = row_count*TILE_SIZE
                    self.tile_list.append((dat_img, img_rect))
                if col==2:
                    lava= Lava(col_count*TILE_SIZE,row_count*TILE_SIZE)
                    enemy_group.add(lava)
                if col==3:
                    enemy= Enemy(col_count*TILE_SIZE,row_count*TILE_SIZE)
                    enemy_group.add(enemy)
                if col==4:
                    nextLevel = Nexlevel(col_count*TILE_SIZE,row_count*TILE_SIZE)
                    next_group.add(nextLevel)
                if col==5:
                    center_x = col_count * TILE_SIZE + TILE_SIZE // 2
                    center_y = row_count * TILE_SIZE + TILE_SIZE // 2
                    coin = Coin(center_x, center_y)
                # Thêm đối tượng Coin vào nhóm coin_group
                    coin_group.add(coin)
                col_count+=1
            row_count+=1
    def draw(self, screen):
        for data in self.tile_list:
            screen.blit(data[0],data[1])


'''
import pygame
from pygame.locals import *
from settings import TILE_SIZE
from lava import Lava
from enemy import Enemy
from nextLevel import Nexlevel
from coin import Coin
from moving_platform import MovingPlatform  # Import lớp MovingPlatform
from levels import *

# Khởi tạo các sprite group
enemy_group = pygame.sprite.Group()
next_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
moving_platform_group = pygame.sprite.Group()  # Thêm group cho moving platforms

class World():
    def __init__(self, data):
        self.tile_list = []
        dat_img = pygame.image.load('assets/img/dirt.png')
        dat_img = pygame.transform.scale(dat_img, (TILE_SIZE, TILE_SIZE))
        
        row_count = 0
        for row in data:
            col_count = 0
            for col in row:
                if col == 1:  # Ground
                    img_rect = dat_img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    self.tile_list.append((dat_img, img_rect))
                
                elif col == 2:  # Lava
                    lava = Lava(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    enemy_group.add(lava)
                
                elif col == 3:  # Enemy
                    enemy = Enemy(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    enemy_group.add(enemy)
                
                elif col == 4:  # Next level
                    nextLevel = Nexlevel(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    next_group.add(nextLevel)
                
                elif col == 5:  # Coin
                    center_x = col_count * TILE_SIZE + TILE_SIZE // 2
                    center_y = row_count * TILE_SIZE + TILE_SIZE // 2
                    coin = Coin(center_x, center_y)
                    coin_group.add(coin)
                
                # THÊM XỬ LÝ CHO MOVING PLATFORMS
                elif col == 6:  # Moving platform vertical (lên xuống)
                    platform = MovingPlatform(
                        col_count * TILE_SIZE, 
                        row_count * TILE_SIZE,
                        move_x=0, 
                        move_y=2, 
                        move_range=80
                    )
                    moving_platform_group.add(platform)
                
                elif col == 7:  # Moving platform horizontal (trái phải)
                    platform = MovingPlatform(
                        col_count * TILE_SIZE, 
                        row_count * TILE_SIZE,
                        move_x=2, 
                        move_y=0, 
                        move_range=100
                    )
                    moving_platform_group.add(platform)
                
                elif col == 8:  # Moving platform diagonal (chéo)
                    platform = MovingPlatform(
                        col_count * TILE_SIZE, 
                        row_count * TILE_SIZE,
                        move_x=1, 
                        move_y=1, 
                        move_range=60
                    )
                    moving_platform_group.add(platform)
                
                col_count += 1
            row_count += 1

    def draw(self, screen):
        # Vẽ tiles nền
        for data in self.tile_list:
            screen.blit(data[0], data[1])
        
        # Vẽ moving platforms
        moving_platform_group.draw(screen)
        
        # Vẽ các nhóm khác
        enemy_group.draw(screen)
        next_group.draw(screen)
        coin_group.draw(screen)

    def update(self):
        # Cập nhật moving platforms
        moving_platform_group.update()
        
        # Cập nhật các nhóm khác
        enemy_group.update()
        coin_group.update()
        '''