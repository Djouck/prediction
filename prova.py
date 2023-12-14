from datetime import datetime


def add_second(date_object):
    try:
        in_format_time = datetime.strptime(str(date_object), '%Y-%m-%d %H:%M:%S.%f%z')
    except ValueError:
        in_format_time = datetime.strptime(str(date_object), '%Y-%m-%d %H:%M:%S%z')
    result = in_format_time.timestamp() + 1
    result = datetime.fromtimestamp(result)
    return result


print(add_second('2017-01-09 13:48:42.999000+00:00'))
