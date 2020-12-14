
from python.pytest_allure.login import login_check

def test_login_success():

    result = login_check("peile","happy")
    assert result == "正确"