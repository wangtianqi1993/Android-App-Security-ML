# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wtq'

import os
from androguard.core import androconf
from androguard.core.bytecodes import apk
from detector.logger import DetectorLogger

logger = DetectorLogger(path = "apk_information.log")


def get_apk_info(apk_path):
    """
    get the apk base information then save to log
    :param apk_path:
    :return:
    """
    ret_type = androconf.is_android(apk_path)
    if ret_type == "APK":
        logger.info(os.path.basename(apk_path) + ":")
        try:
            a = apk.APK(apk_path)
            if a.is_valid_APK():

                activities = a.get_activities()
                for i in activities:
                    logger.info(i)

                services = a.get_services()
                for i in services:
                    logger.info(i)

                receivers = a.get_receivers()
                for i in receivers:
                    logger.info(i)

                permissions = a.get_requested_permissions()
                for i in permissions:
                    logger.info(i)

        except Exception, e:
            logger.info(e)


if __name__ == "__main__":
    get_apk_info("/home/wtq/Downloads/2dd8691142974b3562d769ac57d9aacb.apk")
