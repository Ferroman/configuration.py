from string import Template

import os

from configuration_py.parsers.base_parser import BaseConfigParser


class ConfigStringTemplateProcessor(BaseConfigParser):

    extensions = 'tmpl', 'strtmpl'

    def parse(self, file_content, context={}):
        context.update(os.environ)
        try:
            return Template(file_content).substitute(context)
        except KeyError, e:
            raise EnvironmentError(
                'Config try to use {e} variable which does not exists. Pass variable to load context '
                'or set it to the environment.'.format(e=e))