# -*- coding:utf-8 -*-

import os
import time

import rrdtool


def rrd_init_or_update(rrdname, value, step, counter_type, rrd_dir):
    rrdpath = os.path.join(rrd_dir, rrdname)
    if os.path.isfile(rrdpath):
        rrd_update(rrdpath, value)
    else:
        rrd_init(rrdpath, step, counter_type)
        rrd_update(rrdpath, value)


def rrd_init(rrdname, step, counter_type):
    """
    聚合时间根据自己需要
    """
    cur_time = str(int(time.time()))
    # print(rrdname)

    rrd = rrdtool.create(rrdname, '--step', '%s' % (step), '--start', cur_time,
                         'DS:metric:%s:600:0:U' % (counter_type),
                         'RRA:AVERAGE:0.5:1:600',
                         'RRA:AVERAGE:0.5:6:700',
                         'RRA:AVERAGE:0.5:24:775',
                         'RRA:AVERAGE:0.5:288:797',
                         'RRA:MAX:0.5:1:600',
                         'RRA:MAX:0.5:6:700',
                         'RRA:MAX:0.5:24:775',
                         'RRA:MAX:0.5:444:797',
                         'RRA:MIN:0.5:1:600',
                         'RRA:MIN:0.5:6:700',
                         'RRA:MIN:0.5:24:775',
                         'RRA:MIN:0.5:444:797',
                         )

    if rrd:
        print(rrd)


def rrd_update(rrdname, rx):
    start_time = int(time.time())
    print(rrdname, start_time, type(start_time), rx, type(rx))
    x = rrdtool.updatev(rrdname, "%s:%s" % (str(start_time), str(rx)))
    if x:
        print(x)