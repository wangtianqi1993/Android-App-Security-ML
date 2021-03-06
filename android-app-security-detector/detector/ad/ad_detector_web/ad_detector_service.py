# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

import threading
from threading import Lock
import time
import os
import urllib
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import requests
import json
from detector.ad.ad_detector_web.task_queue import detector_task, running_detector_task
from detector.config import DOWNLOAD_PATH, WEB_IP, LOCATION_URL, HEART_IP, WEB_PORT, HEART_PATH, REQUEST_URL, AGENT_ID
from detector.logger import AdDetectorLogger

logger = AdDetectorLogger()

define('port', default=8889, help='run on the given port', type=int)
# 0 -> zhou 1 -> qin


class AppWebService:

    def start(self):
        logger.info(threading.current_thread().name + ' start listening.....')
        tornado.options.parse_command_line()
        # app = tornado.web.Application(handlers=[(r"/detector/(.*)", AdDetectorHandler)])
        app = tornado.web.Application(handlers=[(r"/addetector/(.*)", AdDetectorHandler)])

        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(options.port, address='0.0.0.0')

        tornado.ioloop.IOLoop.instance().start()

    def heart_beat(self):
        logger.info(threading.current_thread().name + 'heart beat listening.....')
        while True:
            # 接受端会根据maxcap-currentload来决定要发送给这一端的apk loaction数量
            r = requests.put(HEART_IP + ":" + WEB_PORT + HEART_PATH,
                             data=json.dumps({"ip": "10.108.115.114", "port": 8889, "type": "05", "version": "01", "status": 1,
                                              "maxCap": 1, "currentLoad": len(running_detector_task)}))
            print r.status_code
            time.sleep(3)


class AdDetectorHandler(tornado.web.RequestHandler):

    def post(self, task_id):

        # print(threading.current_thread().name() + ":" + "AdDetector Running....")

        self.write("{\"code\":200,\"msg\":\"ok\"}")
        # 获取客户端传过来的json数据
        sign = 1
        data = self.request.body
        str_data = data.decode('utf-8')
        request_parameter = json.loads(str_data)

        download_uri = request_parameter['location']
        if 'port' in request_parameter:
            # sign to zhou
            sign = 0
            port = request_parameter['port']
        if 'path' in request_parameter:
            path = request_parameter['path']


        detector_report = {'tast_id': task_id}
        # 得到请求端的ip
        ip = self.request.remote_ip
        remote_url = LOCATION_URL + download_uri
        # remote_url = download_uri
        app_name = download_uri.split('/')[-1] + ".apk"
        detector_report['app_name'] = app_name

        # 判断服务器发送过来的任务是否正在进行或者在等待中，不是就下载apk并加入到任务队列
        if task_id in running_detector_task:
            print('already has the task!')
        else:

            try:
                # 下载apk到制定目录
                download_path = os.path.join(DOWNLOAD_PATH, app_name)
                urllib.urlretrieve(remote_url, download_path)
                # urllib.urlretrieve(download_uri, download_path)
                print("下载成功！")

                # 保证存储任务时为原子操作
                lock = Lock()
                lock.acquire()
                # 向队列中添加信息
                print ("加入任务队列")
                detector_task.sign.put(sign)
                detector_task.task_id.put(task_id)
                detector_task.app_name.put(app_name)
                detector_task.wed_ip.put(ip)
                if not sign:
                    detector_task.port.put(port)
                    detector_task.path.put(path)

                running_detector_task[task_id] = app_name
                lock.release()
            except Exception as e:
                print ('e download = ' + str(e))
                # 返回数据到请求的一端
                if sign:
                    r = requests.put("http://" + ip + ":" + str(WEB_PORT) + REQUEST_URL
                    + task_id, data=json.dumps({"agent_id": AGENT_ID, "status": 0, "detector_report": ""}))
                else:
                    r = requests.put("http://" + ip + ":" + str(port) + path
                                    + task_id, data=json.dumps({"agent_id": AGENT_ID, "status": 0, "detector_report": ""}))

    def get(self, task_id):
        print("get")
        self.post(task_id)

    def put(self, task_id):
        print("put")
        self.post(task_id)
