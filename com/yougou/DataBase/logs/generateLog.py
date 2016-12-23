#!/usr/bin/python
#encoding=utf-8

import time
import datetime
import os

def fileStream():
    #文件读取的路径
    readpath='/usr/local/ltz/log/generated/20160426.log'
    #文件写入的路径
    fwriterpath="/usr/local/ltz/log/test.log"
    #file=open(readpath,'r')
    i=0
    while i<100:
        now = str(time.time())
        if(os.path.exists(fwriterpath)=='false'):
            os.mknod(fwriterpath)
            print  '创建待写入的文件'

        with open(readpath,'r') as file:
            for line in file.readlines():
                time.sleep(1)
                with open(fwriterpath, 'a') as fwriter:
                    print line
                    fwriter.write(line)


        i=i+1
        os.rename(fwriterpath,"/usr/local/ltz/log/"+now)
        print('生成文件'+now)
        os.remove("/usr/local/ltz/log/"+now)
        print '移除文件'


if __name__=='__main__':
    starttime = datetime.datetime.now()
    fileStream()
    endtime = datetime.datetime.now()
    print "Total time costs  :   %ds" % ((endtime - starttime).seconds)







