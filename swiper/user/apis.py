import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.

from common import errors
from common.utils import is_phone_num
from libs.http import render_json


def verify_phone(request):
    """
    验证手机号码
    生成验证码
    保存验证码
    发送
    """
    phone_num = request.POST.get('phone_num')

    if is_phone_num(phone_num):
        # 号码格式正确
        return render_json()
    else:
        return render_json(code=errors.PHONE_NUM_ERR)