import os
import numpy as np
import random
# from static_objects import Stat_objs
from Special_Objects import Cloud
# from board import Board


def create_arena(board_obj):
    board_obj.add_magnet_to_arena(6,int(2*board_obj.col/3))
    board_obj.add_speedboost_to_arena(18,int(board_obj.col/3))
    s_col=0
    while s_col<board_obj.col-70:
        board_obj.add_cloud_to_arena(int(0),s_col)
        s_col+=30
    row=[6,15,24]
    for i in range(3):
        s_col=0
        while s_col<board_obj.col-board_obj.frame_size-20:
            s_row=row[i] + random.randint(0,2)
            s_col+=random.randint(0,100)%30
            if random.randint(0,13)%2 == 0 :
                t=board_obj.add_coins_to_arena(s_row,s_col)                
            else :
                t=board_obj.add_firebeam_to_arena(s_row,s_col)
            if t is False :
                continue
            s_col+=25
        i+=1