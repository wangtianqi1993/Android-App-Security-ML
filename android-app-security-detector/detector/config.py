#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

current_path = os.path.dirname(__file__)

# app name
APP_NAME = 'Android application detector'

# app extension name
APP_EXTENSION_NAME = 'apk'

# log file path
LOG_PATH = 'detector_logging.log'


# Mongodb HOST and PORT
MONGODB_HOST = '10.108.114.233'
MONGODB_PORT = 27017

# H5Detector DB Name
DETECTOR_DB_NAME = 'detector'
PERMISSIONS_COLLECTION = 'android-permissions'
TRAIN_NAIVEBAYES = 'trainbayes'
TEST_NAIVEBAYES = 'testbayes'
TRAIN_SVM = 'trainsvm'
TEST_SVM = 'testsvm'
TRAIN_PERMISSION = 'train-permission'
MALWARE_SOURCE = 'malware_source'
BENIGN_SOURCE = 'benign_source'
# Test Apk Path Config
ENV_PATH = os.environ.get('VIRTUAL_ENV', sys.prefix)
TEST_APK_PATH = os.path.join(ENV_PATH, 'apkpath/testapk')

# Train Apk Path
TRAIN_APK_PATH = os.path.join(ENV_PATH, 'apkpath/trainapk')

# save classifier path
CLASSIFIER_PATH = os.path.join(ENV_PATH, 'train_save/')

# Backup mongodb path
BACKUP_TRAIN_PATH = os.path.join(ENV_PATH, 'mongodb/train_ad_permission.txt')
BACKUP_TEST_PATH = os.path.join(ENV_PATH, 'mongodb/backup_test')
BACKUP_MALWARE_SOURCE = os.path.join(ENV_PATH, 'mongodb/backup_malware_source.txt')
BACKUP_BENIGN_SOURCE = os.path.join(ENV_PATH, 'mongodb/backup_benign_source.txt')

# State Description
TRAIN_DESCRIPTION = 'the item is bayes probability'
TEST_DESCRIPTION = 'the item is test analysis'
TRAIN_SVM_DESCRIPTION = 'the item is svm state'

# Sort Parameter
SORT_PARAMETER = 'createdAt:-1'

# virtualenv path
ENV_PATH = os.environ.get('VIRTUAL_ENV', sys.prefix)
DECOMPRESS_PATH = os.path.join(ENV_PATH, 'decompress/')

# AD feature json file
AD_FEATURE_FILE = os.path.join(current_path, 'adfeature.json')
MALWARE_FEATURE = '/home/wtq/develop/workspace/gitlab/android-app-security-detector/detector/malware/malware_feature.json'
# Service reference
DOWNLOAD_PATH = os.path.join(ENV_PATH, 'apkpath/download')
WEB_IP = '10.108.112.23'
LOCATION_URL = 'http://dfs.asec.buptnsrc.com/'
# REQUEST_URL = '/subtask/advertise/'
REQUEST_URL = '/apkagent/advertise/'
HEART_IP = 'http://docker.buptnsrc.com'

HEART_PATH = '/heart_beat/addetector'
WEB_PORT = '4466'
AGENT_ID = 'addetector'


JAD = '/home/wtq/develop/developtools/jad-tools/jad'
