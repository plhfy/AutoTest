
import pytest


if __name__ == '__main__':
    #pytest.main()  #执行pytest命令，收集用例，然后执行用例。当前所在的目录是rootdir
    pytest.main(["--alluredir=./allure_use_testfile"])
