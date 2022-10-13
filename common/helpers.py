import json
import time
from datetime import datetime, timedelta

import requests
from django.utils import timezone
from rest_framework.pagination import LimitOffsetPagination


def get_paginated_qs(queryset, request, limit=10):
    paginator = LimitOffsetPagination()
    paginator.max_limit = 50
    paginator.default_limit = limit
    paginator.offset = 0

    pg_qs = paginator.paginate_queryset(
        queryset,
        request
    )

    next_link = paginator.get_next_link()
    prev_link = paginator.get_previous_link()
    if next_link:
        next_link = next_link.split('?')[1]
    if prev_link:
        prev_link = prev_link.split('?')[1]

    data = {
        'qs': pg_qs,
        'limit': paginator.limit,
        'offset': paginator.offset,
        'count': paginator.count,
        'next': next_link,
        'prev': prev_link,
    }

    # print(json.dumps(data))

    return data


def get_paginated(queryset, request, to_dict, limit=10):
    paginator = LimitOffsetPagination()
    paginator.max_limit = 50
    paginator.default_limit = limit
    paginator.offset = 0

    obj_list = paginator.paginate_queryset(
        queryset,
        request
    )

    results = to_dict(obj_list)

    next_link = paginator.get_next_link()
    prev_link = paginator.get_previous_link()
    if next_link:
        next_link = next_link.split('?')[1]
    if prev_link:
        prev_link = prev_link.split('?')[1]

    data = {
        'results': results,
        'limit': paginator.limit,
        'offset': paginator.offset,
        'count': paginator.count,
        'next': next_link,
        'prev': prev_link,
    }

    # print(json.dumps(data))

    return data


SMS_GATEWAY_USERNAME = 'info@dingi.com'
SMS_GATEWAY_PASSWORD = '321dingi% )'
SMS_GATEWAY_FORMAT = '%Y-%m-%d %H:%M:%S'
SMS_GATEWAY_URL = 'http://api.infobuzzer.net/v3.1/SendSMS/sendSmsInfoStore'


def send_message_jhorotech(phone_no, sms_text):
    unix_time = int(time.time())
    cu_time = (datetime.now(timezone.utc) + timedelta(seconds=10) + timedelta(hours=6)).strftime(
        SMS_GATEWAY_FORMAT
    )
    phone = phone_no
    if phone_no is not None:
        data = {
            "trxID": str(unix_time),
            "trxTime": str(unix_time),
            "smsDatumArray": [
                {
                    "smsID": str(unix_time),
                    "smsSendTime": cu_time,
                    "mask": "No Mask",
                    "mobileNo": phone,
                    "smsBody": sms_text,
                }
            ],
        }
    resp = requests.post(
        SMS_GATEWAY_URL,
        data=json.dumps(data),
        auth=(SMS_GATEWAY_USERNAME, SMS_GATEWAY_PASSWORD),
    )
    return resp
