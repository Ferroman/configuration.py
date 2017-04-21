import yaml

from configuration_py.parsers.base_parser import BaseConfigParser


class YAMLParser(BaseConfigParser):

    extensions = 'yml', 'yaml'

    def parse(self, file_content, context=None):
        config_dict = yaml.load(file_content)
        if not config_dict or not isinstance(config_dict, dict):
            raise EnvironmentError('Config file does not contain config variables')
        return config_dict
