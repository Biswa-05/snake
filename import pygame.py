import pygame
import random
pygame.init()

red=(255,0,0)
black= (0, 0, 0, 255)
blue=(0, 0, 255, 255),
cyan= (0, 255, 255, 255),
gold= (255, 215, 0, 255),
gray=(190, 190, 190, 255),
green=(0, 255, 0, 255),
orange= (255, 165, 0, 255),
purple=(160, 32, 240, 255),
red= (255, 0, 0, 255),
violet= (238, 130, 238, 255)
yellow=(255, 255, 0, 255)
white=(255,255,255,255)

screen_width=600
screen_height=600

gameWindow=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Bisu The Snake")
pygame.display.update()

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,25)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color, [x,y,snake_size,snake_size])
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(green)
        text_screen("Saapon ki duniya mai apka swagat hai ",black,150,250)
        text_screen("Khelna hai toh spacebar daba ",black,185,290)

        for event in pygame.event.get():
            if event.type==pygame.event.get():
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)
                

    
def gameloop():
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    velocity_x=0
    velocity_y=0
    food_x=random.randint(20, screen_width//2)
    food_y=random.randint(20, screen_height//2)
    score=0
    init_velocity = 5
    snake_size=30
    fps=60
    snk_list=[]
    snk_length=1
    while not exit_game:
        if game_over:      
            gameWindow.fill(cyan)
            text_screen("Saanp mar gaya!! Chal enter daba phirse khelna hai toh",red,80,250)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                     if event.key==pygame.K_LEFT:
                         velocity_x=-init_velocity
                         velocity_y=0
                     if event.key==pygame.K_UP:
                         velocity_y=-init_velocity
                         velocity_x=0
                     if event.key==pygame.K_DOWN:
                         velocity_y=init_velocity
                         velocity_x=0
            snake_x=snake_x + velocity_x
            snake_y=snake_y + velocity_y

            if ((abs(snake_x - food_x)<20) and ( abs(snake_y  -  food_y)<20)):
                score+=1
                food_x=random.randint(20, screen_width//2)
                food_y=random.randint(20, screen_height//2)
                snk_length+=3
        
            gameWindow.fill(gold)
            text_screen("Score:   "+str(score*10),red,5,5)
            pygame.draw.rect(gameWindow,red, [food_x,food_y,snake_size,snake_size])

            head=[]
            head.append(snake_x,)
            head.append(snake_y,)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                    game_over=True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                
                
            pygame.draw.rect(gameWindow,black, [snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
    
        
