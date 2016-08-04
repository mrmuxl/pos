#!/usr/bin/env python2
#-*- coding: utf-8 -*

import uuid,random,time

def get_order_id():
    uid = str(uuid.UUID.get_time_low(uuid.uuid1()))
    if len(uid) < 10:
        d = 10 - len(uid)
        for i in range(d):
            r = random.randint(0,9)
            uid = uid + str(r)
    order_id = time.strftime("%Y%m%d") + uid
    return order_id

