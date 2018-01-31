# coding:utf8

import json
import uuid
import socket
import platform


class Host:

    def __init__(self):
        self.hostname = self.get_hostname()
        self.ipaddress = self.get_ipaddress()
        self.macipaddress = self.get_macipaddress()
        self.system_type = self.get_system_type()
        self.system_version = self.get_system_version()
        self.sn = self.get_sn()

    def get_hostname(self):
        """get hostname"""
        hostname = socket.gethostname()
        if hostname is not None:
            return hostname
        else:
            pass

    def get_macipaddress(self):
        """get macipaddress"""
        mac_ip = uuid.UUID(int = uuid.getnode()).hex[-12:]
        if mac_ip is not None:
            return ':'.join([mac_ip[i:i+2] for i in range(0, 11, 2)])
        else:
            pass

    def get_ipaddress(self):
        """get host ipaddress"""
        ipaddress = socket.gethostbyname_ex(socket.gethostname())[-1:]
        if ipaddress is not None:
            return ipaddress
        else:
            pass
    def get_system_type(self):
        """get system type"""
        system_type = platform.system()
        if system_type is not None:
            return system_type
        else:
            pass

    def get_system_version(self):
        """get system version"""
        system_version = platform.version()
        if system_version is not None:
            return system_version
        else:
            pass

    def get_sn(self):
        """get host sn"""
        pass


if __name__ == '__main__':
    host = Host()
    host_dict = {}
    host_dict['hostname'] = host.hostname
    host_dict['ipaddress'] = host.ipaddress
    host_dict['macipaddress'] = host.macipaddress
    host_dict['system_type'] = host.system_type
    host_dict['system_version'] = host.system_version
    print(host_dict)



