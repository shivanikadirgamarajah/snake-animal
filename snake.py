import pygame
import time
import random

pygame.init()


snake_block=20
snake_speed=15
food_block=20


animal_images=[pygame.transform.scale(pygame.image.load("rabbit.png"),(snake_block, snake_block)),
               pygame.transform.scale(pygame.image.load("pig.png"),(snake_block,snake_block)),
               pygame.transform.scale(pygame.image.load("panda.png"),(snake_block,snake_block)),
               pygame.transform.scale(pygame.image.load("monkey.png"),(snake_block,snake_block))
               ]




food_images=[
    pygame.transform.scale(pygame.image.load("carrot.png"),(food_block, food_block)),
    pygame.transform.scale(pygame.image.load("apple.png"),(food_block, food_block)),
    pygame.transform.scale(pygame.image.load("bamboo.png"),(food_block, food_block)),
    pygame.transform.scale(pygame.image.load("banana.png"),(food_block, food_block))
    ]
    
bgi=pygame.image.load("grass.png")
bgi=pygame.transform.scale(bgi,(600,400))
white=(0,255,255)
yellow=(255,255,102)

red=(255,0,0)
green=(0,255,0)
black=(0,0,0)

dis_width=600
dis_height=400

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake game by Edureka')

clock=pygame.time.Clock()




font_style=pygame.font.SysFont("bahnschrift", 25)
score_font=pygame.font.SysFont("comicansms", 35)

def Your_score(score):
    value=score_font.render("Your Score: "+str(score), True, yellow)
    dis.blit(value, [0,0])
    

def our_snake(snake_block, snake_list,snake_images):
    for pos, img in zip(snake_list, snake_images):
        dis.blit(img, (pos[0], pos[1]))
def message(msg,color):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,[dis_width/6, dis_height/3])
    

    
def gameLoop():
    game_over=False
    game_close=False

    x1=dis_width/2
    y1=dis_height/2

    x1_change=0
    y1_change=0

    snake_List=[]
    snake_images=[]
    Length_of_snake=1
    snake_List.append([x1,y1])
    snake_images.append(random.choice(animal_images))
    foodx=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0
    foody=round(random.randrange(0,dis_height-snake_block)/10.0)*10.0
    while not game_over:
        while game_close==True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_UP:
                    y1_change=-snake_block
                    x1_change=0
                elif event.key==pygame.K_DOWN:
                    y1_change=snake_block
                    x1_change=0
        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            game_close=True
        x1+=x1_change
        y1+=y1_change
        dis.blit(bgi,(0,0))
        head=snake_images[-1]
        animal_index=animal_images.index(head)
        dis.blit(food_images[animal_index],(foodx,foody))
        snake_Head=[x1,y1]
        snake_List.append(snake_Head)
        
        if len(snake_List)> Length_of_snake:
            snake_List.pop(0)
        while len(snake_images)<Length_of_snake:
            snake_images.insert(0,random.choice(animal_images))
        for x in snake_List[:-1]:
            if x==snake_Head:
                game_close=True
        our_snake(snake_block,snake_List,snake_images)
        Your_score(Length_of_snake-1)
        pygame.display.update()

        if (pygame.Rect(x1,y1,snake_block,snake_block).colliderect(pygame.Rect(foodx,foody,food_block,food_block))):
            foodx=round(random.randrange(0,dis_width - snake_block)/ 10.0)*10.0
            foody=round(random.randrange(0,dis_height- snake_block)/10.0)*10.0
            Length_of_snake+=1
            snake_images.append(random.choice(animal_images))
        clock.tick(snake_speed)


    pygame.quit()
    quit()
gameLoop()
