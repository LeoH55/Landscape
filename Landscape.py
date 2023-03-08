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

rect_x = 0
rect_y = 300
rect_change_x = 1
rect_change_y = 1

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (50,200,100)
GREY = (128,128,128)
BLUE = (20,20,210)
BROWN = (139,69,19)
WOOD = (220,181,121)
SUN = (255,255,0)
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

    if r == 2:
        time.sleep(3)
    if r == 0:
        r_change = r_change * (0-1)
        g_change = g_change * (0-1)
        b_change = b_change * (0-1)
    if b == 250:
        r_change = r_change * (0-1)
        g_change = g_change * (0-1)
        b_change = b_change * (0-1)

    screen.fill(NIGHT)
    
    pygame.draw.circle(screen, ORANGE, (rect_x, rect_y), 30)
    pygame.draw.circle(screen, SUN, (rect_x, rect_y), 25)
    rect_x += rect_change_x
    rect_y -= rect_change_y
    if rect_x == 250 and rect_y == 50:
        time.sleep(4)
        rect_change_y = rect_change_y * (0-1)
    elif rect_x == 500 and rect_y == 300:
        rect_change_y = rect_change_y * (0-1)
        rect_x = 0
        rect_y = 300

    pygame.draw.rect(screen, GREEN, [0,250,500,50])
    pygame.draw.rect(screen, GREY, [150,250,350,10])
    pygame.draw.polygon(screen, GREY, [[150,260],[110,260],[110,270]])
    pygame.draw.polygon(screen, GREY, [[90,270],[70,250],[90,250]])
    pygame.draw.rect(screen, GREY, [110,250,40,10])
    pygame.draw.rect(screen, GREY, [90,250,20,20])

    pygame.draw.rect(screen, BLUE, [50,150,100,100])
    pygame.draw.rect(screen, BLACK, [121,105,20,30])
    pygame.draw.polygon(screen, RED, [[100,100],[37.5,150], [162.5,150]])
    pygame.draw.rect(screen, WHITE, [90,210,20,40])
    pygame.draw.rect(screen, BLACK, [90,230,5,5])
    if r <= 5:
        for y_offset in range(1,121,60):
            pygame.draw.rect(screen, SUN, [60+y_offset,160,20,30])
    else:
        for y_offset in range(1,121,60):
            pygame.draw.rect(screen, BLACK, [60+y_offset,160,20,30])
    for y_offset in range(1,241,60):
        pygame.draw.rect(screen, BROWN, [250+y_offset,200,10,50])
        pygame.draw.rect(screen, GREEN, [230+y_offset,160,50,40])



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
