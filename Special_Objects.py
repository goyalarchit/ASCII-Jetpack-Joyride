import os
import numpy as np
import random
import time
from ASCIIArt import TextASCII_to_ndarray



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



class Magnet(Spec_objs):
    def __init__(self,row,col):
        shape=TextASCII_to_ndarray("./magnet.txt")
        super().__init__(row,col,shape)


class Coins(Spec_objs):
    def __init__(self,row,col):
        k=random.randint(1,5)
        shape=TextASCII_to_ndarray('./coin'+str(k)+'.txt')
        super().__init__(row,col,shape)


class Firebeam(Spec_objs):
    def __init__(self,row,col):
        shape=  [     [   [ "O", " " , " " , " ", " "  ], 
                        [ " ", "*" , " " , " ", " "  ],
                        [ " ", " " , "*" , " ", " "  ],
                        [ " ", " " , " " , "*", " "  ],
                        [ " ", " " , " " , " ", "O"  ]],
                    [   [ " ", " " , " " , " ", "O"  ], 
                        [ " ", " " , " " , "*", " "  ],
                        [ " ", " " , "*" , " ", " "  ],
                        [ " ", "*" , " " , " ", " "  ],
                        [ "O", " " , " " , " ", " "  ]],
                    [   [ " ", " " , "O" , " ", " "  ], 
                        [ " ", " " , "*" , " ", " "  ],
                        [ " ", " " , "*" , " ", " "  ],
                        [ " ", " " , "*" , " ", " "  ],
                        [ " ", " " , "O" , " ", " "  ]],
                    [   [ " ", " " , " " , " ", " "  ], 
                        [ " ", " " , " " , " ", " "  ],
                        [ "O", "*" , "*" , "*", "O"  ],
                        [ " ", " " , " " , " ", " "  ],
                        [ " ", " " , " " , " ", " "  ]],
                    [   [ "O", "*" , "*" , "*", "O"  ],
                        [ " ", " " , " " , " ", " "  ], 
                        [ " ", " " , " " , " ", " "  ],
                        [ " ", " " , " " , " ", " "  ],
                        [ "O", "*" , "*" , "*", "O"  ]],
                ]
        shape_np=np.asarray(shape,dtype= 'U1',)
        random.seed(time.time())
        fin_shape=shape_np[random.randint(0,106)%shape_np.shape[0]]
        super().__init__(row,col,fin_shape)


class IceBall(Spec_objs):
    def __init__(self,row,col):
        shape=TextASCII_to_ndarray('./ice_balls.txt')
        empty=np.ndarray(shape.shape,dtype='U50')
        empty.fill(' ')
        super().__init__(row,col,shape)
        self.__cncld_obj=empty
    
    def move(self,vel):
        self._col+=vel
    
    def set_conc_obj(self,a):
        self.__cncld_obj=a

    def get_conc_obj(self):
        return self.__cncld_obj

class SpeedBoost(Spec_objs):
    def __init__(self,row,col):
        shape=TextASCII_to_ndarray('./speedboost.txt')
        empty=np.ndarray(shape.shape,dtype='U50')
        empty.fill(' ')
        super().__init__(row,col,shape)




class Cloud(Spec_objs):
    def __init__(self,row,col):
        shape=TextASCII_to_ndarray('./cloud.txt')
        empty=np.ndarray(shape.shape,dtype='U50')
        empty.fill(' ')
        super().__init__(row,col,shape)