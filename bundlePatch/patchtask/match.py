#coding=utf-8

import os
from matchCompare import *

def main():
    # 当前目录
    currentPath = os.getcwd()
    # patches 目录
    patchesPath = '../patches/'

    patchesVersionList = os.listdir(patchesPath)
    if len(patchesVersionList) <= 0:
        return
    patchNewVersion = patchesVersionList[-1]
    patchVersionFloderPath = patchesPath+patchNewVersion
    if not os.path.isdir(patchVersionFloderPath):
        return
    print 'match 新版本号为：'+patchNewVersion
    for platformType in  os.listdir(patchVersionFloderPath):
        compareMatchPlatform(patchVersionFloderPath, platformType)

main()