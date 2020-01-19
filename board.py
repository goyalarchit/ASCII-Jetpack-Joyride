import os
from PIL import Image, ImageDraw, ImageFont
from colorama import Fore, Back , Style

import numpy as np
class Board:

    def __init__(self,row,col,frame_size):
        self.row=row
        self.col=col
        self.strt_col=0
        self.end_col=frame_size
        self.matrix=np.ndarray((row,col),dtype='U1')
        self.frame_size=frame_size
    
    def create_board(self):
        # for i in range(self.row):
        #     self.element = []
        #     for j in range(self.col):
        #         self.element.append(" ")
        #     self.matrix.append(self.element)
        # self.grid=np.chararray(self.matrix.shape)
        self.matrix.fill(' ')

    
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


    def spawn_mando(self,player):#
        self.matrix[player.y_cor:player.y_cor+3,player.x_cor:player.x_cor+3]=player.shape


#jump higher



if __name__ == "__main__":
    Board = Board(30,160,160)
    Board.create_board()
    #Board.print_grid()
    # Board.spawn_mando()
    Board.print_grid()