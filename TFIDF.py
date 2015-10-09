__author__ = 'ben'

import jieba
import codecs
import os
import jieba.analyse
import math
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def TFIDF(inputFile, outputFile, stopWords, fileCnt):
    print 'doing TFIDF...'
    stopWordsline = stopWords.readlines()
    lineAll = 0
    TF = {}
    tf = {}
    WordSeg = {}                                                                                                        #WordSeg:all keyword in one .txt and its showup line number
    for i in range(0, fileCnt):
        lineCnt = 0
        inputread = inputFile[i].read()
        seg_list = jieba.cut(inputread)
        TF[i]={}
        for seg in seg_list :
            if (seg == "\n" or seg == "\r" or seg == "\n\r" or seg == "\r\n" or seg == "\n\n"):
                for j in range(0, len(stopWordsline)):                                                                 #delete stopwords for each line
                    if(tf.has_key(stopWordsline[j][:-2]) == True):
                        del tf[stopWordsline[j][:-2]]
                TF[i][lineCnt] = {}
                for j in tf:
                    TF[i][lineCnt][j] = float(tf[j])                                                                    #TF:the number of keyword'i' in lineCnt
                lineCnt += 1
                lineAll += 1
                tf.clear()
            else:
                if (seg != '' and seg != "\n" and seg != "\n\n") :
                    if seg in tf :
                        tf[seg] += 1
                    else :
                        tf[seg] = 1
        for j in range(0, lineCnt):
            for k in TF[i][j]:
                if (k in WordSeg):
                    WordSeg[k] += 1
                else:
                    WordSeg[k] = 1
    for i in range(0, fileCnt):
        tmpseg = '\t'
        outputFile[i].write(tmpseg)
        wordCnt = 0
        for j in WordSeg:
            tmpseg = j + ' '
            outputFile[i].write(tmpseg)
            wordCnt += 1
        print wordCnt
        outputFile[i].write('\n\r')
        #outputFile[i].next()
        for j in range(0, len(TF[i])):
            tmpseg = 'Line' + str(j+1) + ':'
            outputFile[i].write(tmpseg)
            for k in WordSeg:
                if(TF[i][j].has_key(k) == False):
                    tmpseg = '0' + ' '
                    outputFile[i].write(tmpseg)
                else:
                    tfidf = round(TF[i][j][k] * math.log(float(lineAll)/float(WordSeg[k]), 10), 4)
                    tmpseg = str(tfidf) + ' '
                    outputFile[i].write(tmpseg)
            outputFile[i].write('\n\r')
            #outputFile[i].next()