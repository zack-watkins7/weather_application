from tkinter import font
from turtle import Screen
import pygame
import random
import sys 

#basic things we need in the game
#reset function
#reward system our agent gets food= 10 die= -10 other=0
#play(action) --> direction
#game_iter
# is_collision


class SnakeAI():
    def __init__(self):
        self.length=1
        self.boardposition = [((display_width / 2), (display_height / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17,24,30)
        self.score = 0
        self.reset()
        
    def head_position(self):
        return self.boardposition[0] #the snakes body is stored in a list where the head is always defined as the first element of that list
        
    
    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction: # makes it so that if your snake is longer than 1 you cannot make a 180 degree turn
            return # this return specifically doesnt let you make the 180 turn
        else:
            self.direction = point
    
    def move(self):
        self.iteration +=1
        #self.head_position()
        current=self.head_position()
        x,y= self.direction
        new_snake_position= ((current[0]+(x*grid_size)), (current[1]+(y*grid_size)) )
        x_coord= new_snake_position[0]
        y_coord= new_snake_position[1]
        self.reward=0
        
        #says if snake is longer than 2 squares and if it collides with itself or the wall it will trigger a reset
        if len(self.boardposition) > 2 and new_snake_position in self.boardposition[2:] or x_coord >= display_width or x_coord < 0 or y_coord >= display_height or y_coord < 0:
            self.reward=-10
            game_over = True
            self.reset()
            return self.score, game_over

        else:
            self.boardposition.insert(0, new_snake_position) # makes sure the snake doesn't grow while moving around the board
            if len(self.boardposition)> self.length:
                self.boardposition.pop()
        
    
    def reset(self):
        self.length = 1
        self.boardposition = [((display_width / 2), (display_height / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score= 0
        self.iteration= 0

    def draw(self, surface):
        for i in self.boardposition:
            snake_rectangle= pygame.Rect((i[0],i[1]), (grid_size, grid_size))
            pygame.draw.rect(surface, (150,200,200), snake_rectangle)
            pygame.draw.rect(surface, self.color, snake_rectangle,1)



    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(DOWN)
                elif event.key == pygame.K_DOWN:
                    self.turn(UP)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
                
                elif event.key == pygame.K_ESCAPE:
                    paused = True
                    while paused:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key== pygame.K_q:
                                    pygame.quit()
                                    quit()
                                elif event.key == pygame.K_c:
                                    paused= False

def draw_grid(surface):
    for y in range(0,int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y) % 2 == 0:
                r= pygame.Rect((x*grid_size, y*grid_size),(grid_size, grid_size))
                pygame.draw.rect(surface, (93,30,16), r)
            else:
                rr= pygame.Rect((x*grid_size, y*grid_size),(grid_size,grid_size))
                pygame.draw.rect(surface,(80,80,80), rr)

class Food(object):
    def __init__(self):
        self.position = (0,0)
        self.color = (255,160, 200)
        self.random_position()

    def random_position(self):
        self.position = (random.randint(0, grid_width-1)* grid_size, random.randint(0, grid_height-1)*grid_size)
    
    def draw(self, surface):
        draw_food= pygame.Rect((self.position[0], self.position[1]),(grid_size, grid_size))
        pygame.draw.rect(surface, self.color, draw_food)
        pygame.draw.rect(surface,(255,255,255), draw_food, 1)

display_width= 800
display_height = 480
game_display= pygame.display.set_mode((display_width,display_height))
grid_size = 20
grid_width= display_width / grid_size
grid_height= display_height / grid_size



UP= (0,1)
DOWN=(0,-1)
LEFT=(-1,0)
RIGHT=(1,0)



def GameLoop():
    pygame.init()
    snake= SnakeAI()
    food= Food()
    clock= pygame.time.Clock()
    screen= pygame.display.set_mode((display_width, display_height),0, 32)
#getting the size of the screen
    surface= pygame.Surface(screen.get_size())
    surface= surface.convert()

    draw_grid(surface)


    Font= pygame.font.SysFont("monospace", 20)
    while (True):
        clock.tick(10)
        snake.handle_keys()
        draw_grid(surface)
        snake.move()
        if snake.head_position() == food.position:
            snake.reward= 10
            snake.length += 1
            snake.score += 1
            food.random_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface,(0,0))
        score_text= Font.render("Your score is {0}".format(snake.score), 1 ,(255,255,255))
        screen.blit(score_text, (5,10))
        pygame.display.update()

GameLoop()