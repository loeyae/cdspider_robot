#-*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"),
# see LICENSE for more details: http://www.apache.org/licenses/LICENSE-2.0.

"""
:author:  Zhang Yi <loeyae@gmail.com>
:date:    2018-8-4 21:43:09
"""

from cdspider.database.base import Base

{
    "wechat_robot_chat_info": {
        "IUin": int,
        "MsgId" : str,
        "FromUserName" : str,
        "ToUserName" : str,
        "MsgType" : int,
        "Content" : str,
        "Type": str,
        "Text": str,
        "User": {
            "Uin" : int,
            "UserName" : str,
            "NickName" : str,
            "HeadImgUrl" : str,
            "ContactFlag" : int,
            "MemberCount" : int,
            "RemarkName" : str,
            "HideInputBarFlag" : int,
            "Sex" : int,
            "Signature" : str,
        },
    }
}

class WechatRobotChatInfoDB(Base):
    """
    wechat_robot_chat_info data object
    """

    def insert(self, obj = {}):
        raise NotImplementedError

    def update(self, id, obj = {}):
        raise NotImplementedError

    def delete(self, id):
        raise NotImplementedError
