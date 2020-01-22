import numpy as np
import collections 
import os
from character import Person
import time

class Mando(Person):

    def __init__(self,y_cor,x_cor):
        shape=[  [ [ "/" , "0" , "\\"  ], [ " " , "|" ," "], [ "/" , "|", "\\" ]],
                        [ [ "\033[45m/\033[0m" , "\033[45m0\033[0m" , "\033[45m\\\033[0m"  ],
                         [ "\033[45m \033[0m" , "\033[45m|\033[0m" ,"\033[45m \033[0m"], 
                         [ "\033[45m/\033[0m" , "\033[45m|\033[0m", "\033[45m\\\033[0m" ]]]
        Person.__init__(self,y_cor,x_cor,shape)
        self.__coins=0
        self.__shield_available=1
        self.__shield_active=0
        self.__last_used_time=time.time()
        self.__shield_strt_time=0
        empty=np.ndarray((3,3),dtype='U50')
        empty.fill(' ')
        self.__cncld_obj=empty
        self.__speedboost=0
        self.__speedboost_st=0
        self.__vel_y=0


    def get_coins(self):
        return self.__coins

    def set_conc_obj(self,a):
        self.__cncld_obj=a

    def get_conc_obj(self):
        return self.__cncld_obj

    def set_vel_y(self,a):
        if a==0:
            self.__vel_y=a
        else:
            self.__vel_y+=a

    def get_vel_y(self):
        return self.__vel_y

    def inc_coins(self,collected):
        self.__coins+=collected

    def get_shape(self):
        return self._shape[self.__shield_active]

    def get_speedboost(self):
        return self.__speedboost

    def move(self,dx,dy,board_obj):
        if self.__speedboost!=0:
            if time.time() - self.__speedboost_st > 10:
                self.__speedboost=0
        empty=np.ndarray([3,3],dtype='U50')
        empty.fill(' ')
        x_cor=self.get_xcor()
        y_cor=self.get_ycor()
        if y_cor+dy<4 or y_cor+dy+3>board_obj.row-2 :
            dy=0
        if x_cor+dx<board_obj.strt_col :
            self.set_xcor(board_obj.strt_col-x_cor)
        if x_cor+dx+3>board_obj.end_col :
            dx=0
        self.shield_book_keeping()
        if self.check_collision(dx,dy,board_obj) is False:
            board_obj.matrix[self.get_ycor():self.get_ycor()+3,self.get_xcor():self.get_xcor()+3]=empty
            self.set_ycor(dy)
            self.set_xcor(dx)
        board_obj.matrix[self.get_ycor():self.get_ycor()+3,self.get_xcor():self.get_xcor()+3]=self.get_shape()


    def check_collision(self,dx,dy,board_obj):
        empty=np.ndarray([3,3],dtype='U50')
        empty.fill(' ')
        flag=False
        y_cor=self.get_ycor()
        x_cor=self.get_xcor()
        if dx!=0:
            for x in range(1,dx+1):
                check=board_obj.matrix[y_cor+dy:y_cor+dy+3,x_cor+x:x_cor+x+3]
                if  np.array_equal(check,empty) is False :
                    check1=check.tolist()
                    if (self.__shield_active==0) and ((sum(i.count('O') for i in check1) + sum(i.count('*') for i in check1)) > 0):
                        flag=True
                        self.dec_lives()
                        board_obj.matrix[y_cor:y_cor+3,x_cor:x_cor+3]=empty
                        self.set_xcor(board_obj.strt_col+5-x_cor)
                        self.set_ycor(5-y_cor)
                        dx=dy=0
                        if self.get_lives() is 0:
                            self.died()
                    if sum(i.count('$') for i in check1) > 0:
                        self.inc_coins(sum(i.count('$') for i in check1))
                    if sum(i.count('#') for i in check1) > 0:
                        self.__speedboost=3
                        self.__speedboost_st=time.time()
                    if flag is True :
                        return True
        if dy!=0:
            for y in range(1,dy+1):
                check=board_obj.matrix[y_cor+y:y_cor+y+3,x_cor+dx:x_cor+dx+3]
                if  np.array_equal(check,empty) is False :
                    check1=check.tolist()
                    if (self.__shield_active==0) and ((sum(i.count('O') for i in check1) + sum(i.count('*') for i in check1)) > 0):
                        flag=True
                        self.dec_lives()
                        board_obj.matrix[y_cor:y_cor+3,x_cor:x_cor+3]=empty
                        self.set_xcor(board_obj.strt_col+5-x_cor)
                        self.set_ycor(5-y_cor)
                        dx=dy=0
                        if self.get_lives() is 0:
                            self.died()
                    if sum(i.count('$') for i in check1) > 0:
                        self.inc_coins(sum(i.count('$') for i in check1))
                    if sum(i.count('#') for i in check1) > 0:
                        self.__speedboost=3
                        self.__speedboost_st=time.time()
                    if flag is True:
                        return True
        return flag
        '''
        note disappearing beams can be overcome by reprinting the collided beam and removing the respawining place beam 
        '''

    def try_sheild(self):
        if self.__shield_active==1:
            return
        if self.__shield_active==0:
            if self.__shield_available==1:
                self.__shield_active=1
                self.__shield_available=0
                self.__shield_strt_time=int(time.time())
            
    def shield_book_keeping(self):
        if self.__shield_active==1:
            if (int(time.time())-self.__shield_strt_time)>10:
                self.__last_used_time=time.time()
                self.__shield_active=0
        else:
            if self.__shield_available==0:
                if int(time.time()-self.__last_used_time)>60:
                    self.__shield_available=1
            

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