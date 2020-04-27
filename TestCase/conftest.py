import pytest
import allure

from Conf.Config import ReadConfig

@pytest.fixture()
def action():
    # 定义环境
    env = 'debug'
    # 定义报告中的environment
    conf = ReadConfig()
    host = conf.get_config('private_debug', 'host')
    tester = conf.get_config('private_debug', 'tester')
    allure.environment(environment=env)
    allure.environment(hostname=host)
    allure.environment(tester=tester)
    return env

