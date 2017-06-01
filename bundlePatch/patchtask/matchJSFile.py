#coding=utf-8

import os
import diff_match_patch as dmp_module
dmp = dmp_module.diff_match_patch()

def compareMatchJSFile(newVersionTmpPath,oldVersionTmpPath,patchVersionTmpPath,fileName):
    extensions = os.path.splitext(fileName)
    if len(extensions) != 2:
        return
    # 补丁包地址

    if extensions[1] == '.patch':
        patchVersionTmpFilePath = os.path.join(patchVersionTmpPath, fileName)
        oldVersionTmpFilePath = os.path.join(oldVersionTmpPath, extensions[0])
        newVersionTmpFilePath = os.path.join(newVersionTmpPath, extensions[0])

        #补丁包
        patchFile = open(patchVersionTmpFilePath)
        patchFileString = patchFile.read()
        oldFile = open(oldVersionTmpFilePath)
        oldFileString = oldFile.read()
        patches = dmp.patch_fromText(patchFileString)
        arres = dmp.patch_apply(patches,oldFileString)
        newFileString = arres[0]
        #创建新版本文件
        os.system("touch " + newVersionTmpFilePath)
        newFilePath = file(newVersionTmpFilePath, "a+")
        newFilePath.write(newFileString)
        newFilePath.close()
        patchFile.close()
        patchFile.close()

    else:
        patchVersionTmpFilePath = os.path.join(patchVersionTmpPath, fileName)
        newVersionTmpFilePath = os.path.join(newVersionTmpPath, fileName)
        #直接覆盖
        os.system('cp '+patchVersionTmpFilePath+' '+newVersionTmpFilePath)
