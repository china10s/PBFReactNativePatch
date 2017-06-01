#coding=utf-8

import os,shutil,hashlib
from patchImageFile import *
from patchJSFile import *
from patchZip import *
from patchMD5 import *

# 拷贝全量 bundles 文件
def copyBundleZip(newBundlePath,patchesPath,plantform,version):
    patchesTmpZipPath = os.path.join(newBundlePath,plantform)
    patchesTmpZipPath+='.zip'
    patchesZipPath = os.path.join(patchesPath, version)
    patchesZipPath = os.path.join(patchesZipPath, plantform)
    patchesZipPath = os.path.join(patchesZipPath, version+'.zip')
    # 打 zip 包
    zipFloder(newBundlePath+'/',plantform)

    cpBundleString = 'mv -f ' +patchesTmpZipPath+ ' ' + patchesZipPath
    os.system(cpBundleString)
    return calculateMD5(patchesZipPath)

#比较文件
def compareWithPlatform(platformType,oldVersionIn,newVerionIn):
    oldJSFolderPath = '../bundles/'+oldVersionIn +'/'+ platformType+'/'
    newJSFolderPath = './build/'+platformType+'/'
    patchFloderFile =  oldVersionIn+'-'+newVerionIn
    patchFloderPath = '../patches/'+newVerionIn+'/'+platformType+'/'+patchFloderFile
    os.system('rm -rf '+patchFloderPath)
    os.system('mkdir -p '+patchFloderPath)
    # 比较文件
    for jsNewFile in os.listdir(newJSFolderPath):
        if jsNewFile == '.DS_Store':
            continue
        newFilePath = newJSFolderPath+jsNewFile
        oldFilePath = oldJSFolderPath + jsNewFile
        extensitionFile = os.path.splitext(newFilePath)

        if os.path.isdir(newFilePath):
            # 图片文件夹文件比较
            print '图片文件夹比较'
            compareImageFileWithPath(oldJSFolderPath,newJSFolderPath,patchFloderPath,jsNewFile)
        elif extensitionFile[1] == '.jsbundle':
            # JS文件比较
            compareJSFileWithPath(oldFilePath, newFilePath, patchFloderPath, jsNewFile)
        else:
            # 未打包文件
            print '未打包文件 ：'+jsNewFile
    # 压缩文件夹
    zipFloder(patchFloderPath, patchFloderFile)
    # 删除被压缩文件
    os.system('rm -rf ' + patchFloderPath)
    # 获取 zip 文件 MD5 码
    # zipFilePath = open(os.path.join(patchFloderPath,patchFloderFile))
    # zipFileString = zipFilePath.read()
    # zipFileMD5 = hashlib.md5()
    # zipFileMD5.update(zipFileString)
    # newImgMD5String = zipFileMD5.hexdigest()
    # zipFilePath.close()
    zipFilePath = patchFloderPath+".zip"
    return calculateMD5(zipFilePath)