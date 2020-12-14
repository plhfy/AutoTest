# 被测接口

def login_check(user,password):
    if user is not None and password is not None:
        if user == 'peile' and password == 'happy':
            return "正确"
        else:
            return "账号或密码错误"

    else:
        return "账户或密码为空"

