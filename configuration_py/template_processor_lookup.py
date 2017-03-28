from template_processors.string_template_processor import ConfigStringTemplateProcessor


def get_supported_extensions():
    return ('tmpl',)


def get_template_processor(extension):
    return ConfigStringTemplateProcessor()