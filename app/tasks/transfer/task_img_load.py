# coding: utf-8
import time

from tasks.task import Task

from utils.util import *
from utils.settings import *

from procs.transfer.img_load import ImageLoader

MAX_COLLECT_COUNT = 400

class TaskImgLoader(Task):
    #---------------------------------------------
    # constructor
    def __init__(self, params={}):
        super(TaskImgLoader, self).__init__(params)

        self.loader = None

    #-------------------------------------
    # init_self
    def init_self(self):
        self.loader = ImageLoader()

        self.count.value = 0
        pass

    def run_self(self):

        count = 0
        #items = []

        while count < MAX_COLLECT_COUNT:

            data = self.get_input_data()

            if data is not None:
                time.sleep(1)

                self.put_output_data(data)
                self.count.value += 1
                count += 1


        # 특정 개수 까지 모았다가 한번에 queue에 집어넣기
        # for item in items:
        #     self.put_output_data(item)
        #     self.count.value += 1
