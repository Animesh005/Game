import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("car_sound.wav")

dispaly_width = 800
dispaly_hight = 700

initial_pos = [230, 430]

road_startx = 205
road_finishx = 605

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

light_red = (150, 0, 0)
light_green = (0, 150, 0)

car_width = 100
car_height = 168

pause = False
crashed = True
intro = True

game_introduction1 = "This is a car race.And you have to dodge each car coming towars you."
game_introduction2 = "Also you have to keep your car within the road."
game_introduction3 = "Othewise you will crash."

gameDisplay = pygame.display.set_mode((dispaly_width, dispaly_hight))

pygame.display.set_caption('A Car Race')

clock = pygame.time.Clock()

carImg = pygame.image.load('car1.png')
car2Img = pygame.image.load('car3.png')
roadImg = pygame.image.load('road2.png')

pygame.display.set_icon(carImg)

def thing_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged : "+str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy):
    gameDisplay.blit(car2Img, (thingx, thingy))

def road(roadx, roady):
    gameDisplay.blit(roadImg, (roadx, roady))

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText)

    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def game_intro_2():
    global intro, game_introduction1, game_introduction2, game_introduction3
    intro = False
    intro2 = True

    while intro2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        large_Text1 = pygame.font.Font('freesansbold.ttf', 20)
        Text_Surface1, Text_Rectangle1 = text_objects(game_introduction1, large_Text1)
        Text_Rectangle1.center = (400, 100)

        gameDisplay.blit(Text_Surface1, Text_Rectangle1)

        large_Text2 = pygame.font.Font('freesansbold.ttf', 20)
        Text_Surface2, Text_Rectangle2 = text_objects(game_introduction2, large_Text2)
        Text_Rectangle2.center = (400, 150)

        gameDisplay.blit(Text_Surface2, Text_Rectangle2)

        large_Text3 = pygame.font.Font('freesansbold.ttf', 20)
        Text_Surface3, Text_Rectangle3 = text_objects(game_introduction3, large_Text3)
        Text_Rectangle3.center = (400, 200)

        gameDisplay.blit(Text_Surface3, Text_Rectangle3)

        button("GO!", 150, 550, 100, 50, light_green, green, game_loop)
        button("Back", 450, 550, 100, 50, light_red, red, game_intro)

        pygame.display.update()
        clock.tick(60)



def quiteGame():
    pygame.quit()
    quit()

def game_intro():
    global intro

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurface, TextRectangle = text_objects("A Bit Racy", largeText)
        TextRectangle.center = ((dispaly_width / 2), (dispaly_hight / 2))
        gameDisplay.blit(TextSurface, TextRectangle)

        button("Play", 150, 450, 100, 50, light_green, green, game_intro_2)
        button("Quit", 450, 450, 100, 50, light_red, red, quiteGame)

        pygame.display.update()
        clock.tick(20)

def unpause():
    global pause

    pygame.mixer.music.unpause()

    pause = False

def Pause():

    pygame.mixer.music.pause()

    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurface, TextRectangle = text_objects("pause", largeText)
    TextRectangle.center = ((dispaly_width / 2), (dispaly_hight / 2))
    gameDisplay.blit(TextSurface, TextRectangle)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)


        button("Continue", 150, 450, 100, 50, light_green, green, unpause)
        button("Quit", 450, 450, 100, 50, light_red, red, quiteGame)

        pygame.display.update()
        clock.tick(20)

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurface, TextRectangle = text_objects(text, largeText)
    TextRectangle.center = ((dispaly_width / 2), (dispaly_hight / 2))
    gameDisplay.blit(TextSurface, TextRectangle)

    pygame.display.update()

    time.sleep(2)
    game_loop()

def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    global crashed

    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurface, TextRectangle = text_objects("You Crashed", largeText)
    TextRectangle.center = ((dispaly_width / 2), (dispaly_hight / 2))
    gameDisplay.blit(TextSurface, TextRectangle)

    while crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)


        button("Play Again", 150, 450, 110, 50, light_green, green, game_loop)
        button("Quit", 450, 450, 100, 50, light_red, red, quiteGame)

        pygame.display.update()
        clock.tick(20)

def game_loop():

    pygame.mixer.music.play(-1)

    global pause

    x = (dispaly_width * 0.35)
    y = (dispaly_hight * 0.65)

    x_change = 0

    thing_startx = random.choice(initial_pos)
    thing_starty = -100

    thing_speed = 6
    thing_speed_change = 1
    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10

                if event.key == pygame.K_p:
                    pause = True
                    Pause()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


            if event == pygame.key.get_pressed():

                #keystate = pygame.key.get_pressed()
                if event[pygame.K_UP]:
                    thing_speed += thing_speed_change

                if event[pygame.K_DOWN]:
                    thing_speed -= thing_speed_change

                #keystate = pygame.key.get_pressed()


            #print(event)

        x += x_change

        gameDisplay.fill(white)

        road(-100, 0)

        things(thing_startx, thing_starty)
        thing_starty += thing_speed

        car(x, y)
        thing_dodged(dodged)

        if x > road_finishx - car_width or x < road_startx:
            crash()

        if thing_starty > dispaly_hight:
            thing_starty = -100
            thing_startx = random.choice(initial_pos)
            dodged += 1
            thing_speed += 1

        if y < thing_starty + car_height:

            if x > thing_startx and x < thing_startx + car_width or x + car_width > thing_startx and x + car_width < thing_startx + car_width:
                crash()

        pygame.display.update()

        clock.tick(120)


game_intro()


#game_loop()
pygame.quit()
quit()
