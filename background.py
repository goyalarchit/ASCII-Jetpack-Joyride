import os
import numpy as np
import random
from static_objects import Stat_objs
# from board import Board


def create_arena(board_obj):
    so = Stat_objs()
    # frame=board_obj.col/board_obj.frame_size
    # print(frame)
    # cur_frame=0
    s_col=0
    # while cur_frame<frame:
    #     a=random.randint(0,1000)%5
    #     b=random.randint(0,1000)%5
    #     while a>0:
    #         s_row=random.randint(0,18)
    #         s_col=random.randint(cur_frame*board_obj.frame_size,(cur_frame+1)*board_obj.frame_size,)
    #         chars=so.put_coins()
    #         board_obj.matrix[s_row:s_row+chars.shape[0],s_col:s_col+chars.shape[1]]=chars
    #         a-=1
    #     cur_frame+=1
    
    row=[0,9,18]
    for i in range(3):
        s_col=0
        while s_col<board_obj.col-100:
            if random.randint(0,13)%2 == 0 :
            # if s_col%2 == 0 :
                chars=so.put_coins()
            else :
                chars=so.put_firebeams()
            s_row=row[i] + random.randint(0,2)
            s_col+=random.randint(0,100)%30
            empty=np.ndarray([chars.shape[0],chars.shape[1]],dtype='U1')
            empty.fill(' ')
            check = board_obj.matrix[s_row:s_row+chars.shape[0],s_col:s_col+chars.shape[1]]
            if np.array_equal(check,empty) is False :
                continue
            try :
                print(chars.shape) 
                t=board_obj.set_objmatrix(s_row,s_col,chars.shape)
                # print(t)
                board_obj.matrix[s_row:s_row+chars.shape[0],s_col:s_col+chars.shape[1]]=chars

            except :    
                continue        
            s_col+=chars.shape[1]+5
        i+=1