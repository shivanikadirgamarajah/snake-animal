import pygame
import time
import random
import os

pygame.init()
pygame.mixer.init()

# Load sound effects
try:
    eat_sound = pygame.mixer.Sound("eat.mp3")
except:
    eat_sound = None
    
try:
    game_over_sound = pygame.mixer.Sound("gameover.wav")
except:
    game_over_sound = None

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
bgi=pygame.transform.scale(bgi,(520,480))

# Modern UI Colors - Neon/Gaming theme
white=(0,255,255)
yellow=(255,255,102)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)
dark_green=(34,139,34)
light_gray=(240,240,240)
ui_bg=(20,20,30)  # Dark blue-gray
ui_text=(255,255,255)
neon_cyan=(0,255,255)
neon_magenta=(255,0,127)
neon_green=(0,255,100)
accent_color=(0,200,255)
sidebar_bg=(30,30,50)

# Window dimensions
dis_width=750
dis_height=530

# Game area dimensions
game_width=520
game_height=480
game_x=15
game_y=25
sidebar_x=555
sidebar_width=175

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake-Animal Game')

clock=pygame.time.Clock()
# Global variable for food eat animation
food_flash_timer = 0



font_style=pygame.font.SysFont("bahnschrift", 24)
score_font=pygame.font.SysFont("comicansms", 42, bold=True)
title_font=pygame.font.SysFont("bahnschrift", 32, bold=True)
small_font=pygame.font.SysFont("bahnschrift", 16)
label_font=pygame.font.SysFont("bahnschrift", 14, bold=True)
instr_font=pygame.font.SysFont("bahnschrift", 11)

def Your_score(score):
    # Draw score in sidebar
    value=score_font.render(str(score), True, yellow)
    dis.blit(value, [sidebar_x+20, 80])

def draw_sidebar(score, speed):
    # Draw sidebar background with gradient effect
    pygame.draw.rect(dis, sidebar_bg, (sidebar_x-8, game_y-5, sidebar_width+16, game_height+10))
    pygame.draw.rect(dis, neon_cyan, (sidebar_x-8, game_y-5, sidebar_width+16, game_height+10), 3)
    pygame.draw.line(dis, neon_magenta, (sidebar_x-8, game_y+60), (sidebar_x+sidebar_width+8, game_y+60), 2)
    
    # Draw title with accent
    title=title_font.render("STATS", True, neon_cyan)
    dis.blit(title, [sidebar_x+10, game_y+10])
    
    # Draw score section
    score_label=label_font.render("SCORE", True, accent_color)
    dis.blit(score_label, [sidebar_x+15, game_y+75])
    score_value=score_font.render(str(score), True, neon_magenta)
    dis.blit(score_value, [sidebar_x+18, game_y+95])
    
    # Draw speed section
    speed_label=label_font.render("SPEED", True, accent_color)
    dis.blit(speed_label, [sidebar_x+15, game_y+165])
    speed_text=score_font.render(str(speed), True, neon_green)
    dis.blit(speed_text, [sidebar_x+18, game_y+185])
    
    # Draw decorative line
    pygame.draw.line(dis, neon_magenta, (sidebar_x+10, game_y+260), (sidebar_x+sidebar_width-10, game_y+260), 1)
    
    # Draw instructions
    instr_label=label_font.render("CONTROLS", True, accent_color)
    dis.blit(instr_label, [sidebar_x+15, game_y+280])
    
    arrows=instr_font.render("use arrow keys to move", True, light_gray)
    dis.blit(arrows, [sidebar_x+25, game_y+310])
    
    q_text=instr_font.render("Q = Quit", True, light_gray)
    dis.blit(q_text, [sidebar_x+15, game_y+360])
    
    c_text=instr_font.render("C = Restart", True, light_gray)
    dis.blit(c_text, [sidebar_x+15, game_y+385])

def draw_game_border():
    # Draw double border with neon effect
    pygame.draw.rect(dis, neon_cyan, (game_x-3, game_y-3, game_width+6, game_height+6), 2)
    pygame.draw.rect(dis, neon_magenta, (game_x-6, game_y-6, game_width+12, game_height+12), 1)
    pygame.draw.rect(dis, neon_cyan, (game_x, game_y, game_width, game_height), 1)
    

def our_snake(snake_block, snake_list,snake_images):
    for pos, img in zip(snake_list, snake_images):
        dis.blit(img, (game_x + pos[0], game_y + pos[1]))
def message(msg, color):
    # Draw styled message with background
    large_font = pygame.font.SysFont("bahnschrift", 28, bold=True)
    mesg=large_font.render(msg, True, color)
    msg_width = mesg.get_width()
    msg_height = mesg.get_height()
    msg_x = game_x + (game_width - msg_width) // 2
    msg_y = game_y + (game_height - msg_height) // 2 - 30
    
    # Draw background box with neon effect
    box_x, box_y = msg_x-30, msg_y-25
    box_w, box_h = msg_width+60, msg_height+50
    pygame.draw.rect(dis, (0,0,0), (box_x, box_y, box_w, box_h))
    pygame.draw.rect(dis, color, (box_x, box_y, box_w, box_h), 3)
    pygame.draw.rect(dis, neon_magenta, (box_x-2, box_y-2, box_w+4, box_h+4), 1)
    
    dis.blit(mesg, [msg_x, msg_y])

def play_game_over_sound():
    if game_over_sound:
        game_over_sound.play()

    
def gameLoop():
    game_over=False
    game_close=False

    x1=game_width/2
    y1=game_height/2

    x1_change=0
    y1_change=0

    snake_List=[]
    snake_images=[]
    Length_of_snake=1
    snake_List.append([x1,y1])
    snake_images.append(random.choice(animal_images))
    foodx=round(random.randrange(0,game_width-snake_block)/10.0)*10.0
    foody=round(random.randrange(0,game_height-snake_block)/10.0)*10.0
    while not game_over:
        while game_close==True:
            dis.fill(ui_bg)
            
            # Draw decorative elements
            pygame.draw.rect(dis, sidebar_bg, (0, 0, dis_width, game_y-5))
            pygame.draw.line(dis, neon_magenta, (0, game_y-2), (dis_width, game_y-2), 2)
            
            pygame.draw.rect(dis, dark_green, (game_x-3, game_y-3, game_width+6, game_height+6), 2)
            dis.blit(bgi, (game_x, game_y))
            
            # Show game over message
            message("GAME OVER!", red)
            
            # Draw final score in center
            final_score_text = score_font.render(f"Final Score: {Length_of_snake-1}", True, neon_magenta)
            score_x = game_x + (game_width - final_score_text.get_width()) // 2
            score_y = game_y + game_height // 2 + 60
            pygame.draw.rect(dis, (0,0,0), (score_x-20, score_y-10, final_score_text.get_width()+40, 40), 0)
            pygame.draw.rect(dis, neon_magenta, (score_x-20, score_y-10, final_score_text.get_width()+40, 40), 2)
            dis.blit(final_score_text, [score_x, score_y])
            
            # Draw sidebar with final stats
            draw_sidebar(Length_of_snake-1, snake_speed)
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
        if x1>=game_width or x1<0 or y1>=game_height or y1<0:
            play_game_over_sound()
            game_close=True
        x1+=x1_change
        y1+=y1_change
        
        # Draw game background
        dis.fill(ui_bg)
        
        # Draw decorative top bar
        pygame.draw.rect(dis, sidebar_bg, (0, 0, dis_width, game_y-5))
        pygame.draw.line(dis, neon_magenta, (0, game_y-2), (dis_width, game_y-2), 2)
        
        # Draw title in top bar
        top_title = title_font.render('🐍 SNAKE ANIMALS 🎮', True, neon_cyan)
        title_rect = top_title.get_rect()
        title_x = (game_width - title_rect.width) // 2 + game_x
        dis.blit(top_title, [title_x, game_y-23])
        
        dis.blit(bgi,(game_x, game_y))
        
        # Draw food with glow effect
        head=snake_images[-1]
        animal_index=animal_images.index(head)
        dis.blit(food_images[animal_index],(game_x + foodx, game_y + foody))
        snake_Head=[x1,y1]
        snake_List.append(snake_Head)
        
        if len(snake_List)> Length_of_snake:
            snake_List.pop(0)
        while len(snake_images)<Length_of_snake:
            snake_images.insert(0,random.choice(animal_images))
        for x in snake_List[:-1]:
            if x==snake_Head:
                play_game_over_sound()
                game_close=True
        # Draw game border and UI
        draw_game_border()
        draw_sidebar(Length_of_snake-1, snake_speed)
        
        # Draw snake
        our_snake(snake_block,snake_List,snake_images)
        pygame.display.update()

        if (pygame.Rect(game_x+x1,game_y+y1,snake_block,snake_block).colliderect(pygame.Rect(game_x+foodx,game_y+foody,food_block,food_block))):
            if eat_sound:
                eat_sound.play()
            foodx=round(random.randrange(0, game_width - snake_block) / 10.0) * 10.0
            foody=round(random.randrange(0, game_height - snake_block) / 10.0) * 10.0
            Length_of_snake+=1
            snake_images.append(random.choice(animal_images))
        clock.tick(snake_speed)


    pygame.quit()
    quit()
gameLoop()
