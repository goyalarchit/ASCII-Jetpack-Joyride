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
import termios
from config import *
from ASCIIArt import TextASCII_to_ndarray


TIMEOUT = 1
def noinput(signum,frame):
    raise AlarmException


def user_input(timeout=0.05):
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
    #Forward
    if char == 'd':
        dx=3
        dy=0
    #Backward
    if char == 'a':
        dx=-2
        dy=0
    #Activate Jetpack
    if char == 'w':
        dx=0
        dy=-5
        player.set_vel_y(0)
    #Fire Bullet
    if char == 'b':
        b.add_bullet_to_arena(player.get_ycor()+1,player.get_xcor()+1)
    #Activate Shield
    if char == ' ':
        player.try_sheild()
    
    if char == '\0':
        return
    #Quit
    if char=='q':
        quit(2)
    #Pause and Resume
    if char == 'p':
        ch2='\0'
        while ch2 != 'p':
            ch2=user_input()
            continue
    Bossenemy.simulate_fight(player,b)
    player.move(dx,dy,b)
    # return {'dx':dx,'dy':dy}


def quit(code):
    files=['./ASCII_ART/youwon.txt','./ASCII_ART/youlost.txt','./ASCII_ART/youquit.txt']
    fig=TextASCII_to_ndarray(files[code])
    strt_col=b.get_board_strt_col()
    col=strt_col+20
    row=0+10
    b.matrix[row:row+fig.shape[0],col:col+fig.shape[1]]=fig
    os.system('clear')
    os.write(1,str.encode(Back.BLACK+"Coins : "+str(player.get_coins())+'\t\t\t\t\t\t\t\t\t\t\t\t\t'))
    os.write(1,str.encode(Back.BLACK+"Time : "+str(remaining_time)+'\n'))
    os.write(1,str.encode(Back.BLACK+"Your Lives : "+str(player.get_lives())+'\t\t\t\t\t\t\t\t\t\t\t\t\t'))
    os.write(1,str.encode(Back.BLACK+"Boss Enemy Lives : "+str(Bossenemy.get_lives())+'\n'))
    b.print_grid(int(player.get_speedboost()))
    termios.tcsetattr(1, termios.TCSADRAIN, oldattr)
    exit()

# Hide cursor
os.system("tput civis")
# Disable terminal echoing
oldattr = termios.tcgetattr(1)
newattr = termios.tcgetattr(1)
newattr[3] = newattr[3] & ~termios.ECHO
termios.tcsetattr(1, termios.TCSADRAIN, newattr)
os.system('clear')
fig=TextASCII_to_ndarray('./ASCII_ART/gamemenu1.txt')
casting_board=Board(fig.shape[0],fig.shape[1],FRAME_SIZE)
casting_board.matrix[:,:]=fig
casting_board.print_grid(0)
time.sleep(2)
del casting_board
os.system('clear')
random.seed(time.time)
b=Board(ROWS,COL_LENGTH,FRAME_SIZE)
b.create_board()
create_arena(b)
player=Mando(5,2)
b.spawn_mando(player)
Bossenemy = BossEnemy(0,b.get_board_col_size()-51)
b.spwan_boss_enemy_to_arena(Bossenemy)
Baby_yoda=Yoda(b.get_board_row_size()-5,b.get_board_col_size()-11)
b.spwan_captured_baby_yoda_to_arena(Baby_yoda)
vel_x=1
remaining_time=COL_LENGTH+400
strt_time=time.time()
while True :
    # os.system('clear')
    os.write(1,str.encode('\033[0;0H'))
    remaining_time-=1 #int(time.time())-int(strt_time)
    os.write(1,str.encode(Back.BLACK+"Coins : "+str(player.get_coins())+'\t\t\t\t\t\t\t\t\t\t\t\t\t'))
    os.write(1,str.encode(Back.BLACK+"Time : %4d" % (remaining_time)+'\n'))
    os.write(1,str.encode(Back.BLACK+"Your Lives : "+str(player.get_lives())+'\t\t\t\t\t\t\t\t\t\t\t\t\t'))
    os.write(1,str.encode(Back.BLACK+"Boss Enemy Lives : "+str(Bossenemy.get_lives())+'\n'))
    b.print_grid(int(player.get_speedboost()))
    os.write(1,str.encode('Press p to Pause/Resume'))
    # sys.stdout.flush()
    # signal.alarm(TIMEOUT)
    gameplay()
    b.simulate_bullet_motion(Bossenemy,int(player.get_speedboost()))
    b.simulate_iceball_motion()
    b.magnet_action(player)
    # signal.alarm(0)
    if(b.get_board_end_col()==b.get_board_col_size()):
        vel_x=0
    player.move(vel_x+int(player.get_speedboost()),int(player.get_vel_y()),b)
    if Bossenemy.is_dead() is True:
        quit(0)
    elif player.is_dead() is True or (remaining_time<=0):
        quit(1)
    player.set_vel_y(0.5)
    # time.sleep(1/24)
    
