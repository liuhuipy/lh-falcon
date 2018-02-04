# -*- coding:utf-8 -*-
import socket
import subprocess

def get_hostname():
    hostname = socket.gethostname()
    return hostname

def get_ipaddress():
    hostname = get_hostname()
    ipaddress = socket.gethostbyname(hostname)
    return ipaddress

def get_version():
    pass

def get_system_uname():
    pass

def get_system_uptime():
    pass

