# "Stopwatch: The Game"

# Import modules
import simplegui
import random

# define global variables
interval = 100
seg = 0
x = 0
y = 0
width = 400
height = 400
position = [145, 210]
wins = str(x) + "/" + str(y)

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """ format A:BC.D """
    a = 0
    b = 0
    c = 0
    d = 0
    temp = str(t)
    if t > 0 and t <= 9:
        d = t
    elif t > 10  and t <= 99:
        d = t % 10
        c = t / 10
    elif t > 99 and t <= 599:
        b = temp[0]
        c = temp[1]
        d = temp[2]
    elif t > 599 and t <= 5999:
        a = t / 60 / 10
        mod_600 = t % 600
        if mod_600 > 0 and mod_600 <= 9:
            d = mod_600
        elif mod_600 > 9 and mod_600 <= 99:
            d = mod_600 % 10
            c = mod_600 / 10
        elif mod_600 > 99 and mod_600 <= 599:
            temp = str(mod_600)
            b = temp[0]
            c = temp[1]
            d = temp[2]
    return str(a) + ":" + str(b) + str(c) + "." + str(d)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_btn_hanlder():
    timer.start()

def stop_btn_hanlder():
    global x,y, wins
    st = format(seg)
    if timer.is_running():
        if st[4:6] == ".0":
            x += 1
        y += 1
    timer.stop()
    wins = str(x) + "/" + str(y)

def reset_btn_hanlder():
    global seg,x,y,wins
    seg = 0
    x = 0
    y = 0
    wins = str(x) + "/" + str(y)
    if timer.is_running():
        timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global seg
    seg += 1


# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(seg), position, 50, "Blue")
    canvas.draw_text(wins,[300,50],50, "Purple")

# create frame
frame = simplegui.create_frame("Stopwatch", width, height)

# register event handlers
frame.add_button("Start", start_btn_hanlder,100)
frame.add_button("Stop", stop_btn_hanlder,100)
frame.add_button("Reset", reset_btn_hanlder,100)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
