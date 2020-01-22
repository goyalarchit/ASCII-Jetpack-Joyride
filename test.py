import numpy as np
import time
import os
a=np.ndarray([25,2000],dtype='U50')
# a.fill('\033[31;1;42mS')
a[0:20,:2000]='\033[44mS\033[0m'
a[20:25,:2000]='\033[42mS\033[0m'
def printit():
    s=0
    e=114;
    for i in range(25):
        for j in range(s,e):
            print(a[i][j],end='')
        print()
        if e<2000:
            s+=1;
            e+=1

# while True:
    
#     os.system('clear')
#     printit()
#     time.sleep(1/24)
    

# s='12,0'
# s2=s.split(',')
# print(s2)
# s3=str(s2[0]+','+s2[1])
# print(s3)
# s1=u'\033[44mS'
# s2=u'\033[44mS'
# print(s1,s2)
# if s1==s2:
#     print("Can Do It")
# else:
#     print("Cant Do It")

'''
for gravity
mario
-velocity y=0
if w is press set v_y=0 and on other cases
'''


'''
empty=np.ndarray([5,5],dtype='U50')
        empty.fill(' ')
        BULLET_VEL_X=5
        for bullet in self.bullets:
            old_row=bullet.get_row()
            old_col=bullet.get_col()
            if old_col>=self.end_col-1:
                self.matrix[old_row,old_col]=' '
                bul_del=bullet
                self.bullets.remove(bullet)
                del bul_del
            else:
                for x in range(1,BULLET_VEL_X+1):
                    if self.matrix[old_row,old_col+x] in ['O','*']:
                        col_cell=self.get_objmatrix(old_row,old_col)
                        print(col_cell)
                        self.matrix[int(col_cell[0]):int(col_cell[0])+5,int(col_cell[1]):int(col_cell[1])+5] = empty
                        bul_del=bullet
                        self.bullets.remove(bullet)
                        del bul_del
                        break;
                else:   
                    old_col=bullet.get_col()
                    self.matrix[old_row,old_col]=' '
                    if self.matrix[old_row,old_col+BULLET_VEL_X]==' ':
                        self.matrix[old_row,old_col+BULLET_VEL_X]=bullet.get_shape()
                        bullet.set_col(old_col+BULLET_VEL_X)
                    else :
                        bullet.set_col(old_col+BULLET_VEL_X)
'''

# cnt=0
# chararray=[]
# with open("./boss enemy") as obj:
#     for text in obj:
#         cnt+=1
#         line=text.strip('\n')
#         print(list(line))
#         chararray.append(list(line))
# print(chararray)
# max_len = np.array([len(array) for array in chararray]).max()
# print(max_len)
# default_value=' '
# b= [np.pad(array, (0, max_len - len(array)), mode='constant', constant_values=default_value) for array in chararray]
# bossenemy=np.asarray(b,dtype='U1')
# print(bossenemy.shape)
# for a in bossenemy:
#     for b in a:
#         print(b,end='')
#     print()

dic =time.time()
print(dic)
# print(str1)