from string import Template

from configuration_py.template_processors.base_processor import BaseConfigTemplateProcessor


class ConfigStringTemplateProcessor(BaseConfigTemplateProcessor):

    @property
    def extensions(self):
        return 'tmpl', 'strtmpl'

    def parse(self, file_content, context={}):
        return Template(file_content).substitute(context)

