import numpy as np

def TextASCII_to_ndarray(filename):
    chararray=[]
    with open(filename) as obj:
        for text in obj:
            line=text.strip('\n')
            chararray.append(list(line))
    max_len = np.array([len(array) for array in chararray]).max()
    default_value=' '
    b= [np.pad(array, (0, max_len - len(array)), mode='constant', constant_values=default_value) for array in chararray]
    bossenemy=np.asarray(b,dtype='U1')
    return bossenemy
    