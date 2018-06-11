# -*- coding:utf-8 -*-

import rrdtool
import time

def main():
	title = "load 1min data (" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ")"
	name = "/Users/liuhui/PycharmProjects/lh-falcon/rrddatas/ansible.node2.com/net_if_in_sizes.rrd"
	rrdtool.graph('Flow.png', '--start', '-1h', '--vertical-label=Bytes/s',
		          '--x-grid', 'MINUTE:12:HOUR:1:HOUR:1:0:%H',
		          '--width', '750', '--height', '300', '--title', title,
		          'DEF:metric=%s:metric:AVERAGE' % (name),
		          # 'DEF:outoctets=%s:eth0_out:AVERAGE' % (name),
		          'AREA:metric#00FF00:load 1min',
		          # 'LINE1:outoctets#0000FF:Out traffic',
		          'HRULE:190#FF0000:Load value\\r',
		          'CDEF:data=metric,8,*',
		          # 'CDEF:outbits=outoctets,8,*',
		          'COMMENT:\\r',
		          )

