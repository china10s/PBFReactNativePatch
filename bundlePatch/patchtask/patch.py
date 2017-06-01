#coding=utf-8

"""
Author: zhulin (china10s)
Usage: python patch.py
Description:
Automatically pack reactnative jsbundle and different package,directory structure：
             -Root
                -package.json
                -index.ios.js
                -index.android.js
                -[bundlePatch]
                   -[bundles]                       //source floder
                      -1_0_0
                         -ios
                            -assets
                            -ios.jsbundle
                         -android
                            -drawable-mdpi
                            -android.jsbundle
                      -1_0_1
                         -ios
                            -assets
                            -ios.jsbundle
                         -android
                            -drawable-mdpi
                            -android.jsbundle
                   -[patches]                       //differ patch
                      -1_0_0
                      -1_0_1
                         -ios
                            -1_0_0-1_0_1.zip
                         -android
                            -1_0_0-1_0_1.zip
                   -[patchtask]                     //job
                      -build
                      patch.py                      //main function
                      patchImageFile.py
                      patchJSBuild.py
                      patchJSFile.py
                      patchCompare.py
                      patchZip.py
                      diff_match_patch.py
Version: 1.0
"""

import os,json

from patchJSBuild import *
from patchCompare import *
from patchZip import *

# 生成 upgrade.json 文件
def createUpgradeJson(jsonString,patchespath):
    fileUpgradePath = patchespath+'/'+'upgrade.json'
    os.system('touch '+fileUpgradePath)
    upgradeFile = open(fileUpgradePath,'w')
    upgradeFile.write(jsonString)
    upgradeFile.close()

# 主函数
def main():
    reload(dmp_module)
    # 获取当前脚本目录
    currentPath = os.getcwd()
    # 获取工作目录
    currentPaths = os.path.split(currentPath)
    workpath = currentPaths[0]
    # bundles 地址
    bundlesPath = workpath + '/bundles'
    if not os.path.isdir(bundlesPath):
        os.system('mkdir -p ' + bundlesPath)
    # patches 地址
    patchesPath = workpath + '/patches'
    if not os.path.isdir(patchesPath):
        os.system('mkdir -p ' + patchesPath)

    # 按照版本号放入
    print '输入本次发布的版本号:'
    newVerion = raw_input()
    newVerion = newVerion.replace('.', '_')

    print '是否需要重新编译 jsbundle：n ? y'
    isAutoJsBundlePack = raw_input()
    if isAutoJsBundlePack == 'y':
        JSBuild()

    # 更新 bundles 目录
    buildBundlePath = './build/'
    newBundlePath = os.path.join(bundlesPath, newVerion)
    os.system('rm -rf ' + newBundlePath)
    cpBundleString = 'cp -r ' + buildBundlePath + ' ' + newBundlePath
    os.system(cpBundleString)

    upgradeJsonString = ""
    upgradeJsonArry = []

    # 1、打差异包
    for oldVersionFloder in os.listdir(bundlesPath):
        if oldVersionFloder == '.DS_Store':
            continue
        print '### ios '+oldVersionFloder+' 差异包生成中 ###'
        # 比较文件
        iosMd5 = compareWithPlatform('ios', oldVersionFloder,newVerion)
        print '### ios '+oldVersionFloder+' 差异包生成完成 ###'
        print '### android '+oldVersionFloder+' 差异包生成中 ###'
        # 比较文件
        androidMd5 = compareWithPlatform('android', oldVersionFloder,newVerion)
        print '### android '+oldVersionFloder+' 差异包生成完成 ###'
        # upgradeJson
        patchFileName = oldVersionFloder+'-'+newVerion
        upgradeJsonArry.append({'v':patchFileName,'iosBundleMd5':iosMd5,'androidBundleMd5':androidMd5,'filename':patchFileName+'.zip'})

    # 2、打全量包到 patches 目录下
    entireiOSMD5 = copyBundleZip(newBundlePath,patchesPath,'ios',newVerion)
    entireAndroidMD5 = copyBundleZip(newBundlePath, patchesPath, 'android', newVerion)
    upgradeJsonArry.append({
            'v':newVerion, 'iosBundleMd5':entireiOSMD5, 'androidBundleMd5':entireAndroidMD5,'filename':newVerion+'.zip'})
    upgradeJson = json.dumps(upgradeJsonArry)

    # 3、生成 upgrade.json
    patchesJsonPath = os.path.join(patchesPath, newVerion)
    createUpgradeJson(upgradeJson,patchesJsonPath)

    # 打开文件夹
    os.system('open ../bundles')

main()
