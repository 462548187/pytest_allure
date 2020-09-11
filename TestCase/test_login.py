import pytest
import allure

from Common.Request import Request
from Conf.Config import ReadConfig
from Params.login_params import LoginSucess,LoginPasswordError,LoginPasswordNull,LoginPasswordMiss

@allure.feature('登录功能')
class TestLogin():

    conf = ReadConfig()
    request = Request()

    @allure.severity('blocker')
    @allure.story('登录用例')
    def test_success_login_01(self):
        """ 登录成功 """
        allure.dynamic.title("登录成功")

        data = LoginSucess()

        host = self.conf.host
        url = data.url[0]
        params = data.data[0]
        headers = data.headers[0]
        api_url = host + url
        response = self.request.request_post(url=api_url,data=params,headers=headers).json()
        allure.attach('{0}'.format(response),'返回的结果')
        assert response['ret'] == 0

    @allure.severity('blocker')
    @allure.story('登录用例')
    def test_password_error_login_02(self):
        """ 登录密码错误 """
        allure.dynamic.title("登录密码错误")

        data = LoginPasswordError()

        host = self.conf.host
        url = data.url[0]
        params = data.data[0]
        headers = data.headers[0]
        api_url = host + url
        response = self.request.request_post(url=api_url,data=params,headers=headers).json()
        allure.attach('{0}'.format(response),'返回的结果')
        assert response['msg'] == "用户名或密码错误"

    @allure.severity('blocker')
    @allure.story('登录用例')
    def test_password_null_login_03(self):
        """ 登录密码错误 """
        allure.dynamic.title("登录密码为空")

        data = LoginPasswordNull()

        host = self.conf.host
        url = data.url[0]
        params = data.data[0]
        headers = data.headers[0]
        api_url = host + url
        response = self.request.request_post(url=api_url,data=params,headers=headers).json()
        allure.attach('{0}'.format(response),'返回的结果')
        assert response['msg'] == "用户名或密码错误"

    @allure.severity('blocker')
    @allure.story('登录用例')
    def test_password_miss_login_04(self):
        """ 登录密码错误 """
        allure.dynamic.title("缺少登录密码")

        data = LoginPasswordMiss()

        host = self.conf.host
        url = data.url[0]
        params = data.data[0]
        headers = data.headers[0]
        api_url = host + url
        response = self.request.request_post(url=api_url,data=params,headers=headers).json()
        allure.attach('{0}'.format(response),'返回的结果')
        assert response['msg'] == "用户名或密码错误"

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', 'results'])