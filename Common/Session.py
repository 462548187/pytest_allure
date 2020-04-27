import json
import requests

from Conf.Config import ReadConfig



class Session():

    def __init__(self):
        self.read_config = ReadConfig()

    def get_session(self):

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                                 "(KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
                   "Content-Type": "application/x-www-form-urlencoded"}

        url = self.read_config.get_config('private_debug', 'loginHost')
        data = json.loads(self.read_config.get_config('private_debug', 'loginInfo'))

        session_debug = requests.session()
        res = session_debug.post(url,data,headers)
        cookie = res.cookies.get_dict()
        return cookie

if __name__ == '__main__':
    test = Session()
    a = test.get_session()
    print(a)