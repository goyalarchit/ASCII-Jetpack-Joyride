from character import Person
from ASCIIArt import TextASCII_to_ndarray

class Yoda(Person):
    def __init__(self,y_cor,x_cor):
        shape=TextASCII_to_ndarray("./ASCII_ART/baby-yoda.txt")
        super().__init__(y_cor,x_cor,shape)