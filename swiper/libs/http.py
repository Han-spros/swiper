from json import dumps

from django.http import HttpResponse


def render_json(data = None, error_code = 0):
    """数据返回改为json格式"""
    result = {
        'data' : data,
        'code' : error_code
    }
    
    json_str = dumps(result, ensure_ascii=False, separators=[',',':'])
    return HttpResponse(json_str)