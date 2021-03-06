# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import numpy
from androguard.core import androconf
from androguard.core.bytecodes import apk
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

from detector.config import CLASSIFIER_PATH
from detector.config import TRAIN_PERMISSION
from detector.error import AdDetectorException
from detector.logger import AdDetectorLogger
from .base import BasePermission

logger = AdDetectorLogger()


class AdBasePredict(BasePermission):
    predictor = None

    def __init__(self):
        super(AdBasePredict, self).__init__()

        if self.predictor is None:
            raise AdDetectorException('You must init an predictor'
                                      ' using an method！')

        # init predictor
        trained_permissions = self.session.query_sort(TRAIN_PERMISSION,
                                                      'create', limit=1)

        permission_list = trained_permissions['train-permission']
        self.stand_permissions = self.get_standard_permission_from_mongodb()
        train_vector = []
        all_train_permissions = permission_list[0]
        for _permission in all_train_permissions:
            _vector = self.create_permission_vector(
                self.stand_permissions, _permission)
            train_vector.append(_vector)

        sample_x = train_vector
        sample_y = numpy.array(permission_list[1])
        self.predictor.fit(sample_x, sample_y)

    def predict_ad_classifier(self, classifier_name, apk_path):
        """
        :param classifier_name: the classifier name
        :param apk_path: a apk path that you want to detector
        :return: 1->content ad 0->not contentad
        """
        # 加载训练好的分类器
        clf = joblib.load(CLASSIFIER_PATH + classifier_name + ".m")

        # clf, train_id = self.train_classifier(clf, classifier_name)
        stand_permissions = self.get_standard_permission_from_mongodb()
        ret_type = androconf.is_android(apk_path)
        if ret_type == "APK":
            try:
                a = apk.APK(apk_path)
                if a.is_valid_APK():
                    predict_permission = self.create_permission_vector(
                        stand_permissions, self.get_permission_from_apk(a))
                    logger.info(os.path.basename(apk_path) + ' classified as: ')
                    logger.info(clf.predict(predict_permission))
                    return clf.predict(predict_permission)[0]
                else:
                    logger.info("INVALID")

            except Exception, e:
                logger.info(e)
        else:
            logger.info("is not a apk!!!")

    def predict(self, apk_path):
        # if apk_path is APK
        ret_type = androconf.is_android(apk_path)
        if ret_type == "APK":
            try:
                a = apk.APK(apk_path)
                if a.is_valid_APK():

                    apk_permissions = self.get_permission_from_apk(a)
                    predict_vector = self.create_permission_vector(
                        self.stand_permissions, apk_permissions)
                    return self.predictor.predict([predict_vector])
                else:
                    logger.info("INVALID")
                    raise AdDetectorException('There is not a valid apk!!!')

            except Exception, e:
                logger.info(e.message)
        else:
            logger.info("There is not a apk!!!")
            raise AdDetectorException('There is not a apk!!!')


class AdGaussianPredict(AdBasePredict):
    def __init__(self):
        self.predictor = GaussianNB()
        super(AdGaussianPredict, self).__init__()


class AdBernoulliPredict(AdBasePredict):
    def __init__(self):
        self.predictor = BernoulliNB()
        super(AdBernoulliPredict, self).__init__()


class AdMultinomialPredict(AdBasePredict):
    def __init__(self):
        self.predictor = MultinomialNB()
        super(AdMultinomialPredict, self).__init__()



class AdSVMPredict(AdBasePredict):
    def __init__(self):
        self.predictor = SVC()
        super(AdSVMPredict, self).__init__()


class AdRandomForestPredict(AdBasePredict):
    def __init__(self, n_estimators=20):
        self.predictor = RandomForestClassifier(n_estimators=n_estimators)
        super(AdRandomForestPredict, self).__init__()
