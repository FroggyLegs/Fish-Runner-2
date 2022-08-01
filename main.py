from sprite import *
from player_input import *

width = 1040
height = 380
bg_i = 0

win = pygame.display.set_mode((width, height))
bg = pygame.image.load("./images/background.jpg").convert()
bg = pygame.transform.scale(bg, (width, height))
fish_img = pygame.image.load("./images/fish.png")
shark_img = pygame.image.load("./images/shark.png")
pygame.display.set_caption("Fish Runner")
clock = pygame.time.Clock()

gamerunning = True

while gamerunning:
    win.fill((0, 0, 0))
    clock.tick(60)
    win.blit(bg, (bg_i, 0))
    win.blit(bg, (width+bg_i, 0))
    if bg_i == -width:
        win.blit(bg, (width+bg_i, 0))
        bg_i = 0
    bg_i -= 8
    win.blit(fish_img, (fish.x, fish.y))
    win.blit(shark_img, (shark.x, shark.y))
    shark.x -= shark.speed
    get_input()
    print(fish.y)
    pygame.display.update()
