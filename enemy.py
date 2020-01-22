from character import Person
from ASCIIArt import TextASCII_to_ndarray
import numpy as np

class BossEnemy(Person):
    def __init__(self,y_cor,x_cor):
        shape=TextASCII_to_ndarray("boss enemy.txt")
        super().__init__(y_cor,x_cor,shape)
        

    def simulate_fight(self,player,board_obj):
        if(board_obj.end_col<=self.get_xcor()):
            return
        if self._lives>0:
            shape=self.get_shape()
            empty=np.ndarray((board_obj.row,shape.shape[1]),dtype='U50')
            empty.fill(' ')
            print(empty.shape)
            x_cor=self.get_xcor()
            y_cor=self.get_ycor()
            board_obj.matrix[:,x_cor:x_cor+shape.shape[1]]=empty
            dy=player.get_ycor()-y_cor+3
            print(shape.shape)
            print(x_cor,y_cor)
            
            if y_cor+dy>board_obj.row-shape.shape[0]:
                dy-=shape.shape[0]
            elif y_cor+dy<0:
                dy-=y_cor
            
            self.set_ycor(dy)
            print(self._y_cor)
            board_obj.matrix[y_cor:y_cor+shape.shape[0],x_cor:x_cor+shape.shape[1]]=shape
