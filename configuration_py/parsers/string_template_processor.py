import os
import string

from configuration_py.parsers.base_parser import BaseConfigParser


class ConfigStringTemplateProcessor(BaseConfigParser):
    extensions = 'tmpl', 'strtmpl'

    def parse(self, file_content, context=None):
        context = dict(context or {}, **os.environ)
        try:
            return string.Template(file_content).substitute(context)
        except KeyError, exc:
            raise EnvironmentError(
                'Config try to use {exc} variable which does not exists. Pass variable to load context '
                'or set it to the environment.'.format(exc=exc))
