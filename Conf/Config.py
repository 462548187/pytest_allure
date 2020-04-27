from configparser import ConfigParser
import os

class ReadConfig():
    # 标题
    title = 'private_debug'

    # 值
    tester = 'tester'
    host = 'host'

    def __init__(self):
        self.config_file = os.path.dirname(__file__) + '/config.ini'
        self.config = ConfigParser()
        self.config.read(self.config_file)

        self.tester = self.get_config(self.title, self.tester)
        self.host = self.get_config(self.title, self.host)

    def get_config(self,title, value):
        value = self.config.get(title, value)
        return value




if __name__ == '__main__':
    test = ReadConfig()
    print(test.host)



