import os
from colorama import Fore, Back , Style
import config
import numpy as np
from Special_Objects import Bullet,Magnet,IceBall,SpeedBoost,Coins,Firebeam,Cloud
class Board:

    def __init__(self,row,col,frame_size):
        self.__row=row
        self.__col=col
        self.__strt_col=0
        self.__end_col=frame_size
        self.matrix=np.ndarray((row,col),dtype='U50')
        self.__frame_size=frame_size
        self.__objectmatrix=np.ndarray((row,col),dtype='U10')
        self.__bullets=[]
        self.__magnets=[]
        self.__ice_balls=[]
        self.__coins=[]
        self.__firebeams=[]
        self.__clouds=[]
        self.__speedboosts=[]
    
    def get_frame_size(self):
        return self.__frame_size

    def get_board_row_size(self):
        return self.__row    

    def get_board_col_size(self):
        return self.__col

    def get_board_strt_col(self):
        return self.__strt_col 

    def get_board_end_col(self):
        return self.__end_col 


    def create_board(self):
        self.matrix.fill(' ')
        self.__objectmatrix.fill('0,0')
        # print(self.__objectmatrix)

    
    def print_grid(self,speedboost):
        for i in range(self.__row):
            for j in range(self.__strt_col,self.__end_col):
                if i<self.__row-2:
                    if self.matrix[i][j]=='$':
                        os.write(1,str.encode(Back.LIGHTBLUE_EX+Fore.LIGHTYELLOW_EX+self.matrix[i][j]+Back.BLACK+Fore.RESET))
                    elif (self.matrix[i][j]=='*' or self.matrix[i][j]=='O') and j < self.__col-self.__frame_size:
                        os.write(1,str.encode(Back.LIGHTBLUE_EX+Fore.RED+self.matrix[i][j]+Back.BLACK+Fore.RESET))
                    elif self.matrix[i][j]=='N':
                        os.write(1,str.encode(Back.LIGHTBLUE_EX+Fore.RED+self.matrix[i][j]+Back.BLACK+Fore.RESET))
                    elif self.matrix[i][j]=='S':
                        os.write(1,str.encode(Back.LIGHTBLUE_EX+Fore.BLUE+self.matrix[i][j]+Back.BLACK+Fore.RESET))
                    elif self.matrix[i][j]=='#':
                        os.write(1,str.encode(Back.LIGHTBLUE_EX+Fore.BLACK+self.matrix[i][j]+Back.BLACK+Fore.RESET))
                    else:
                        os.write(1,str.encode(Back.LIGHTBLUE_EX+self.matrix[i][j]+Back.BLACK))
                else:
                    os.write(1,str.encode(Back.LIGHTGREEN_EX+self.matrix[i][j]+Back.BLACK))
            os.write(1,str.encode('\n'))
        if self.__end_col<=self.__col-1 :
            self.__strt_col+=1+speedboost
            self.__end_col+=1+speedboost
        # print(self.matrix)

    def set_objmatrix(self,s_row,s_col,shape):
        self.__objectmatrix[s_row:s_row+shape[0],s_col:s_col+shape[1]]=str(s_row)+','+str(s_col)
    
    def get_objmatrix(self,row,col):
        return self.__objectmatrix[row,col].split(',')
    
    def spawn_mando(self,player):#
        self.matrix[player.get_ycor():player.get_ycor()+3,player.get_xcor():player.get_xcor()+3]=player.get_shape()


#jump higher
    def add_bullet_to_arena(self,row,col):
        self.__bullets.append(Bullet(row,col))


    def simulate_bullet_motion(self,bossenemy):
         
        empty=np.ndarray([5,5],dtype='U50')
        empty.fill(' ')
        BULLET_VEL_X=2
        for bullet in self.__bullets:
            old_row=bullet.get_row()
            old_col=bullet.get_col()
            self.matrix[old_row,old_col]=' '
            if (old_col>=self.__end_col-4) or (old_col>=self.__col-30):
                self.matrix[old_row,old_col]=' '                
                bul_del=bullet
                self.__bullets.remove(bullet)
                del bul_del
            else:
                for x in range(1,BULLET_VEL_X+1):
                    if self.matrix[old_row,old_col+x ] in ['O','*'] :
                        col_cell=self.get_objmatrix(old_row,old_col+x)
                        self.matrix[int(col_cell[0]):int(col_cell[0])+5,int(col_cell[1]):int(col_cell[1])+5] = empty
                        bul_del=bullet
                        self.__bullets.remove(bullet)
                        del bul_del
                        break
                    elif self.matrix[old_row,old_col+x ] in ['l','<','(','@','\''] :
                        bossenemy.dec_lives()
                        if bossenemy.get_lives()==0:
                            bossenemy.died()
                        bul_del=bullet
                        self.__bullets.remove(bullet)
                        del bul_del
                        break
                else:
                    self.matrix[old_row,old_col]=bullet.get_conc_obj()
                    bullet.set_conc_obj(self.matrix[old_row,old_col+BULLET_VEL_X])
                    self.matrix[old_row,old_col+BULLET_VEL_X]=bullet.get_shape()
                    bullet.move(BULLET_VEL_X)

                        

        ###for bullet in self.__bullets
        #check collision
        #if found remove buttet
        #else move bullet forward
    
    def add_magnet_to_arena(self,row,col):
        self.__magnets.append(Magnet(row,col))
        shape=self.__magnets[int(self.__magnets.__len__())-1].get_shape()
        self.matrix[row:row+shape.shape[0],col:col+shape.shape[1]]=shape

    def magnet_action(self,player):
        for magnet in self.__magnets:
            fig=magnet.get_shape()
            mag_row=magnet.get_row()
            mag_col=magnet.get_col()
            self.matrix[mag_row:mag_row+fig.shape[0],mag_col:mag_col+fig.shape[1]]=fig
            if (magnet.get_col()>=self.__strt_col) and (magnet.get_col()<=self.__end_col):
                dx=int((magnet.get_col()-player.get_xcor())/4)
                player.move(dx,0,self)
            else:
                pass

    def spwan_boss_enemy_to_arena(self,bossenemy):
        shape=bossenemy.get_shape()
        self.matrix[bossenemy.get_ycor():bossenemy.get_ycor()+shape.shape[0],bossenemy.get_xcor():bossenemy.get_xcor()+shape.shape[1]]=shape

    def spwan_captured_baby_yoda_to_arena(self,baby_yoda):
        shape=baby_yoda.get_shape()
        self.matrix[baby_yoda.get_ycor():baby_yoda.get_ycor()+shape.shape[0],baby_yoda.get_xcor():baby_yoda.get_xcor()+shape.shape[1]]=shape


    def add_iceball_to_arena(self,row,col):
        self.__ice_balls.append(IceBall(row,col))


    def simulate_iceball_motion(self):
        ICEBALL_VEL_X=-3
        for iceball in self.__ice_balls:
            old_row=iceball.get_row()
            old_col=iceball.get_col()
            shape=iceball.get_shape()
            empty=np.ndarray(shape.shape,dtype='U50')
            empty.fill(' ')
            self.matrix[old_row:old_row+shape.shape[0],old_col:old_col+shape.shape[1]]=empty
            if (old_col<self.__strt_col) or (old_col>=self.__col-10):
                iceball_del=iceball
                self.__ice_balls.remove(iceball)
                del iceball_del
            else:
                self.matrix[old_row:old_row+shape.shape[0],old_col:old_col+shape.shape[1]]=iceball.get_conc_obj()
                iceball.set_conc_obj(self.matrix[old_row:old_row+shape.shape[0],old_col+ICEBALL_VEL_X:old_col+ICEBALL_VEL_X+shape.shape[1]])
                self.matrix[old_row:old_row+shape.shape[0],old_col+ICEBALL_VEL_X:old_col+ICEBALL_VEL_X+shape.shape[1]]=shape
                iceball.move(ICEBALL_VEL_X)

    def add_speedboost_to_arena(self,row,col):
        speedboost=SpeedBoost(row,col)
        self.__speedboosts.append(speedboost)
        fig=speedboost.get_shape()
        try : 
            self.set_objmatrix(row,col,fig.shape)
            self.matrix[row:row+fig.shape[0],col:col+fig.shape[1]]=fig
        except:
            return

    def add_cloud_to_arena(self,row,col):
        cloud=Cloud(row,col)
        self.__clouds.append(cloud)
        fig=cloud.get_shape()
        try : 
            self.set_objmatrix(row,col,fig.shape)
            self.matrix[row:row+fig.shape[0],col:col+fig.shape[1]]=fig
        except:
            return 
    def add_coins_to_arena(self,row,col):
        coin=Coins(row,col)
        self.__coins.append(coin)
        fig=coin.get_shape()
        empty=np.ndarray([fig.shape[0],fig.shape[1]],dtype='U50')
        empty.fill(' ')
        check = self.matrix[row:row+fig.shape[0],col:col+fig.shape[1]]
        if np.array_equal(check,empty) is False :
            return False
        try : 
            self.set_objmatrix(row,col,fig.shape)
            self.matrix[row:row+fig.shape[0],col:col+fig.shape[1]]=fig
        except:
            return True

    def add_firebeam_to_arena(self,row,col):
        firebeam=Firebeam(row,col)
        self.__firebeams.append(firebeam)
        fig=firebeam.get_shape()
        empty=np.ndarray([fig.shape[0],fig.shape[1]],dtype='U50')
        empty.fill(' ')
        check = self.matrix[row:row+fig.shape[0],col:col+fig.shape[1]]
        if np.array_equal(check,empty) is False :
            return False
        try : 
            self.set_objmatrix(row,col,fig.shape)
            self.matrix[row:row+fig.shape[0],col:col+fig.shape[1]]=fig
        except:
            return True
