#coding=utf-8

from zipfile import *

# 压缩目录
def zipFloder(pathIn,zipFileName):
    orientPath = os.getcwd()
    zipPath = os.path.dirname(pathIn)
    os.chdir(zipPath)
    zipf = zipfile.ZipFile(zipFileName+'.zip', 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk('./'+zipFileName):
        for filename in filenames:
            zipf.write(os.path.join(dirpath, filename))
    zipf.close()
    os.chdir(orientPath)