# import os
# import numpy as np
# import random
# import time
# from ASCIIArt import TextASCII_to_ndarray

# class Stat_objs:
#     # def __init__(self,row,col):
#     #     self.row=row
#     #     self.col=col
#     #     self.matrix

#     def put_firebeams(self):
#         self.__shape=[  [   [ "O", " " , " " , " ", " "  ], 
#                             [ " ", "*" , " " , " ", " "  ],
#                             [ " ", " " , "*" , " ", " "  ],
#                             [ " ", " " , " " , "*", " "  ],
#                             [ " ", " " , " " , " ", "O"  ]],
#                         [   [ " ", " " , " " , " ", "O"  ], 
#                             [ " ", " " , " " , "*", " "  ],
#                             [ " ", " " , "*" , " ", " "  ],
#                             [ " ", "*" , " " , " ", " "  ],
#                             [ "O", " " , " " , " ", " "  ]],
#                         [   [ " ", " " , "O" , " ", " "  ], 
#                             [ " ", " " , "*" , " ", " "  ],
#                             [ " ", " " , "*" , " ", " "  ],
#                             [ " ", " " , "*" , " ", " "  ],
#                             [ " ", " " , "O" , " ", " "  ]],
#                         [   [ " ", " " , " " , " ", " "  ], 
#                             [ " ", " " , " " , " ", " "  ],
#                             [ "O", "*" , "*" , "*", "O"  ],
#                             [ " ", " " , " " , " ", " "  ],
#                             [ " ", " " , " " , " ", " "  ]],
#                         [   [ "O", "*" , "*" , "*", "O"  ],
#                             [ " ", " " , " " , " ", " "  ], 
#                             [ " ", " " , " " , " ", " "  ],
#                             [ " ", " " , " " , " ", " "  ],
#                             [ "O", "*" , "*" , "*", "O"  ]],
#                     ]
#         self._shape_np=np.asarray(self.__shape,dtype= 'U1',)
#         # print(self._shape_np.shape)
#         # print()
#         random.seed(time.time())
#         return self._shape_np[random.randint(0,106)%self._shape_np.shape[0]]
        


#     def put_coins(self):
        
#         k=random.randint(1,5)
#         chars=TextASCII_to_ndarray('./coin'+str(k)+'.txt')
#         # print(chars)
#         # strings = chars.view('U' + str(chars.shape[1])).flatten()
#         # print( "\n".join(strings))
#         return chars

# if __name__ == "__main__":
#     s= Stat_objs()
#     s.put_coins()
#     print(s.put_firebeams())