import os

dir_fd = os.open('./datos.txt', os.O_RDONLY)

def opener(path, flags):
    return os.open(path, flags, dir_fd=dir_fd)

with open('datos.txt','w',opener=opener) as f:
    print('./datos.txt',file = f) 

os.close(dir_fd)