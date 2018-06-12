# -*- coding:utf-8 -*-

import json
import os
import sys
import time
import threading
import schedule
import requests
import configparser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from agent.funcs.cpustat import Cpustat
from agent.funcs.host import Host
from agent.funcs.ifstat import IfStat
from agent.funcs.loadavg import LoadAvg
from agent.funcs.meminfo import Meminfo

config = configparser.ConfigParser()
config.read(BASE_DIR + '/conf/agent.ini')

ITEM_REPORT_URL = config['server']['item_report_api']

INTERVAL_ITEM = int(config['interval']['item'])

HOSTNAME = Host().hostname


def report_item_data(data, url=ITEM_REPORT_URL):
    data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=data, headers=headers)
    print(response.text, response.status_code)


def render_data():
    dic_data = {}
    dic_data['host'] = config_host_routes()

    func_list = [config_cpu_routes(), config_loadavg_routes(), config_mem_routes()]
    dic_data['items'] = {}
    for func in func_list:
        for k, v in func.items():
            item_dic = {
                'value': v,
                'step': INTERVAL_ITEM,
                'counterType': 'GAUGE'
            }
            dic_data['items'][k] = item_dic
    for k, v in  config_ifstat_routes().items():
        item_dic = {
            'value': v,
            'step': INTERVAL_ITEM,
            'counterType': 'COUNTER'
        }
        dic_data['items'][k] = item_dic
    report_item_data(dic_data)


def config_host_routes():
    hostinfo = Host()
    return {
        'hostname': hostinfo.hostname,
        'ipaddress': hostinfo.ipaddress,
        'macaddress': hostinfo.macadddress,
        'os_type': hostinfo.os_type,
        'os_version': hostinfo.os_version,
    }


def config_cpu_routes():
    cpuinfo = Cpustat()
    return {
        'cpu.idle': cpuinfo.cpu_idle,
        'cpu.nice': cpuinfo.cpu_nice,
        'cpu.system': cpuinfo.cpu_system,
        'cpu.user': cpuinfo.cpu_user,
        'cpu.steal': cpuinfo.cpu_steal,
        'cpu.guest': cpuinfo.cpu_guest,
        'cpu.iowait': cpuinfo.cpu_iowait,
        'cpu.irq': cpuinfo.cpu_irq,
        'cpu.softirq': cpuinfo.cpu_softirq,
        'cpu.switches': cpuinfo.cpu_switches,
    }


def config_ifstat_routes():
    ifstat = IfStat()
    if_addrs = list(ifstat.get_if_addrs())
    if 'lo' in if_addrs:
        if_addrs.remove('lo')
    return {
        'net_if_in_sizes': sum([ifstat.get_net_if_in_sizes(addr) for addr in if_addrs]),
        'net_if_in_packets': sum([ifstat.get_net_if_in_packets(addr) for addr in if_addrs]),
        'net_if_in_errors': sum([ifstat.get_net_if_in_errors(addr) for addr in if_addrs]),
        'net_if_in_dropped': sum([ifstat.get_net_if_in_dropped(addr) for addr in if_addrs]),
        'net_if_in_fifo_errs': sum([ifstat.get_net_if_in_fifo_errs(addr) for addr in if_addrs]),
        'net_if_in_frame_errs': sum([ifstat.get_net_if_in_frame_errs(addr) for addr in if_addrs]),
        'net_if_in_compressed_errs': sum([ifstat.get_net_if_in_compressed_errs(addr) for addr in if_addrs]),
        'net_if_in_multicast': sum([ifstat.get_net_if_in_multicast(addr) for addr in if_addrs]),
        'net_if_out_sizes': sum([ifstat.get_net_if_out_sizes(addr) for addr in if_addrs]),
        'net_if_out_packets': sum([ifstat.get_net_if_out_packets(addr) for addr in if_addrs]),
        'net_if_out_errors': sum([ifstat.get_net_if_out_errors(addr) for addr in if_addrs]),
        'net_if_out_dropped': sum([ifstat.get_net_if_out_dropped(addr) for addr in if_addrs]),
        'net_if_out_fifo_errs': sum([ifstat.get_net_if_out_fifo_errs(addr) for addr in if_addrs]),
        'net_if_out_frame_errs': sum([ifstat.get_net_if_out_frame_errs(addr) for addr in if_addrs]),
        'net_if_out_compressed_errs': sum([ifstat.get_net_if_out_compressed_errs(addr) for addr in if_addrs]),
        'net_if_out_multicast': sum([ifstat.get_net_if_out_multicast(addr) for addr in if_addrs]),
        'net_if_total_sizes': sum([ifstat.get_net_if_total_sizes(addr) for addr in if_addrs]),
        'net_if_total_dropped': sum([ifstat.get_net_if_total_dropped(addr) for addr in if_addrs]),
        'net_if_total_errors': sum([ifstat.get_net_if_total_errors(addr) for addr in if_addrs]),
        'net_if_total_packets': sum([ifstat.get_net_if_total_packets(addr) for addr in if_addrs]),
    }


def config_loadavg_routes():
    loadavg = LoadAvg()
    return {
        'load_1min': loadavg.load_1min,
        'load_5min': loadavg.load_5min,
        'load_15min': loadavg.load_15min,
    }


def config_mem_routes():
    meminfo = Meminfo()
    return {
        'mem_memtotal': meminfo.mem_memtotal,
        'mem_memused': meminfo.mem_memused,
        'mem_memused_percent': meminfo.mem_memused_percent,
        'mem_memfree': meminfo.mem_memfree,
        'mem_memfree_percent': meminfo.mem_memfree_percent,
        'mem_swaptotal': meminfo.mem_swaptotal,
        'mem_swapused': meminfo.mem_swapused,
        'mem_swapused_percent': meminfo.mem_swapused_percent,
        'mem_swapfree': meminfo.mem_swapfree,
        'mem_swapfree_percent': meminfo.mem_swapfree_percent,
    }


def run(job_func):
    job_sched = threading.Thread(target=job_func)
    job_sched.start()


def main():
    print("###################### The lh-falcon agent is starting!!! #######################")
    # print(render_data())

    schedule.every(INTERVAL_ITEM).seconds.do(run, render_data)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
