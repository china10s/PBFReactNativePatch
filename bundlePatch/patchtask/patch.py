#coding=utf-8

"""
Author: zhulin (china10s)
Usage: python patch.py
Description:
            Automatically pack reactnative jsbundle and different package,directory structure：
             -Root
                -[ios]                              //ios 目录
                -[android]
                -[node_modules]
                -package.json
                -index.ios.js
                -index.android.js
                -[bundlePatch]
                   -[bundles]                       //源文件目录
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
                   -[patches]                       //差异包目录
                      -1_0_0
                      -1_0_1
                         -ios
                            -1_0_0-1_0_1.zip
                         -android
                            -1_0_0-1_0_1.zip
                   -[patchtask]                     //任务脚本
                      -build
                      patch.py                      //脚本入口
                      diff_match_patch.py           //打包算法
Version: 1.0
"""

import os

from patchJSBuild import *
from patchCompare import *

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

    # 打差异包
    for oldVersionFloder in os.listdir(bundlesPath):
        if oldVersionFloder == '.DS_Store':
            continue
        print '### ios '+oldVersionFloder+' 差异包生成中 ###'
        # 比较文件
        compareWithPlatform('ios', oldVersionFloder,newVerion)
        print '### ios '+oldVersionFloder+' 差异包生成完成 ###'
        print '### android '+oldVersionFloder+' 差异包生成中 ###'
        # 比较文件
        compareWithPlatform('android', oldVersionFloder,newVerion)
        print '### android '+oldVersionFloder+' 差异包生成完成 ###'

    # 更新 bundles 目录
    buildBundlePath = './build/'
    newBundlePath = os.path.join(bundlesPath,newVerion)
    cpString = 'cp -r '+buildBundlePath +' '+newBundlePath
    os.system(cpString)
    os.system('open ../bundles')

main()
