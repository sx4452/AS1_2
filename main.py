__author__ = 'ben'

import jieba
import codecs
import os
import jieba.analyse
import math
import time
import sys
from TFIDF import TFIDF

reload(sys)                                                                          #Set the coding as 'utf-8' or you will get chaos
sys.setdefaultencoding('utf8')

def main():
    #########Input and Output##########                                              #IMPORTANT!
    lilypath = 'lily'                                                               #IMPORTANT! Set your own lily path and stopWords
    stopWordspath = 'Chinese-stop-words.txt'                                     #IMPORTANT!
    stopWords = codecs.open(stopWordspath, 'r', 'gbk')
    inputfile = {}
    outputfile = {}
    filenames = os.listdir(lilypath)
    cnt = 0
    for filename in filenames:
        inputfile[cnt] = codecs.open(lilypath + '/' + filename, 'r', 'utf-8')
        outputfile[cnt] = open(filename, 'w+')
        cnt += 1
    #############TFIDF#############
    TFIDF(inputfile, outputfile, stopWords, cnt)                   #The TFIDF algorithem
    for i in range(0, cnt):
        inputfile[i].close()
        outputfile[i].close()
    stopWords.close()

if __name__ == "__main__":
    start = time.clock()
    print start
    main()
    end = time.clock()
    print 'runtime is '
    print end
