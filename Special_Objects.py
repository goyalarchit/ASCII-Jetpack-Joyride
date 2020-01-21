import os
import numpy as np
import random
from PIL import Image, ImageDraw, ImageFont
import time

class Spec_objs:
    def __init__(self,row,col,shape):
        self._row=row
        self._col=col
        self._shape=shape
    def get_shape(self):
        return self._shape

    def get_row(self):
        return self._row
    
    def get_col(self):
        return self._col


class Bullet(Spec_objs):
    def __init__(self,row,col):
        shape=u'\U00002022'
        super().__init__(row,col,shape)
        self.__cncld_obj=' '
    
    def move(self,vel):
        self._col+=vel
    
    def set_conc_obj(self,a):
        self.__cncld_obj=a

    def get_conc_obj(self):
        return self.__cncld_obj


