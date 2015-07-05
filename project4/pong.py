# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
HALF_HEIGHT = HEIGHT / 2
HALF_WIDTH = WIDTH / 2
#ball variables
BALL_RADIUS = 20
BALL_POS = [WIDTH / 2 , HEIGHT / 2]
BALL_VEL = [2,3]
#paddles variables
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
#adding paddings initials positions
paddle_l = [[HALF_PAD_WIDTH,HALF_HEIGHT - HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, HALF_HEIGHT + HALF_PAD_HEIGHT ]]
paddle_r = [[WIDTH-1-HALF_PAD_WIDTH,HALF_HEIGHT - HALF_PAD_HEIGHT],[WIDTH-1-HALF_PAD_WIDTH,HALF_HEIGHT + HALF_PAD_HEIGHT]]
paddle1_pos = (HEIGHT / 2)
paddle2_pos = (HEIGHT / 2)
# paddle's velocities
paddle1_vel = 0
paddle2_vel = 0
# direction
LEFT = True
RIGHT = False
# Scores
score1 = 0
score2 = 0
rand1 = 0
rand2 = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global BALL_POS, BALL_VEL # these are vectors stored as lists
    global WIDTH, HEIGHT, rand1, rand2

    BALL_POS[0] = WIDTH / 2
    BALL_POS[1] = HEIGHT / 2

    if direction is RIGHT:
        rand1 = random.randrange(120, 240)
        rand2 = random.randrange(60, 180)
        print 'right', rand1, rand2
        BALL_VEL[0] -= rand1 / 1000
        BALL_VEL[1] -= rand2 / 1000
    elif direction is LEFT:
        rand1 = random.randrange(120, 240)
        rand2 = random.randrange(60, 180)
        print 'left', rand1, rand2
        BALL_VEL[0] -=  (rand1 / 1000)
        BALL_VEL[1] -=  (rand2 / 1000)

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, BALL_POS, BALL_VEL, BALL_RADIUS
    global paddle_l, paddle_r

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "Red")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "Yellow")

    # update ball
    BALL_POS[0] += BALL_VEL[0]
    BALL_POS[1] += BALL_VEL[1]
    if BALL_POS[1] <= BALL_RADIUS:
        BALL_VEL[1] = - BALL_VEL[1]
    elif BALL_POS[1] >= ((HEIGHT - 1) - BALL_RADIUS):
        BALL_VEL[1] = - BALL_VEL[1]

    # draw ball
    canvas.draw_circle(BALL_POS, BALL_RADIUS, 2, "Red", "White")

    # update paddle's vertical position, keep paddle on the screen

    #print paddle1_vel , paddle_l[0][1] , paddle_l[1][1]
    #print paddle2_vel , paddle_r[0][1] , paddle_r[1][1]

    #limit paddle in the top left
    if ((paddle_l[0][1] - abs(paddle1_vel)) > 0) and ((paddle_l[1][1]-PAD_HEIGHT - abs(paddle1_vel)) > 0) \
    and paddle1_vel < 0:
        paddle_l[0][1] += paddle1_vel
        paddle_l[1][1] += paddle1_vel
    #limit paddle in the bottom left
    if ((paddle_l[0][1] + PAD_HEIGHT + abs(paddle1_vel)) < HEIGHT) and \
       ((paddle_l[1][1] + abs(paddle1_vel)) < HEIGHT ) and paddle1_vel > 0:
            paddle_l[0][1] += paddle1_vel
            paddle_l[1][1] += paddle1_vel

    #limit paddle in the top right
    if ((paddle_r[0][1] - abs(paddle2_vel)) > 0) and ((paddle_r[1][1]-PAD_HEIGHT - abs(paddle2_vel)) > 0) \
    and paddle2_vel < 0:
        paddle_r[0][1] += paddle2_vel
        paddle_r[1][1] += paddle2_vel
    #limit paddle in the bottom right
    if ((paddle_r[0][1] + PAD_HEIGHT + abs(paddle2_vel)) < HEIGHT) and \
       ((paddle_r[1][1] + abs(paddle2_vel)) < HEIGHT ) and paddle2_vel > 0:
            paddle_r[0][1] += paddle2_vel
            paddle_r[1][1] += paddle2_vel

    # draw paddles
    canvas.draw_line(paddle_l[0],paddle_l[1],PAD_WIDTH,"White")
    canvas.draw_line(paddle_r[0],paddle_r[1],PAD_WIDTH,"Yellow")

    # determine whether paddle and ball collide
    if  ((BALL_POS[1] < paddle_l[0][1] or BALL_POS[1] > paddle_l[1][1]) and BALL_POS[0] == PAD_WIDTH):
        score2 += 1
        spawn_ball(RIGHT)
    elif (BALL_POS[1] >= paddle_l[0][1] and BALL_POS[1] <= paddle_l[1][1] and BALL_POS[0] == PAD_WIDTH):
        #print 'collide to the right'
        BALL_VEL[0] = - BALL_VEL[0]
        spawn_ball(RIGHT)
    elif ((BALL_POS[1] < paddle_r[0][1] or BALL_POS[1] > paddle_r[1][1]) and BALL_POS[0] == (WIDTH - PAD_WIDTH)):
        score1 += 1
        spawn_ball(LEFT)
    elif (BALL_POS[1] >= paddle_r[0][1] and BALL_POS[1] <= paddle_r[1][1] and BALL_POS[0] == (WIDTH - PAD_WIDTH)):
        #print 'collide to the left'
        BALL_VEL[0] = - BALL_VEL[0]
        spawn_ball(LEFT)


    # draw scores
    canvas.draw_text(str(score1), ((WIDTH / 2) - 40, HEIGHT - 350), 35, 'White')
    canvas.draw_text(str(score2), ((WIDTH / 2) + 25, HEIGHT - 350), 35, 'Yellow')

    #draw reset button


def keydown(key):
    global paddle1_vel, paddle2_vel, my_key
    acc = 3
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

def button_handler():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', button_handler)


# start frame
new_game()
frame.start()
