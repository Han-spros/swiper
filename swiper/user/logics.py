from common import utils
from libs import sms


def send_verify_code(phone_num):
    """发送验证码逻辑
    :params phone_num: 手机号码
    :return:
    """

    code = utils.gen_rendom_code(6)
    #生成验证码
    sms.send_verify_code(phone_num, code)
    #发送验证码
    return True