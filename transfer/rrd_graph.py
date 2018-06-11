# -*- coding:utf-8 -*-

import os
import rrdtool
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

base_dir = os.path.join(BASE_DIR, "rrddatas")
filename = base_dir + '/ansible.node2.com/load_1min.rrd'
print(filename)

# 定义图表上方大标题
title = "Server network  traffic flow (" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ")"
# 重点解释"--x-grid","MINUTE:12:HOUR:1:HOUR:1:0:%H"参数的作用（从左往右进行分解）
"MINUTE:12"  # 表示控制每隔12分钟放置一根次要格线
"HOUR:1"  # 表示控制每隔1小时放置一根主要格线
"HOUR:1"  # 表示控制1个小时输出一个label标签
"0:%H"  # 0表示数字对齐格线，%H表示标签以小时显示
rrdtool.graph("/root/Flow.png", "--start", "-1d", "--vertical-label=Bytes/s",
              "--x-grid", "MINUTE:12:HOUR:1:HOUR:1:0:%H",
              "--width", "650", "--height", "230",
              "DEF:wan_rx=%s:wan_rx:AVERAGE" % (filename),  # 指定网卡入流量数据源DS及CF
              )  # 绘制出流量最小值