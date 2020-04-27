import pytest
import allure

from Common.Request import Request
from Conf.Config import ReadConfig
from Params.params import AddEvent,SelectEvent,DeleteEvent

@allure.feature('发布会功能')
class TestEevent():

    @allure.severity('blocker')
    @allure.story('添加发布会')
    def test_add_event_01(self):
        """ 添加发布会 """
        conf = ReadConfig()
        data = AddEvent()
        request = Request()

        host = conf.host
        url = data.url[0]
        params = data.data[0]
        headers = data.headers[0]
        api_url = host + url
        response = request.request_post(url=api_url,data=params,headers=headers).json()
        allure.attach('{0}'.format(response),'返回的结果')
        assert response['status'] == 200


    @allure.severity('blocker')
    @allure.story('查询所有发布会')
    def test_select_event_02(self):
        """ 查询所有发布会 """
        global event_id
        conf = ReadConfig()
        data = SelectEvent()
        request = Request()

        host = conf.host
        url = data.url[0]
        params = data.data[0]
        headers = data.headers[0]
        api_url = host + url
        response = request.request_get(url=api_url,params=params,headers=headers).json()
        event_id = response['data'][-1]['id']
        allure.attach('{0}'.format(response), '返回的结果')
        assert response['status'] == 200


    @allure.severity('blocker')
    @allure.story('删除发布会')
    def test_delete_event_03(self):
        """ 删除发布会 """
        conf = ReadConfig()
        data = DeleteEvent()
        request = Request()

        host = conf.host
        url = data.url[0]
        params = data.data[0]
        headers = data.headers[0]
        api_url = host + url
        params['event_id'] = event_id
        response = request.request_post(url=api_url,data=params,headers=headers).json()
        allure.attach('{0}'.format(response), '返回的结果')
        assert response['status'] == 200

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', 'results'])