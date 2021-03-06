# !/usr/bin/env python
# -*= coding: utf-8 -*-

__author__ = 'wtq'

from numpy import zeros

from detector.config import PERMISSIONS_COLLECTION
from detector.db.session import MongDBSession
from detector.logger import AdDetectorLogger

logger = AdDetectorLogger()


class BasePermission(object):
    def __init__(self):
        self.session = MongDBSession()

    def get_permission_from_apk(self, apk):
        """
        :param apk: use androguard to deal apk
        :return: permissions of the apk
        """
        permission = []
        requested_permissions = apk.get_requested_permissions()
        for i in requested_permissions:
            str_permission = i.split('.')
            stand_permission = str_permission[-1]
            permission.append(stand_permission)
        return permission

    def get_standard_permission_from_mongodb(self):
        """
        :return: the stand permission list form google
        """

        stand_permissions_dict = self.session.query_one(PERMISSIONS_COLLECTION)
        stand_permissions = stand_permissions_dict['permissions']
        return stand_permissions

    def create_permission_vector(self, stand_permissions, input_permissions):
        """
        :param stand_permissions: the stand permission of google
        :param input_permissions: the permission that you want to convert vector
        :return: the vector of permission
        """

        return_permission = zeros(len(stand_permissions))
        return_permission = list(return_permission)
        for permission in input_permissions:
            if permission in stand_permissions:
                return_permission[stand_permissions.index(permission)] = 1
            # else:
            #     logger.debug("the permission: %s is not"
            #                  " in my permission list" % permission)
        return return_permission
