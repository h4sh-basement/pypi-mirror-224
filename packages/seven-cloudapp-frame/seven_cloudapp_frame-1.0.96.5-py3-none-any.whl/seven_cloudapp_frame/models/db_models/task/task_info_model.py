# -*- coding: utf-8 -*-
"""
@Author: HuangJianYi
@Date: 2021-08-10 10:09:06
@LastEditTime: 2021-08-12 10:11:20
@LastEditors: HuangJianYi
@Description: 
"""

#此文件由rigger自动生成
from seven_framework.mysql import MySQLHelper
from seven_framework.base_model import *
from seven_cloudapp_frame.models.cache_model import *


class TaskInfoModel(CacheModel):
    def __init__(self, db_connect_key='db_cloudapp', sub_table=None, db_transaction=None, context=None):
        super(TaskInfoModel, self).__init__(TaskInfo, sub_table)
        db_connect_key = "db_task" if config.get_value("db_task") else db_connect_key
        self.db = MySQLHelper(config.get_value(db_connect_key))
        self.db_connect_key = db_connect_key
        self.db_transaction = db_transaction
        self.db.context = context
        self.redis_config_dict = config.get_value("redis_task")

    #方法扩展请继承此类

class TaskInfo:

    def __init__(self):
        super(TaskInfo, self).__init__()
        self.id = 0  # 标识
        self.app_id = ""  # 应用标识
        self.act_id = 0  # 活动标识
        self.module_id = 0  # 活动模块标识
        self.complete_type = 0  # 完成类型(1-每日任务 2-每周任务 3-持久任务 4-每月任务)
        self.task_name = ""  # 任务名称
        self.task_type = 0  # 任务类型（公共枚举TaskType，业务继承公共枚举进行拓展）
        self.config_json = ""  # 任务配置（json字符串，TaskType里面的注释都有详细例子）
        self.sort_index = 0  # 排序
        self.is_release = 0  # 是否发布
        self.create_date = "1900-01-01 00:00:00"  # 创建时间
        self.modify_date = "1900-01-01 00:00:00"  # 更新时间
        self.route_url = ""  # 路由地址
        self.i1 = 0  # i1
        self.i2 = 0  # i2
        self.s1 = ""  # s1
        self.s2 = ""  # s2

    @classmethod
    def get_field_list(self):
        return ['id', 'app_id', 'act_id', 'module_id', 'complete_type', 'task_name', 'task_type', 'config_json', 'sort_index', 'is_release', 'create_date', 'modify_date', 'route_url', 'i1', 'i2', 's1', 's2']

    @classmethod
    def get_primary_key(self):
        return "id"

    def __str__(self):
        return "task_info_tb"
