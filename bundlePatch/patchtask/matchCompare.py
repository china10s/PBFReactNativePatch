#coding=utf-8

import os,zipfile

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
        #将 oldversion 拷贝到 temp 目录下
        oldBundlesPath = '../bundles/' + oldVersion +'/'+platformType+'/'
        if os.path.isdir(oldBundlesPath):
            cpString = 'cp -r ' + oldBundlesPath + ' ' + tempPath+'/'+oldVersion
            os.system(cpString)

    # 删除 temp 文件夹
    os.system('rm -rf '+os.path.join(patchPlatformPath,'temp'))


def compareMatchPlatform(patchVersionFloderPath, platformType):
    patchPlatformPath = os.path.join(patchVersionFloderPath,platformType)
    for patchVersionName in os.listdir(patchPlatformPath):
        patchVersionPath = os.path.join(patchPlatformPath, patchVersionName)
        if zipfile.is_zipfile(patchVersionPath):
            compareMatchVersion(patchPlatformPath,platformType,patchVersionName)

