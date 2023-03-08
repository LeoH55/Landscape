import pygame
import time
pygame.init()
done = False

r = 0
g = 0
b = 0
r_change = 1
g_change = 1
b_change = 1

circle_x = 0
circle_y = 300
circle_change_x = 1
circle_change_y = 1

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (50,200,100)
PAVEMENT = (128,128,128)
BLUE = (20,20,210)
WOOD = (139,69,19)
YELLOW = (255,255,0)
ORANGE = (255,165,0)

car_distance = 0
car_speed = 2

size = (500,300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Animation")
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            
    r += r_change
    g += g_change
    b += b_change
    NIGHT = (r,g,b)

    if r == 0:
        time.sleep(3)
        r_change = r_change * (0-1)
        g_change = g_change * (0-1)
        b_change = b_change * (0-1)
    if b == 250:
        r_change = r_change * (0-1)
        g_change = g_change * (0-1)
        b_change = b_change * (0-1)

    screen.fill(NIGHT)
    
    pygame.draw.circle(screen, ORANGE, (circle_x, circle_y), 30)
    pygame.draw.circle(screen, YELLOW, (circle_x, circle_y), 25)
    circle_x += circle_change_x
    circle_y -= circle_change_y
    if circle_x == 250 and circle_y == 50:
        time.sleep(3)
        circle_change_y = circle_change_y * (0-1)
    elif circle_x == 500 and circle_y == 300:
        circle_change_y = circle_change_y * (0-1)
        circle_x = 0
        circle_y = 300

    pygame.draw.rect(screen, GREEN, [0,250,500,50])
    pygame.draw.rect(screen, PAVEMENT, [50,250,450,10])
    pygame.draw.polygon(screen, PAVEMENT, [[150,260],[110,260],[110,270]])
    pygame.draw.polygon(screen, PAVEMENT, [[90,270],[50,260],[90,260]])
    pygame.draw.rect(screen, PAVEMENT, [90,260,20,10])

    pygame.draw.rect(screen, BLUE, [50,150,100,100])
    pygame.draw.rect(screen, BLACK, [121,105,20,30])
    pygame.draw.polygon(screen, RED, [[100,100],[37.5,150], [162.5,150]])
    pygame.draw.rect(screen, WHITE, [90,210,20,40])
    pygame.draw.rect(screen, BLACK, [90,230,5,5])
    if r <= 5:
        for x_offset in range(1,121,60):
            pygame.draw.rect(screen, YELLOW, [60+x_offset,160,20,30])
    else:
        for x_offset in range(1,121,60):
            pygame.draw.rect(screen, BLACK, [60+x_offset,160,20,30])
    for x_offset in range(1,241,60):
        pygame.draw.rect(screen, WOOD, [250+x_offset,200,10,50])
        pygame.draw.circle(screen, GREEN, (240+x_offset,190), 20)
        pygame.draw.circle(screen, GREEN, (265+x_offset,185), 20)
        pygame.draw.circle(screen, GREEN, (252+x_offset,165), 20)

    car_distance += car_speed
    if car_distance == 500:
        car_speed = car_speed * (0-1)
    if car_distance == 0:
        car_speed = car_speed * (0-1)
    pygame.draw.rect(screen, RED, [170+car_distance,225,60,15])
    pygame.draw.rect(screen, RED, [185+car_distance,215,30,20])
    for m in range(1,77,38):
        pygame.draw.circle(screen, BLACK, [180+m+car_distance,240], 8)
    pygame.draw.rect(screen, BLUE, [189+car_distance,218,22,8])
    
    pygame.display.flip()
    clock.tick(50)
    
pygame.quit()
