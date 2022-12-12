# -*- coding: utf-8 -*-

import os
import re
from common.do_log import *
from common.do_config import *

logger = GetLog().getlog()
global filesPath
filesPath = []
class processData():
    def __init__(self,dir):
        self.dir = dir

    def getFilePath(self,dir):
        '''
        获取指定目录下的文件路径
        :param dir:
        :return: list
        '''
        global filePath
        dirs = []
        lsdir = os.listdir(dir)  # 获取目录下所有文件名称
        logger.info("获取的文件名称:{0}".format(lsdir))
        #dirs = [i for i in lsdir if os.path.isdir(os.path.join(dir, i))]
        for i in lsdir:

            if os.path.isfile(os.path.join(dir,i)):
                filePath = os.path.join(dir, i)
                print("1:" + filePath)
                filesPath.append(str(filePath))
                logger.info(filesPath)

            elif os.path.isdir(os.path.join(dir,i)):
                dirs = os.path.join(dir, i)
                print(dirs)
                self.getFilePath(dirs)  #递归遍历

            else:
                logger.info("文件格式未知")
                pass

        return filesPath

    def extract (self,wards):
        """
        正则匹配中文
        :param wards:
        :return: list
        """
        reTemp = re.compile('([^\w\s\<\>\-\--\{\}\[\]\(\)\&\$\@\*\;\:\'\"\,\+\=\?\!\%\#\|]+)+?')  # 逆向判断获取中文
        # reResult = reTemp.findall(str(wards))
        mo = r'[\u4e00-\u9fa5]+'
        try:
            reResult = re.findall(mo,wards)
        except:
            pass
            #reResult = re.findall(reTemp,wards)
        return reResult

    def readFile(self,filePath):
        textChinese = []
        #setcionName,optionName = self.getFileName(filePath)
        with open(filePath,'r',encoding="utf-8-sig") as f:
            for line in f: #读取文件内容按行返回
                #print("是每行读取吗:{0}".format(line))
                if ("//" in line) or ("<!--" in line) or ("/*" in line):
                    continue
                else:
                    lienText = self.extract(str(line))
                    logger.info("每行中文:{0}".format(lienText))
                    if len(lienText) == 0:
                        pass
                    else:
                        textChinese.append(lienText)
            return textChinese

    def getFileName(self,filePaht):
        '''
        根据文件路径提取上一级目录名称
        :param filePaht:
        :return:str
        '''
        nameList = filePaht.split("\\")
        print(nameList)
        lenMenber = len(nameList)
        dirName = str(nameList[-2])
        fileName = str(nameList[-1])
        #dirName = filePaht.strip("\\")[-2]
        logger.info("文件夹名称：{0} 文件名称：{1}".format(dirName,fileName))
        return dirName,fileName

class WiteData():

    def __init__(self):
        self.confingText = Config("resulfText.cfg")

    def witeBack(self,sectionName,optionName,text):
        sectionNames = self.confingText.getSections()
        if sectionName in sectionNames:
            self.confingText.writeInfo(sectionName,optionName,text)
        else:
            self.confingText.addSection(sectionName)
            self.confingText.writeInfo(sectionName, optionName, text)










if __name__ == '__main__':
    dir_path ="D:\\cimc-rent-mini"
    test = processData(dir_path)
    filesPath = test.getFilePath(dir_path)
    print(filesPath)
    for i in filesPath:  #遍历每一个文件路径的列表
        text = str(test.readFile(i))
        dirName, fileName = test.getFileName(i)
        print("第一：{0}".format(text))
        print("第二：{0},{1}".format(dirName, fileName))
        WiteData().witeBack(dirName,fileName,text)







