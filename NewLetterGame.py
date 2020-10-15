

# New Draft
# September 8, 2020

# imports
import pygame
import random
import string
import csv

# Intro Terminal message                        Game has issues
print("Welcome to NOSU (Not Osu) " + '\n' + "The game involves pressing the letter on screen " + '\n' +
      "and gaining a point for the correct key." + '\n' +
      "Notice some bugs.")


#setup
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('NOSU')
done = False
datawrite = open("Data.csv","a+")


# Colours
green = (64,215,0)
brown = (105, 54, 19)
grey = (114, 114, 114)
red = (186, 9, 9)
blue = (8,141,208)
pink = (186,0,206)
yellow = (252,210,0)
black = (0,0,0)
colours = [green,brown,grey,red,blue,pink,yellow]
character = random.choice(string.ascii_letters)
count = 0

#screen
screen.fill((255,255,255))
TitleFormat = pygame.font.Font('NewFont.ttf',90)
TitleSurface = TitleFormat.render('nosu',False,(0,0,0))
screen.blit(TitleSurface,(210,0))
pygame.display.update()

def rand():
    random.choice(string.ascii_letters)

def letter_gen():
    global TitleSurface
    letter = pygame.font.Font('NewFont.ttf',30)
    x = random.randrange(30,530)
    y = random.randrange(80,540)
    screen.blit(letter.render(rand(),False, black), (x,y))
    writer = csv.writer(datawrite)
    writer.writerow(random.choice(string.ascii_letters))

    #Score
    count_font = pygame.font.Font('NewFont.ttf',15)
    screen.blit(count_font.render("Score: " + str(count),False,black),(260,70))
    pygame.display.update()

def main():
    global count, done, TitleSurface,character
    letter_gen()
    writer = csv.writer(datawrite)
    writer.writerow(random.choice(string.ascii_letters))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(1111010110)
            if event.type == pygame.KEYDOWN:
                typed_key = pygame.key.name(event.key)
                if typed_key == rand():
                    count += 1
                else:
                    count += 0


            # if event.type == pygame.KEYDOWN:
            #     if event.key == rand():
            #         count += 1

                screen.fill((255, 255, 255))
            TitleFormat = pygame.font.Font('NewFont.ttf', 90)
               TitleSurface = TitleFormat.render('nosu', False, (0, 0, 0))
               screen.blit(TitleSurface, (210, 0))

               letter = pygame.font.Font('NewFont.ttf', 30)
               x = random.randrange(30, 530)
               y = random.randrange(80, 540)
               screen.blit(letter.render(random.choice(string.ascii_letters), False, black), (x, y))
               writer.writerow(character)

               # Score
               count_font = pygame.font.Font('NewFont.ttf', 15)
               screen.blit(count_font.render("Score: " + str(count), False, black), (260, 70))
               pygame.display.update()





    pygame.display.flip()






if __name__ == '__main__':
    main()

