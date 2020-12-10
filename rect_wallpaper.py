import ctypes
import win32api,win32con
from PIL import Image
from PIL import ImageDraw
import os
import random

def Rand_color():
    """随机一些好看的颜色
    """
    N = 12
    Color = [None]*N
    Color[0] = (189, 167, 146)
    Color[1] = (196, 86, 85)
    Color[2] = (174, 94, 83)
    Color[3] = (170, 177, 144)
    Color[4] = (207, 133, 60)
    Color[5] = (127, 156, 186)
    Color[6] = (161, 175, 201)
    Color[7] = (236, 247, 241)
    Color[8] = (242, 249, 242)
    Color[9] = (197, 215, 215)
    Color[10] = (40, 44, 52)
    Color[11] = (77, 114, 184)

    num = random.randint(0,N-1)
    return Color[num]

def Get_size():
    """获取当前显示器分辨率
    """
    size = [0,0]
    size[0] = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    size[1] = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    return size

def Gen_wallpaper(size, folderpath):
    """
    """
    img = Image.new(size=size, mode='RGB', color='white')   # 设置图片大小和图片模式
    a = ImageDraw.ImageDraw(img)

    A1 = Rand_color()
    A2 = Rand_color()
    A3 = A1
    A4 = A2

    a.rectangle((0,0,size[0]/2,size[1]/2),fill=A1)
    a.rectangle((size[0]/2,0,size[0],size[1]/2),fill=A2)
    a.rectangle((0,size[1]/2,size[0]/2,size[1]),fill=A3)
    a.rectangle((size[0]/2,size[1]/2,size[0],size[1]),fill=A4)
    
    imagepath = folderpath + '\\wallpaper.bmp'
    img.save(imagepath)
    return imagepath

def set_wallpaper(imagepath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, imagepath, 0)
    return None

def makedir():
    """创建目录
    """
    StoreFolder = os.getcwd()
    folderpath = StoreFolder + "\\Pictures\\"
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    return folderpath

if __name__ == '__main__':
    folderpath = makedir()
    size = Get_size()
    imagePath = Gen_wallpaper(size, folderpath)
    set_wallpaper(imagePath)

