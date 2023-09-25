import pygame
import random
import os

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Kunkun Dance")
clock = pygame.time.Clock()

kunkun_images = []
for i in range(0, 10):
    image = pygame.image.load(f"kunkun_{i}.png").convert_alpha()
    kunkun_images.append(image)


kunkun_x, kunkun_y = 200, 150
kunkun_speed_x, kunkun_speed_y = 5, 5


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新坤坤跳舞的位置和速度
    kunkun_x += kunkun_speed_x
    kunkun_y += kunkun_speed_y
    if kunkun_x < 0 or kunkun_x > width: 
        kunkun_speed_x = -kunkun_speed_x
    if kunkun_y < 0 or kunkun_y > height:
        kunkun_speed_y = -kunkun_speed_y

    # 绘制坤坤跳舞的图片
    kunkun_image = random.choice(kunkun_images)
    screen.blit(kunkun_image, (kunkun_x, kunkun_y))

    pygame.display.update()
    clock.tick(5)

os.system("pause")
pygame.quit()