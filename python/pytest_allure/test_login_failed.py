"""
pytest 要求
1、用例文件名：test_*.py 或者 *_test.py
2、用例：类里面的方法/函数
    一个函数就是一个测试用例，函数名称：test_开头
    函数名：用例名称
    函数体：用例步骤、断言（期望结果与实际结果比对）、测试数据
    断言：assert 表达式（结果为True表示用例通过）

3、前置/后置-fixture
"""

from python.pytest_allure.login import login_check

def test_login_failed_by_failed_user():

    result = login_check("pl","happy")
    assert result == "账号或密码错误"

def test_login_failed_by_failed_password():

    result = login_check("peile","happy1")
    assert result == "账号或密码错误"

def test_login_failed_by_no_user():

    result = login_check(None,"happy")
    assert result == "账户或密码为空"

def test_login_failed_by_no_password():

    result = login_check("peile",None)
    assert result == "账户或密码为空"