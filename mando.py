import numpy as np
import collections
# l=np.chararray([['!','@','#','$'],['!','@','#','$']])
# print(l)
# #l=['!','@','#','$']
# # print("No = "+ str(l.('$')) )  
import os
from character import Person

class Mando(Person):

    def __init__(self,y_cor,x_cor,dir):
        Person.__init__(self,y_cor,x_cor,dir)
        self.shape=[ [ "/" , "0" , "\\"  ], [ " " , "|" ," "], [ "/" , "|", "\\" ]]
        self.coins=0
        self.shield=0

    def move(self,dx,dy,board_obj):
        empty=np.ndarray([3,3],dtype='U1')
        empty.fill(' ')
        if self.y_cor+dy<0 or self.y_cor+dy+3>30 :
            dy=0
        if self.x_cor+dx<board_obj.strt_col :
            self.x_cor=board_obj.strt_col
        if self.x_cor+dx+3>board_obj.end_col :
            dx=0

        check=board_obj.matrix[self.y_cor+dy:self.y_cor+dy+3,self.x_cor+dx:self.x_cor+dx+3]
        # print(check)
        if  np.array_equal(check,empty) is False :
            check1=check.tolist()
            if (sum(i.count('O') for i in check1) + sum(i.count('*') for i in check1)) > 0 :
                self.lives-=1
                board_obj.matrix[self.y_cor:self.y_cor+3,self.x_cor:self.x_cor+3]=empty
                self.x_cor=board_obj.strt_col+5
                self.y_cor=1
                dx=dy=0
                if self.lives is 0:
                    self.die=True
            if sum(i.count('$') for i in check1) > 0:
                self.coins+=sum(i.count('$') for i in check1)
        board_obj.matrix[self.y_cor:self.y_cor+3,self.x_cor:self.x_cor+3]=empty
        self.y_cor+=dy
        self.x_cor+=dx
        board_obj.matrix[self.y_cor:self.y_cor+3,self.x_cor:self.x_cor+3]=self.shape


    def check_collision(self):
        pass

    def print_mando(self):  
        pass  
        # for i in range(3):
        #     for j in range(3):
        #         print(self.shape[i][j],end='')
        #     print();
        # print(self.shape[:3,:3])
    
# if __name__ == "__main__":
#     m= Mando(14,1,1)
#     m.print_mando()