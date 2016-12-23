#!/usr/bin/python
#encoding=utf-8

import os
import time
import datetime

def py_function():
     fwriterpath="/usr/local/ltz/log/test.log"
     now = int(time.time())
     os.rename(fwriterpath,"/usr/local/ltz/log/"+now)
if __name__:
    starttime = datetime.datetime.now()
    py_function()
    endtime = datetime.datetime.now()
    print "Total time costs  :   %ds" % ((endtime - starttime).seconds)