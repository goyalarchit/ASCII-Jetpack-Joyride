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
from enemy import BossEnemy
from yoda import Yoda


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
        b.add_bullet_to_arena(player.get_ycor()+1,player.get_xcor()+1)
    if char == ' ':
        player.try_sheild()
    if char == '\0':
        return
    # print(char)
    # time.sleep(1)
    Bossenemy.simulate_fight(player,b)
    player.move(dx,dy,b)
    # return {'dx':dx,'dy':dy}





random.seed(time.time)
b=Board(31,200,134)
b.create_board()
# b.add_magnet_to_arena(2,770)
create_arena(b)
player=Mando(0,2)
b.spawn_mando(player)
Bossenemy = BossEnemy(0,b.col-51)
b.spwan_boss_enemy_to_arena(Bossenemy)
Baby_yoda=Yoda(b.row-5,b.col-11)
b.spwan_captured_baby_yoda_to_arena(Baby_yoda)
vel_x=1
while True :
    os.system('clear')
    print(Back.BLACK+"Coins : "+str(player.get_coins()))
    print(Back.BLACK+"Your Lives : "+str(player.get_lives()))
    print(Back.BLACK+"Boss Enemy Lives : "+str(Bossenemy.get_lives()))
    b.print_grid()
    sys.stdout.flush()
    signal.alarm(TIMEOUT)
    gameplay()
    b.simulate_bullet_motion(Bossenemy)
    b.simulate_iceball_motion()
    b.magnet_action(player)
    signal.alarm(0)
    if(b.end_col==b.col):
        vel_x=0
    player.move(vel_x,1,b)
    if Bossenemy.is_dead() is True:
        print('You Won')
        exit()
    elif player.is_dead() is True:
        print('You Lose')
        exit()
    time.sleep(1/30)
    