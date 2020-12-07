import win32api,win32con,win32gui
from PIL import Image
from PIL import ImageDraw
import os
import random

#获取当前路径
StoreFolder = os.getcwd()

def Rand_color():
    """随机一些好看的颜色
    """
    Color = []
    Color.append((189, 167, 146))
    Color.append((196, 86, 85))
    Color.append((174, 94, 83))
    Color.append((170, 177, 144))
    Color.append((207, 133, 60))
    Color.append((127, 156, 186))
    Color.append((161, 175, 201))
    Color.append((236, 247, 241))
    Color.append((242, 249, 242))
    Color.append((197, 215, 215))
    Color.append((40, 44, 52))
    Color.append((77, 114, 184))
    
    N = len(Color)
    num = random.randint(0,N-1)
    return Color[num]

def Get_size():
    """获取当前显示器分辨率
    """
    size = [0,0]
    size[0] = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    size[1] = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    return size

def Gen_wallpaper(size):
    """制作壁纸
    """
    img = Image.new(size=size, mode='RGB', color='white')   # 设置图片大小和图片模式
    a = ImageDraw.ImageDraw(img)

    A1 = Rand_color()
    A2 = Rand_color()
    A3 = Rand_color()
    A4 = Rand_color()

    a.rectangle((0,0,size[0]/2,size[1]/2),fill=A1)
    a.rectangle((size[0]/2,0,size[0],size[1]/2),fill=A2)
    a.rectangle((0,size[1]/2,size[0]/2,size[1]),fill=A3)
    a.rectangle((size[0]/2,size[1]/2,size[0],size[1]),fill=A4)
    
    imagePath = StoreFolder + '\\wallpaper.bmp'
    img.save(imagePath)
    return imagePath

def setWallpaperFromBMP(imagepath):
    """设置为桌面背景
    """
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2") #2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath, 1+2)
    return None
    
if __name__ == "__main__":
    size = Get_size()
    imagePath = Gen_wallpaper(size)
    setWallpaperFromBMP(imagePath)