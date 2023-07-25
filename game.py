import threading
import pyautogui
import pygame
import random
import threading
import pyautogui
from flask import Flask, request, render_template    # 載入 render_template

def thread_job():
    global score
    score = 0
    app = Flask(__name__)
    @app.route('/')
    def home():
        name = request.args.get('name')
        return render_template('test.html', name=name, score=score)  # 傳入遊戲中的 score 到網頁

    @app.route("/<msg>")           
    def ok(msg):
        return f"<h1>{msg}</h1>"
    app.run()


thread1= threading.Thread( target=thread_job)
thread1.start()


# 初始化Pygame
pygame.init()
# 視窗大小
window_width = 800
window_height = 600
# 顏色
black = (0, 0, 0)
white = (255, 255, 255)
# 創建遊戲視窗
window = pygame.display.set_mode((window_width, window_height))
# 載入角色圖片
player_images = []
#player_images[0~3] 向右的圖片
i=0
for i in range(4):   
    img = pygame.image.load(f"player{i}.png")
    img.set_colorkey(white)
    player_images.append(img)
    
for i in range(4):   
    img = pygame.transform.flip(player_images[i], True, False)
    img.set_colorkey(white)
    player_images.append(img)
    
player_rect=player_images[0].get_rect()
# 載入金幣圖片
coin_image = pygame.image.load("coin.png")
coin_image.set_colorkey(white)
coin_rect = coin_image.get_rect()
# 設定角色的起始位置
player_rect.centerx = window_width // 2
player_rect.centery = window_height // 2
score = 0 # 設定初始分數
clock = pygame.time.Clock() # 設定遊戲時鐘
coin_rect.x = random.randint(0, window_width - coin_rect.width)
coin_rect.y = random.randint(0, window_height - coin_rect.height)
# 遊戲迴圈
i_offset=0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:running = False
    # 檢查按鍵輸入
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:player_rect.centerx -= 10 ; i_offset = 4
    if keys[pygame.K_RIGHT]:player_rect.centerx += 10; i_offset = 0
    if keys[pygame.K_UP]:player_rect.centery -= 10 ; 
    if keys[pygame.K_DOWN]:player_rect.centery += 10; 
    # 檢查角色是否碰到金幣
    if player_rect.colliderect(coin_rect):
        score += 1 # 角色吃到金幣，金幣消失，分數加1
        coin_rect.x = random.randint(0, window_width - coin_rect.width)
        coin_rect.y = random.randint(0, window_height - coin_rect.height)
    # 清空遊戲視窗
    window.fill(black)
    # 繪製角色和金幣
    window.blit(player_images[i+i_offset], player_rect)
    i=(i+1)%3
    
    window.blit(coin_image, coin_rect)
    # 顯示分數
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, white)
    window.blit(text, (window_width - 150, 10))
    # 更新遊戲視窗
    pygame.display.update()
    #設定遊戲更新頻率
    clock.tick(20)
    
#關閉Pygame
pygame.quit()
