import json

from configuration_py.parsers.base_parser import BaseConfigParser


class JSONParser(BaseConfigParser):

    extensions = ('json', )

    def parse(self, file_content, context={}):
        config_dict = json.loads(file_content)

        if not config_dict or type(config_dict) is not dict:
            raise EnvironmentError('Config file does not contain config variables')
        return config_dict
