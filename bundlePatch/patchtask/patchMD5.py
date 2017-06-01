#coding=utf-8
import os,hashlib

def calculateMD5(filePath):
    fileIn = open(filePath)
    fileInString = fileIn.read()
    fileMD5 = hashlib.md5()
    fileMD5.update(fileInString)
    md5String = fileMD5.hexdigest()
    fileIn.close()
    return md5String