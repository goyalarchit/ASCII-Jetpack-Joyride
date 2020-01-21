import os
import numpy as np
import random
from PIL import Image, ImageDraw, ImageFont
import time

class Stat_objs:
    # def __init__(self,row,col):
    #     self.row=row
    #     self.col=col
    #     self.matrix

    def put_firebeams(self):
        self.__shape=[  [   [ "O", " " , " " , " ", " "  ], 
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
        self._shape_np=np.asarray(self.__shape,dtype= 'U1',)
        # print(self._shape_np.shape)
        # print()
        random.seed(time.time())
        return self._shape_np[random.randint(0,106)%self._shape_np.shape[0]]
        


    def put_coins(self):
        
        texts=[["? ", " AG "," << "," $ ","GO" ," + ",],
                ["ARCHIT","GOOD", "YEAH"]]
        text=np.array(texts[0])
        k=random.randint(0,text.size-1)
        # print(text.size)
        myfont = ImageFont.truetype("./fonts/arial.ttf", 8)
        size = myfont.getsize(text[k])
        img = Image.new("1",size,"black")
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), text[k], "white", font=myfont)
        pixels = np.array(img, dtype=np.uint8)
        chars = np.array([' ','$'], dtype="U1")[pixels]
        # print(chars)
        # strings = chars.view('U' + str(chars.shape[1])).flatten()
        # print( "\n".join(strings))
        return chars

if __name__ == "__main__":
    s= Stat_objs()
    s.put_coins()
    print(s.put_firebeams())