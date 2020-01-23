from character import Person
from ASCIIArt import TextASCII_to_ndarray
import numpy as np
import time

class BossEnemy(Person):
    def __init__(self,y_cor,x_cor):
        shape=TextASCII_to_ndarray("./ASCII_ART/boss enemy.txt")
        super().__init__(y_cor,x_cor,shape)
        self.__cnt = 0
    
    def set_ycor(self,y):
        self._y_cor=y

    def simulate_fight(self,player,board_obj):
        if(int(board_obj.get_board_end_col())<=int(self.get_xcor())):
            return
        if self._lives>0:
            self.__cnt+=1
            shape=self.get_shape()
            empty=np.ndarray((int(board_obj.get_board_row_size()),shape.shape[1]),dtype='U50')
            empty.fill(' ')
            x_cor=self.get_xcor()
            y_cor=self.get_ycor()
            board_obj.matrix[:,x_cor:x_cor+shape.shape[1]]=empty
            new_y=int(player.get_ycor()/2)+5
            self.set_ycor(new_y)
            y_cor=self._y_cor
            board_obj.matrix[y_cor:y_cor+shape.shape[0],x_cor:x_cor+shape.shape[1]]=shape
            if self.__cnt%10==0:
                board_obj.add_iceball_to_arena(y_cor+6,x_cor+5)
