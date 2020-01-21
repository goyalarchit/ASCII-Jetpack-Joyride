import os
from PIL import Image, ImageDraw, ImageFont
from colorama import Fore, Back , Style
import config
import numpy as np
from Special_Objects import Bullet,Magnet
class Board:

    def __init__(self,row,col,frame_size):
        self.row=row
        self.col=col
        self.strt_col=0
        self.end_col=frame_size
        self.matrix=np.ndarray((row,col),dtype='U50')
        self.frame_size=frame_size
        self.__objectmatrix=np.ndarray((row,col),dtype='U10')
        self.bullets=[]
        self.magnets=[]
    
    def create_board(self):
        # for i in range(self.row):
        #     self.element = []
        #     for j in range(self.col):
        #         self.element.append(" ")
        #     self.matrix.append(self.element)
        # self.grid=np.chararray(self.matrix.shape)
        self.matrix.fill(' ')
        self.__objectmatrix.fill('0,0')
        print(self.__objectmatrix)

    
    def print_grid(self):
        for i in range(self.row):
            for j in range(self.strt_col,self.end_col):
                if i<29:
                    print(Back.LIGHTBLUE_EX+self.matrix[i][j], end="")
                else:
                    print(Back.LIGHTGREEN_EX+self.matrix[i][j], end="")
            print()
        if self.end_col!=self.col :
            self.strt_col+=1
            self.end_col+=1
        # print(self.matrix)

    def set_objmatrix(self,s_row,s_col,shape):
        self.__objectmatrix[s_row:s_row+shape[0],s_col:s_col+shape[1]]=str(s_row)+','+str(s_col)
    
    def get_objmatrix(self,row,col):
        return self.__objectmatrix[row,col].split(',')
    
    def spawn_mando(self,player):#
        self.matrix[player.y_cor:player.y_cor+3,player.x_cor:player.x_cor+3]=player.shape


#jump higher
    def add_bullet_to_arena(self,row,col):
        self.bullets.append(Bullet(row,col))


    def simulate_bullet_motion(self):
         
        empty=np.ndarray([5,5],dtype='U50')
        empty.fill(' ')
        BULLET_VEL_X=2
        for bullet in self.bullets:
            old_row=bullet.get_row()
            old_col=bullet.get_col()
            self.matrix[old_row,old_col]=' '
            if (old_col>=self.end_col-1) or (old_col>=self.col-10):
                self.matrix[old_row,old_col]=' '                
                bul_del=bullet
                self.bullets.remove(bullet)
                del bul_del
            else:
                for x in range(1,BULLET_VEL_X+1):
                    if self.matrix[old_row,old_col+x ] in ['O','*'] :
                        col_cell=self.get_objmatrix(old_row,old_col+x)
                        print(col_cell)
                        self.matrix[int(col_cell[0]):int(col_cell[0])+5,int(col_cell[1]):int(col_cell[1])+5] = empty
                        bul_del=bullet
                        self.bullets.remove(bullet)
                        del bul_del
                        break
                else:
                    self.matrix[old_row,old_col]=bullet.get_conc_obj()
                    bullet.set_conc_obj(self.matrix[old_row,old_col+BULLET_VEL_X])
                    self.matrix[old_row,old_col+BULLET_VEL_X]=bullet.get_shape()
                    bullet.move(BULLET_VEL_X)

                        

        ###for bullet in self.bullets
        #check collision
        #if found remove buttet
        #else move bullet forward
    
    def add_magnet_to_arena(self,row,col):
        self.magnets.append(Magnet(row,col))
        shape=self.magnets[int(self.magnets.__len__())-1].get_shape()
        self.matrix[row:row+shape.shape[0],col:col+shape.shape[1]]=shape

    def magnet_action(self,player):
        for magnet in self.magnets:
            if (magnet.get_col()>=self.strt_col) and (magnet.get_col()<=self.end_col):
                dx=int((magnet.get_col()-player.x_cor)/4)
                player.move(dx,0,self)
            else:
                pass

if __name__ == "__main__":
    Board = Board(30,160,160)
    Board.create_board()
    #Board.print_grid()
    # Board.spawn_mando()
    Board.print_grid()