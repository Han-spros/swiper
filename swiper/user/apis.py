from common import errors
from common.utils import is_phone_num
from libs.http import render_json
from user import logics

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
        if logics.send_verify_code(phone_num):
            # 验证码生成发送
            return render_json()
        else:
            return render_json(code = errors.SMS_SEND_ERR)
            # 返回错误码
    else:
        return render_json(code=errors.PHONE_NUM_ERR)
        # 返回错误码