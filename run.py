''' main game loop
create the board
spwan mario
put obstacles
    generate some k%max obstacles per screen
    check if the sub matrix size required by the obstacle is free by slicing
    put the obstacle
put coins
    generate som no of coins k where k=random%max coin in a frame
    while(k>0)
        put coin on a random free slot
        k--;
put powerups
print grids
check collision
if mando.die>0
loop again'''



import os
from board import Board
from static_objects import Stat_objs
from background import create_arena
import time
import sys
import random
from mando import Mando
import signal
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from colorama import Fore,Back


TIMEOUT = 1
def noinput(signum,frame):
    # print("No Input")
    raise AlarmException

# class _GetchUnix:
#     def __init__(self):
#         import tty, sys

#     def __call__(self):
#         import sys, tty, termios
#         fd = sys.stdin.fileno()
#         old_settings = termios.tcgetattr(fd)
#         signal.signal(signal.SIGALRM,noinput)
#         signal.setitimer(signal.ITIMER_REAL,1)
#         try:
#             tty.setraw(sys.stdin.fileno())
#             ch = sys.stdin.read(1)
#             signal.alarm(0)
#             return ch
#         except:
#             raise noinput(signal.SIGALRM,signal.SIG_IGN)
#         finally:
#             termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#         return '\0'

def user_input(timeout=0.15):
    signal.signal(signal.SIGALRM,noinput)
    signal.setitimer(signal.ITIMER_REAL,timeout)
    try:
        text=getChar()()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM,signal.SIG_IGN)
    return ''




def gameplay():
    
    char=user_input()
    dx=0
    dy=0
    if char == 'd':
        dx=3
        dy=0
    if char == 'a':
        dx=-2
        dy=0
    if char == 'w':
        dx=0
        dy=-4
    if char == 'b':
        b.add_bullet_to_arena(player.y_cor+1,player.x_cor+1)
    if char == '\0':
        return
    # print(char)
    # time.sleep(1)
    player.move(dx,dy,b)
    # return {'dx':dx,'dy':dy}





random.seed(time.time)
b=Board(31,1000,134)
b.create_board()
b.add_magnet_to_arena(2,170)
create_arena(b)
player=Mando(0,2,1)
b.spawn_mando(player)

while True and (player.die is False) is True:
    os.system('clear')
    print(Back.BLACK+"Coins : "+str(player.coins))
    print(Back.BLACK+"Lives : "+str(player.lives))
    print(Back.BLACK+"lives : "+str(player.lives))
    b.print_grid()
    sys.stdout.flush()
    signal.alarm(TIMEOUT)
    gameplay()
    b.simulate_bullet_motion()
    b.magnet_action(player)
    signal.alarm(0)
    player.move(0,1,b)
    # time.sleep(1/1000)
    