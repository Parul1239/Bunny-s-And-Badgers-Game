import pygame
from pygame.locals import *
import math
import random


pygame.init()

display_width = 640
display_heigth = 480


black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
yellow = (200,200,0)
marron = (222,184,135)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_yellow = (255,255,0)
bright_marron = (227,189,140)

block_color = (53,115,255)
INST= pygame.image.load(r"D:\Pycharm Projects\Project1\Lib\INST.jpg")
bunny= pygame.image.load(r"D:\Pycharm Projects\Project1\Lib\bunny.jpg")
INST2= pygame.image.load(r"D:\Pycharm Projects\Project1\INST1.PNG")
INST1= pygame.image.load(r"D:\Pycharm Projects\Project1\INST2.PNG")

# 3 - Load images
player = pygame.image.load(r"D:\Pycharm Projects\Project1\Lib\dude.png")
grass = pygame.image.load(r"D:\Pycharm Projects\Project1\Lib\grass.png")
castle = pygame.image.load(r"D:\Pycharm Projects\Project1\Lib\castle.png")
arrow = pygame.image.load(r"D:\Pycharm Projects\Project1\Lib\bullet.png")
badguyimg1 = pygame.image.load(r"D:\Pycharm Projects\Project1\Lib\badguy.png")
badguyimg=badguyimg1
healthbar = pygame.image.load(r"D:\Pycharm Projects\Project1\Lib\healthbar.png")
health = pygame.image.load(r"D:\Pycharm Projects\Project1\Lib\health.png")
gameover = pygame.image.load(r"D:\Pycharm Projects\Project1\Lib\gameover.png")
youwin = pygame.image.load(r"D:\Pycharm Projects\Project1\Lib\youwin.png")

gameDisplay = pygame.display.set_mode((display_width,display_heigth))
pygame.display.set_caption("Bunny's Kingdom")
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, i,a, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, a, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "start":
                game_loop()
            if action == "instructions":
                inst1()
            if action == "next":
                inst2()
            if action == "previous":
                inst1()
            if action == "back":
                game_intro()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, i, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(0)

        # 6 - draw the screen elements
        for x in range(int(display_width /bunny .get_width() + 0)):
            for y in range(int(display_heigth / bunny.get_height() + 0)):
                gameDisplay.blit(bunny, (x * 100, y * 100))

        largeText = pygame.font.Font('freesansbold.ttf',55)
        TextSurf , TextRect = text_objects("Bunny's Kingdom",largeText)
        TextRect.center = ((display_width/2),(display_heigth/3))
        gameDisplay.blit(TextSurf , TextRect)



        button("Start", 220, 240, 200,50, green, bright_green,"start")
        button("Instructions", 220, 320, 200, 50, yellow, bright_yellow, "instructions")
        button("Quit", 220, 400, 200, 50, red, bright_red, "quit")

        mouse = pygame.mouse.get_pos()


        pygame.display.update()
        clock.tick(15)

def inst1():
    ins1 = True

    while ins1:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(0)


        for x in range(int(display_width / INST2.get_width() + 0)):
            for y in range(int(display_heigth / INST2.get_height() + 0)):
                gameDisplay.blit(INST2, (x * 100, y * 100))
        button("NEXT", 500, 380, 100, 50, marron, bright_marron, "next")
        button("BACK", 25, 40, 100, 50, marron, bright_marron, "back")

        mouse = pygame.mouse.get_pos()
        pygame.display.update()

        clock.tick(20)


def inst2():
    ins2 = True

    while ins2:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(0)

        for x in range(int(display_width / INST1.get_width() + 0)):
            for y in range(int(display_heigth / INST1.get_height() + 0)):
                gameDisplay.blit(INST1, (x * 100, y * 100))

        button("Back", 220, 370, 200, 50, marron, bright_marron, "back")
        mouse = pygame.mouse.get_pos()
        pygame.display.update()

        clock.tick(20)


def game_loop():
    keys = [False, False, False, False]
    playerpos = [100, 100]
    acc = [0, 0]
    arrows = []
    badtimer = 100
    badtimer1 = 0
    badguys = [[640, 100]]
    healthvalue = 194
    timestart =pygame.time.get_ticks()
    num_arrows = 200
    running = 1
    exitcode = 0
    # 4 - keep looping through
    while running:
            badtimer -= 1
            # 5 - clear the screen before drawing it again
            gameDisplay.fill(0)
            # 6 - draw the screen elements
            for x in range(int(display_width / grass.get_width() + 1)):
                for y in range(int(display_heigth / grass.get_height() + 1)):
                    gameDisplay.blit(grass, (x * 100, y * 100))
            gameDisplay.blit(castle, (0, 30))
            gameDisplay.blit(castle, (0, 135))
            gameDisplay.blit(castle, (0, 240))
            gameDisplay.blit(castle, (0, 345))
            # 6.1 - Set player position and rotation
            position = pygame.mouse.get_pos()
            angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
            playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)
            playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
            gameDisplay.blit(playerrot, playerpos1)

            # 6.2 - Draw arrows
            for bullet in arrows:
                index = 0
                velx = math.cos(bullet[0]) * 10
                vely = math.sin(bullet[0]) * 10
                bullet[1] += velx
                bullet[2] += vely
                if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
                    arrows.pop(index)
                index += 1
                for projectile in arrows:
                    arrow1 = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)
                    gameDisplay.blit(arrow1, (projectile[1], projectile[2]))

            # 6.3 - Draw badgers
            if badtimer == 0:
                badguys.append([640, random.randint(50, 430)])
                badtimer = 100 - (badtimer1 * 2)
                if badtimer1 >= 35:
                    badtimer1 = 35
                else:
                    badtimer1 += 5
            index = 0
            for badguy in badguys:
                if badguy[0] < -64:
                    badguys.pop(index)
                badguy[0] -= 7

                # 6.3.1 - Attack castle
                badrect = pygame.Rect(badguyimg.get_rect())
                badrect.top = badguy[1]
                badrect.left = badguy[0]
                if badrect.left < 64:
                    healthvalue -= random.randint(5, 20)
                    badguys.pop(index)

                # 6.3.2 - Check for collisions
                index1 = 0
                for bullet in arrows:
                    bullrect = pygame.Rect(arrow.get_rect())
                    bullrect.left = bullet[1]
                    bullrect.top = bullet[2]
                    if badrect.colliderect(bullrect):
                        acc[0] += 1
                        badguys.pop(index)
                        arrows.pop(index1)
                    index1 += 1

            # 6.3.3 - Next bad guy
            index += 1
            for badguy in badguys:
                gameDisplay.blit(badguyimg, badguy)

            # clock
            font = pygame.font.Font(None,24)
            time_remaining  = 90000 -(pygame.time.get_ticks()- timestart)
            survivedtext = font.render(str((time_remaining / 60000)) + ":" + str(time_remaining / 1000 % 60).zfill(2),
                                       True, (0, 0, 0))
            textRect = survivedtext.get_rect()
            textRect.topright = [635, 5]
            gameDisplay.blit(survivedtext, textRect)
            arrowstext = font.render("Remaining arrows: " + str(num_arrows), True, (0, 0, 0))
            arrowsTextRect = arrowstext.get_rect()
            arrowsTextRect.topright = [635, 20]
            gameDisplay.blit(arrowstext, arrowsTextRect)
            # 6.5 - Draw health bar
            gameDisplay.blit(healthbar, (5, 5))
            for health1 in  range(healthvalue):
                gameDisplay.blit(health, (health1 + 8, 8))

            # 7 - update the screen
            pygame.display.flip()

            # 8 - loop through the events
            for event in pygame.event.get():
                # check if the event is the X button
                if event.type == pygame.QUIT:
                    # if it is quit the game
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == K_w:
                        keys[0] = True
                    elif event.key == K_a:
                        keys[1] = True
                    elif event.key == K_s:
                        keys[2] = True
                    elif event.key == K_d:
                        keys[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        keys[0] = False
                    elif event.key == pygame.K_a:
                        keys[1] = False
                    elif event.key == pygame.K_s:
                        keys[2] = False
                    elif event.key == pygame.K_d:
                        keys[3] = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    acc[1] += 1
                    arrows.append(
                        [math.atan2(position[1] - (playerpos1[1] + 32), position[0] - (playerpos1[0] + 26)),
                         playerpos1[0] + 32,
                         playerpos1[1] + 32])
                    num_arrows -= 1
            # 9 - Move player
            if keys[0]:
                playerpos[1] -= 5
            elif keys[2]:
                playerpos[1] += 5
            if keys[1]:
                playerpos[0] -= 5
            elif keys[3]:
                playerpos[0] += 5

                # 10 - Win/Lose check
            timenow = pygame.time.get_ticks()
            if timenow - timestart >= 90000:
                running = 0
                exitcode = 1
            if healthvalue <= 0:
                running = 0
                exitcode = 0
            if num_arrows == 0:
                running = 0
                exitcode = 0
            if acc[1] != 0:
                accuracy = round(acc[0] * 1.0 / acc[1] * 100, 2)
            else:
                accuracy = 0

            # 11 - Win/lose display
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    elapsedtime = pygame.time.get_ticks() - timestart / 1000

    game_over_message = ""
    if num_arrows == 0:
        game_over_message = "You have run out of arrows!!! "

    game_over_message += "Score: " + str(accuracy)
    text = font.render(game_over_message, True, (0, 255, 0))

    textRect = text.get_rect()
    textRect.centerx = gameDisplay.get_rect().centerx
    textRect.centery = gameDisplay.get_rect().centery + 24
    if exitcode == 0:
        gameDisplay.blit(gameover, (0, 0))
    else:
        gameDisplay.blit(youwin, (0, 0))
    gameDisplay.blit(text, textRect)
    pygame.display.flip()




    pygame.time.delay(10000)
    pygame.display.update()

#game_loop()
#while 1:
    #for event in pygame.event.get():
      #if event.type == pygame.QUIT:
       #     pygame.quit()
        #    exit(0)
      #elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
       #     x, y = event.pos
        #    if x >= textx - 5 and x <= textx + textx_size + 5:
         #       if y >= texty - 5 and y <= texty + texty_size + 5:
          #          game_loop()
           #         break
            #if x >= text2x - 5 and x <= text2x + text2x_size + 5:
             #    if y >= text2y - 5 and y <= text2y + text2y_size + 5:
              #      pygame.quit()
               #     exit(0)

game_intro()
inst1()
inst2()
game_loop()

pygame.quit()
quit()





