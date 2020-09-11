import pytest
import allure

from Common.Request import Request
from Conf.Config import ReadConfig
from Params.customer_params import SelectCustomerLostCookie

@allure.feature('客户功能')
class TestLogin():

    conf = ReadConfig()
    request = Request()

    @allure.severity('blocker')
    @allure.story('客户用例')
    def test_select_customer_lost_cookie_01(self):
        """ 查询所有客户缺少cookie """
        allure.dynamic.title("查询所有客户缺少cookie")

        data = SelectCustomerLostCookie()

        host = self.conf.host
        url = data.url[0]
        param = data.data[0]
        headers = data.headers[0]
        api_url = host + url
        response = self.request.request_get(url=api_url,params=param,headers=headers).json()
        allure.attach('{0}'.format(response),'返回的结果')
        assert response['msg'] == "未登录"

    @allure.severity('blocker')
    @allure.story('客户用例')
    def test_select_customer_cookie_02(self, get_cookie):
        """ 查询所有客户携带cookies"""
        allure.dynamic.title("查询所有客户携带cookies")

        data = SelectCustomerLostCookie()

        host = self.conf.host
        url = data.url[0]
        param = data.data[0]
        headers = data.headers[0]
        api_url = host + url
        response = self.request.request_get(url=api_url,params=param,headers=headers, cookies=get_cookie).json()
        allure.attach('{0}'.format(response),'返回的结果')
        assert response['ret'] == 0

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', 'results'])