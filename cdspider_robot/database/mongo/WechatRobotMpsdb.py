#-*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"),
# see LICENSE for more details: http://www.apache.org/licenses/LICENSE-2.0.

"""
:author:  Zhang Yi <loeyae@gmail.com>
:date:    2018-8-4 21:43:09
"""
import time
import pymongo
from ..base import WechatRobotMpsDB as BaseWechatRobotMpsDB
from cdspider.database.mongo import Mongo

class WechatRobotMpsDB(Mongo, BaseWechatRobotMpsDB):
    """
    wechat_robot_mps data object
    """
    __tablename__ = 'wechat_robot_mps'

    def __init__(self, connector, table=None, **kwargs):
        super(WechatRobotMpsDB, self).__init__(connector, table = table, **kwargs)
        collection = self._db.get_collection(self.table)
        indexes = collection.index_information()
        if 'IUin' not  in indexes:
            collection.create_index('IUin', name='IUin')
        if 'UserName' not  in indexes:
            collection.create_index('UserName', name='UserName')
        if 'NickName' not  in indexes:
            collection.create_index([('NickName', pymongo.TEXT)], name='NickName')
        if 'ctime' not  in indexes:
            collection.create_index('ctime', name='ctime')

    def insert(self, obj = {}):
        obj.setdefault('ctime', int(time.time()))
        super(WechatRobotMpsDB, self).insert(setting=obj)
        return obj['UserName']

    def delete_by_iuin(self, uin):
        where = {"IUin": uin}
        super(WechatRobotMpsDB, self).delete(where=where, multi=True)
