# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

import os
import zipfile
from detector.logger import DetectorLogger

logger = DetectorLogger()


def get_dex_file(apk_path, dex_path):
    """
    extract the classes.dex file from apk
    :return:
    """
    apklist = os.listdir(apk_path)
    print ('waiting...')
    if not os.path.exists(dex_path):
        os.makedirs(dex_path)

    for APK in apklist:
        # scan the sub dir under the input dir
        sub_path = os.path.join(apk_path, APK)
        if os.path.isdir(sub_path):
            get_dex_file(sub_path, dex_path)

        try:
            print 'apk', os.path.join(apk_path, APK)
            portion = os.path.splitext(APK)
            newname = portion[0] + '.zip'
            if portion[1] == '.apk':
                # 使用rename得在当前目录下所以加上os.path,join(),也可使用partion[1]='.zip'
                os.rename(os.path.join(apk_path, APK), os.path.join(apk_path, newname))

            apkname = portion[0]
            zip_apk_path = os.path.join(apk_path, newname)
            z = zipfile.ZipFile(zip_apk_path, 'r')

            for filename in z.namelist():

                if filename.endswith('.dex'):
                    dexfilename = apkname + '.dex'
                    dexfilepath = os.path.join(dex_path, dexfilename)
                    f = file(dexfilepath, 'w')
                    f.write(z.read(filename))
                    f.close()
        except Exception, e:
            logger.info('error')
            logger.info(e)



