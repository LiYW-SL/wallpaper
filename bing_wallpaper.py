import ctypes
import os
import json
import urllib.request

def get_bing_photo(folderpath):
    """下载bing每日壁纸
    """
    url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    res = urllib.request.urlopen(url)
    json_txt = res.read()
    txt = json.loads(json_txt)
    
    # 设置文件名以及文件路径
    name = str(txt['images'][0]['copyright']).split()[0]
    imagepath = folderpath + name + ".jpg"
    
    # 判断文件是否存在，若不存在，则开始下载
    if not os.path.exists(imagepath):
        url = 'https://www.bing.com/' + txt['images'][0]['url']
        photo = urllib.request.urlopen(url)
        d = photo.read()

        f = open(imagepath, "wb")
        f.write(d)
        f.close()
    return imagepath

def set_wallpaper(imagepath):
    """设置目录
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

if __name__ == '__main__':
    folderpath = makedir()
    imagepath = get_bing_photo(folderpath)
    set_wallpaper(imagepath)