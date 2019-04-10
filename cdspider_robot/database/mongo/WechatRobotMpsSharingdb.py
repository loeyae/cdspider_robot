#-*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"),
# see LICENSE for more details: http://www.apache.org/licenses/LICENSE-2.0.

"""
:author:  Zhang Yi <loeyae@gmail.com>
:date:    2018-8-4 21:43:09
"""
import time
import pymongo
from cdspider.database.base import WechatRobotMpsSharingDB as BaseWechatRobotMpsSharingDB
from .Mongo import Mongo

class WechatRobotMpsSharingDB(Mongo, BaseWechatRobotMpsSharingDB):
    """
    wechat_robot_mps_sharing data object
    """
    __tablename__ = 'wechat_robot_mps_sharing'

    def __init__(self, connector, table=None, **kwargs):
        super(WechatRobotMpsSharingDB, self).__init__(connector, table = table, **kwargs)
        collection = self._db.get_collection(self.table)
        indexes = collection.index_information()
        if not 'IUin' in indexes:
            collection.create_index('IUin', name='IUin')
        if not 'ctime' in indexes:
            collection.create_index('ctime', name='ctime')

    def insert(self, obj = {}):
        obj.setdefault('ctime', int(time.time()))
        super(WechatRobotMpsSharingDB, self).insert(setting=obj)
        return obj['MsgId']
