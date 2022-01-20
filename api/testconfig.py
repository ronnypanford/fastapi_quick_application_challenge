import configparser
from constants import PATH_TO_API_CFG



class TestConfig:

    def __init__(self):
        self._config = configparser.RawConfigParser()
        self._config.read([PATH_TO_API_CFG])

    def db(self, name):
        return self._config.get('db', name)


