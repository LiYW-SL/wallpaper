import requests
import random
import os
import ctypes

def set_wallpaper(imagepath):
    """设置壁纸
    """
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

def get_infinity_photo(folderpath):
    """随机下载壁纸
    """
    num = random.randint(1,4000)
    imagepath = folderpath + str(num) + '.jpg'
    
    # 判断文件是否存在，若不存在，则开始下载
    if not os.path.exists(imagepath):
        url = 'https://wallpaper.infinitynewtab.com/wallpaper/' + str(num) + '.jpg'
        response = requests.get(url)
        img = response.content
        with open(imagepath,'wb' ) as f:
            f.write(img)
    return imagepath

if __name__ == '__main__':
    folderpath = makedir()
    imagepath = get_infinity_photo(folderpath)
    set_wallpaper(imagepath)