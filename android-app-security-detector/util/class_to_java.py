# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

import time
import os
import sys
from detector.logger import DetectorLogger
import subprocess


logger = DetectorLogger()


def change_class_to_java():
    """
    此函数没有用了，class到java是通过class_to_java脚本实现的
    通过命令行执行该程序带上当前dex目录与要存放的
    反编译得到的java文件路径
    :return:
    """
    try:
        # 得到在命令行输入的两个参数
        arg0 = sys.argv[1]
        for parent, dirname, filenames in os.walk(arg0):

            # 调用shell命令执行,传入的两个参数间用空格分开
            # 当文件apk文件里有不同级别的子文件夹时，此出入方式也适用
            # 最好用subprocess.Popen()来代替os.system()执行shell脚本,os.system耗资源，不安全
            #os.system('./jad_decom.sh ' + parent)
            ps = subprocess.Popen('bash ./jad_decom.sh ' + parent, shell=True)
            # pa.wait等线程执行完
            ps.wait()
    except Exception, e:
        import traceback
        traceback.print_exc()
        logger.info('error')
        logger.info(e)


if __name__ == '__main__':
    change_class_to_java()
    print "py end!!!"

