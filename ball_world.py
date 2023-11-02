import pygame
from pygame.locals import *
from ball import Ball

screen_width = 640
screen_height = 480
frame_rate = 60

def ball_world():
    # Initialize pygame
    pygame.init()
    list_balls =[]

    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bouncing Ball")

    # Create Ball instances
    for ball in range(1,11):
        ball = Ball(screen, screen_width, screen_height)
        list_balls.append(ball)


    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen once per frame
        screen.fill((0, 0, 0))

        for ball in list_balls:
            ball.draw(1)
            ball.move()


        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    ball_world()
