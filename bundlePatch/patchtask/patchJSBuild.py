#coding=utf-8

import os


def JSBuild():
    print '### js 打包中 ###'
    # 删除原有目录
    os.system('rm -rf ./build/android')
    os.system('rm -rf ./build/ios')
    # 新建目录
    os.system('mkdir -p ./build/android')
    os.system('mkdir -p ./build/ios')
    # 打包 Andorid 和 iOS 的 JSBundle
    os.system(
        'cd ../../ ; react-native bundle --entry-file index.android.js --platform android --assets-dest ./bundlePatch/patchtask/build/android --bundle-output ./bundlePatch/patchtask/build/android/android.jsbundle --dev false')
    os.system(
        'cd ../../ ; react-native bundle --entry-file index.ios.js --platform ios --assets-dest ./bundlePatch/patchtask/build/ios --bundle-output ./bundlePatch/patchtask/build/ios/ios.jsbundle --dev false')
    print '### js 打包完成 ###'