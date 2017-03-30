import inspect
import os
import pkgutil

import sys

from configuration_py.parsers.base_parser import BaseConfigParser

PARSERS_DIR_NAME = 'parsers'


def get_supported_extensions():
    available_parsers = _lookup_for_available_parsers()
    for parser_class in available_parsers:
        for extension in parser_class.extensions:
            yield extension


def get_parser(extension):
    parser_class = _find_parser_class_by_extension(extension)

    return parser_class()


def _find_parser_class_by_extension(extension):
    available_parsers = _lookup_for_available_parsers()

    for parser_class in available_parsers:
        if extension in parser_class.extensions:
            return parser_class

    raise EnvironmentError('No parsers for {extension} found'.format(extension=extension))


def _lookup_for_available_parsers():
    parsers_folder = _get_parsers_folder_path()
    for importer, package_name, _ in pkgutil.iter_modules([parsers_folder]):
        full_package_name = '%s.%s' % (parsers_folder, package_name)
        if full_package_name not in sys.modules:
            module = importer.find_module(package_name).load_module(package_name)
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, BaseConfigParser) and obj is not BaseConfigParser:
                    yield obj


def _get_parsers_folder_path():
    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_dir_path, PARSERS_DIR_NAME)