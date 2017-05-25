#coding=utf-8

import os,shutil,hashlib

#比较图片
def compareImageFileWithPath(oldPath,newPath,desPath,childFloderName):
    oldEntirePath = os.path.join(oldPath,childFloderName)
    newEntirePath = os.path.join(newPath,childFloderName)
    desEntirePath = os.path.join(desPath,childFloderName)
    if not os.path.isdir(newEntirePath): # not os.path.isdir(oldEntirePath) or
        return
    #创建目标目录
    os.system('rm -rf ' + desEntirePath)
    os.system('mkdir -p ' + desEntirePath)
    for imgFileName in os.listdir(newEntirePath):
        if imgFileName == '.DS_Store':
            continue
        newImgFilePath = os.path.join(newEntirePath,imgFileName)
        oldImgFilePath = os.path.join(oldEntirePath,imgFileName)
        desImgFilePath = os.path.join(desEntirePath,imgFileName)
        if os.path.isdir(newImgFilePath) and os.path.isdir(oldImgFilePath):
            #子目录
            compareImageFileWithPath(oldEntirePath,newEntirePath,desEntirePath,imgFileName)
        elif os.path.isfile(newImgFilePath) :
            if os.path.isfile(oldImgFilePath):
                newImgFile = open(newImgFilePath)
                newImgString = newImgFile.read()
                oldImgFile = open(oldImgFilePath)
                oldImgString = oldImgFile.read()

                # md5方式比较图片是否一致
                newFileMD5 = hashlib.md5()
                oldFileMD5 = hashlib.md5()
                newFileMD5.update(newImgString)
                newImgMD5String = newFileMD5.hexdigest()
                oldFileMD5.update(oldImgString)
                oldImgMD5String = oldFileMD5.hexdigest()
                if newImgMD5String != oldImgMD5String:
                    # 移动新文件
                    os.system('cp ' + newImgFilePath + ' ' + desImgFilePath)
                newImgFile.close()
                oldImgFile.close()
            else:
                # 移动新文件
                os.system('cp ' + newImgFilePath + ' ' + desImgFilePath)