# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__author__ = 'wtq'

from detector.ad.permission.predict import AdGaussianPredict
from detector.ad.permission.predict import AdRandomForestPredict
from detector.ad.permission.predict import AdSVMPredict
from detector.ad.ad_detector_web.ad_detector import ad_detector
if __name__ == '__main__':
    # ad_predictor = AdGaussianPredict()
    # print ad_predictor.predict('/home/kevin/Temps/ad.apk')
    # print ad_predictor.predict('/home/kevin/Temps/notad.apk')
    # svm_predict = AdSVMPredict()
    # print svm_predict.predict('/home/kevin/Temps/ad.apk')
    # print svm_predict.predict('/home/kevin/Temps/notad.apk')
    random_forest_predict = AdRandomForestPredict()
    # print random_forest_predict.predict('/home/kevin/Temps/ad.apk')
    # print random_forest_predict.predict('/home/kevin/Temps/notad.apk')
    print ad_detector("/media/wtq/0008943A0007A7BC/android-ad-apk/test_apk/mojitianqi_58602.apk")
    # print random_forest_predict.predict("/media/wtq/0008943A0007A7BC/android-ad-apk/test_apk/mojitianqi_58602.apk")
