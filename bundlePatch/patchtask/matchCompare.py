#coding=utf-8

import os,zipfile
from matchJSFile import *

def compareMatchVersion(patchPlatformPath,platformType,patchVersionName):
    patchVersionPath = os.path.join(patchPlatformPath, patchVersionName)
    f = zipfile.ZipFile(patchVersionPath, 'r')
    # 解压生成 temp 文件夹
    tempPath = os.path.join(patchPlatformPath,'temp')
    for file in f.namelist():
        f.extract(file, tempPath)

    patchVersions = os.path.splitext(patchVersionName)
    filenames = patchVersions[0].split('-')
    if len(filenames) == 2:
        oldVersion = filenames[0]
        newVersion = filenames[1]
        newVersionTmpPath = tempPath + '/' + newVersion
        oldVersionTmpPath = tempPath + '/' + oldVersion
        patchVersionTmpPath = tempPath + '/' + patchVersions[0]
        #将 oldversion 拷贝到 temp 目录下
        oldBundlesPath = '../bundles/' + oldVersion +'/'+platformType+'/'
        if os.path.isdir(oldBundlesPath):
            cpString = 'cp -r ' + oldBundlesPath + ' ' + oldVersionTmpPath
            os.system(cpString)
        #temp 目录下新建新版本文件夹
        os.system('mkdir '+newVersionTmpPath)
        #打补丁验证
        for fileName in os.listdir(patchVersionTmpPath):
            if fileName == '.DS_Store':
                continue
            filePath = os.path.join(patchVersionTmpPath,fileName)
            if os.path.isdir(filePath):
                #文件夹
                print '文件夹'
            else:
                #JS文件
                compareMatchJSFile(newVersionTmpPath,oldVersionTmpPath,patchVersionTmpPath,fileName);

    # 删除 temp 文件夹
    os.system('rm -rf '+os.path.join(patchPlatformPath,'temp'))


def compareMatchPlatform(patchVersionFloderPath, platformType):
    patchPlatformPath = os.path.join(patchVersionFloderPath,platformType)
    for patchVersionName in os.listdir(patchPlatformPath):
        patchVersionPath = os.path.join(patchPlatformPath, patchVersionName)
        if zipfile.is_zipfile(patchVersionPath):
            compareMatchVersion(patchPlatformPath,platformType,patchVersionName)

