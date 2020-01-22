import os

class Person:
    def __init__(self,y_cor,x_cor,shape):
        self._x_cor=x_cor
        self._y_cor=y_cor
        self._lives=5
        self._die=False
        self._shape=shape
    
    def get_shape(self):
        return self._shape

    def get_xcor(self):
        return self._x_cor
    
    def get_ycor(self):
        return self._y_cor

    def get_lives(self):
        return self._lives

    def is_dead(self):
        return self._die

    def died(self):
        self._die=True

    def dec_lives(self):
        self._lives-=1

    def set_ycor(self,dy):
        self._y_cor+=dy

    def set_xcor(self,dx):
        self._x_cor+=dx
        