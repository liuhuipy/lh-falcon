import os
import time

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from common.models import Host
from transfer.rrdtool_action import rrd_init_or_update


class HostInfoView(APIView):
    permission_classes = []

    def post(self, request):
        data = request.data
        if Host.objects.get(hostname=data['hostname']):
            return HttpResponse('host exist!!', HTTP_200_OK)
        try:
            Host.objects.create(hostname=data['hostname'],
                                ipaddress=data['ipaddress'],
                                macaddress=data['macaddress'],
                                os_type=data['os_type'],
                                os_version=data['os_version'],
                                )
        except:
            return HttpResponse('host create failed!!', HTTP_400_BAD_REQUEST)
        return HttpResponse('host create success!!', HTTP_200_OK)


class ItemDataReportView(APIView):
    permission_classes = []

    def post(self, request):
        data = request.data
        print(data)
        endpoint = data['host']['hostname']
        # print(endpoint)
        # if not Host.objects.get(hostname=data['host']['hostname']):
        # Host.objects.update_or_create(hostname=data['host']['hostname'],
        #                     ipaddress=data['host']['ipaddress'],
        #                     macaddress=data['host']['macaddress'],
        #                     os_type=data['host']['os_type'],
        #                     os_version=data['host']['os_version'],
        #                     )

        base_dir = os.path.join(settings.BASE_DIR, "rrddatas")
        rrd_dir = os.path.join(base_dir, endpoint)
        print(rrd_dir)
        if not os.path.isdir(rrd_dir):
            os.makedirs(rrd_dir)
        for k, v in data['items'].items():
            rrdname = k + '.rrd'
            rrd_init_or_update(rrdname, v['value'], v['step'], v['counterType'], rrd_dir)
        return HttpResponse('insert success!!', HTTP_200_OK)
