from string import Template

from configuration_py.parsers.base_parser import BaseConfigParser


class ConfigStringTemplateProcessor(BaseConfigParser):

    extensions = 'tmpl', 'strtmpl'

    def parse(self, file_content, context={}):
        return Template(file_content).substitute(context)

