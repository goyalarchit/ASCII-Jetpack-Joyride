from character import Person
from ASCIIArt import TextASCII_to_ndarray
import numpy as np
import time

class BossEnemy(Person):
    def __init__(self,y_cor,x_cor):
        shape=TextASCII_to_ndarray("boss enemy.txt")
        super().__init__(y_cor,x_cor,shape)
        self.cnt = 0
    
    def set_ycor(self,y):
        self._y_cor=y

    def simulate_fight(self,player,board_obj):
        if(board_obj.end_col<=self.get_xcor()):
            return
        if self._lives>0:
            self.cnt+=1
            shape=self.get_shape()
            empty=np.ndarray((board_obj.row,shape.shape[1]),dtype='U50')
            empty.fill(' ')
            print(empty.shape)
            x_cor=self.get_xcor()
            y_cor=self.get_ycor()
            board_obj.matrix[:,x_cor:x_cor+shape.shape[1]]=empty
            new_y=int(player.get_ycor()/2)+2
            print(shape.shape)
            print(x_cor,y_cor)
            self.set_ycor(new_y)
            print(self._y_cor)
            y_cor=self._y_cor
            board_obj.matrix[y_cor:y_cor+shape.shape[0],x_cor:x_cor+shape.shape[1]]=shape
            if self.cnt%10==0:
                board_obj.add_iceball_to_arena(y_cor+6,x_cor+5)
