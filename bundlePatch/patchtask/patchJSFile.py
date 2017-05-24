#coding=utf-8

import os
import diff_match_patch as dmp_module
dmp = dmp_module.diff_match_patch()

def compareJSFileWithPath(oldFilePath,newFilePath,patchFloderPath,jsNewFile):
    if os.path.isfile(oldFilePath):
        newFile = open(newFilePath)
        newJSString = newFile.read()
        oldFile = open(oldFilePath)
        oldJSString = oldFile.read()
        arrDiff = dmp.diff_main(oldJSString, newJSString)
        arrDiffs = dmp.patch_make(arrDiff)
        patchString = dmp.patch_toText(arrDiffs)
        if patchString != '':
            # 创建 patch 文件
            patchFilePatth = patchFloderPath + '/' + jsNewFile + '.patch'
            os.system("touch " + patchFilePatth)
            filePatch = file(patchFilePatth, "a+")
            filePatch.write(patchString)
            filePatch.close()
            newFile.close()
            oldFile.close()
    else:
        # 移动新文件
        os.system('cp ' + newFilePath + ' ' + os.path.join(patchFloderPath, jsNewFile))