# -*- coding: utf-8 -*-

import uuid
import socket
import platform


class Host:
    """get host information to padding host model"""
    def __init__(self):
        self.hostname = self.get_hostname()
        self.ipaddress = self.get_ipaddress()
        self.macadddress = self.get_macipaddress()
        self.os_type = self.get_os_type()
        self.os_version = self.get_os_version()

    def get_hostname(self):
        """get hostname"""
        return socket.getfqdn(socket.gethostname())

    def get_macipaddress(self):
        """get macipaddress"""
        mac_ip = uuid.UUID(int = uuid.getnode()).hex[-12:]
        return ':'.join([mac_ip[i:i+2] for i in range(0, 11, 2)])

    def get_ipaddress(self):
        """get host ipaddress"""
        return socket.gethostbyname(self.hostname)

    def get_os_type(self):
        """get system type"""
        return platform.system()

    def get_os_version(self):
        """get system version"""
        return platform.version()






