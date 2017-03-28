import os

import parser_lookup
import template_processor_lookup

DEFAULT_CONFIGS_FOLDER = './config'
DEV_SHORTCUTS_LIST = ['dev']
PRODUCTION_SHORTCUTS_LIST = ['prod']


def _generate_possible_config_file_names(config_name):
    supported_parser_extensions = parser_lookup.get_supported_extensions()
    supported_template_processor_extensions = template_processor_lookup.get_supported_extensions()

    for config_extension in supported_parser_extensions:
        yield "{config_name}.{config_extension}".format(config_name=config_name, config_extension=config_extension)

        for parser_extension in supported_template_processor_extensions:
            yield "{config_name}.{config_extension}.{parser_extension}"\
                .format(config_name=config_name,
                        config_extension=config_extension,
                        parser_extension=parser_extension)


def _generate_possible_paths_to_config(config_name, config_folder):
    for file_name in _generate_possible_config_file_names(config_name):
        if not config_folder.startswith(os.pathsep):
            yield os.path.join(os.getcwd(), config_folder, file_name)
        else:
            yield os.path.join(config_folder, file_name)


def _find_existing_config_file(config_name, config_folder):
    for path in _generate_possible_paths_to_config(config_name, config_folder):
        if os.path.exists(path):
            yield path


def _get_path_to_config_file(config_name, config_folder):
    existed_paths = list(_find_existing_config_file(config_name, config_folder))

    if len(existed_paths) == 0:
        raise IOError("No any of config files for '{file_names}' found in '{config_folder}' folder" \
                      .format(file_names=config_name, config_folder=config_folder))
    if len(existed_paths) > 1:
        raise EnvironmentError(
            "Found more than one config file for '{config_name}' found in '{config_folder}': {existed_paths}".format(
                config_name=config_name,
                config_folder=config_folder,
                existed_paths=existed_paths))

    return existed_paths[0]


def _read_config_file(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content


def _get_environment_label_from_os(available_config_environments):
    environment_value = os.environ.get('ENV') or os.environ.get('ENVIRONMENT')

    if environment_value:
        return environment_value.lower()
    else:
        raise EnvironmentError("Current environment for application does not set. To set environment, set one of the " \
                               "available environments ({available_environments}) to ENV or ENVIRONMENT system " \
                               "variable or provide it directly to the 'load' function." \
                               .format(available_environments=available_config_environments))


def _normalize_environment_label(label, available_config_environments):
    if label in DEV_SHORTCUTS_LIST:
        label = 'development'

    if label in PRODUCTION_SHORTCUTS_LIST:
        label = 'production'

    if label not in available_config_environments:
        raise EnvironmentError("There is no configuration for given environment '{label}'. Please, provide " \
                               "configuration section for this environment in config file " \
                               .format(label=label))

    return label


def _get_available_config_environments_list(config):
    available_config_environments_list = list(config)

    if 'default' in available_config_environments_list:
        available_config_environments_list.remove('default')

    return available_config_environments_list


def get_handler(extension):
    handler = parser_lookup.get_parser(extension)

    if not handler:
        return template_processor_lookup.get_template_processor(extension)

    return handler


def _load_config_from_file(path_to_config_file, context):
    extensions = ['tmpl', 'yaml']

    content = _read_config_file(path_to_config_file)

    for extension in extensions:
        handler = get_handler(extension)
        content = handler.parse(content, context)

    return content


def _load_config_by_name(configuration, config_folder, context):
    path_to_config_file = _get_path_to_config_file(configuration, config_folder)
    return _load_config_from_file(path_to_config_file, context)


def load(configuration='application', environment=None, folder=None, context={}):
    config_folder = folder or DEFAULT_CONFIGS_FOLDER

    config = _load_config_by_name(configuration, config_folder, context)
    available_config_environments = _get_available_config_environments_list(config)

    environment_label = environment or _get_environment_label_from_os(available_config_environments)
    environment_label = _normalize_environment_label(environment_label, available_config_environments)

    current_configuration = {'environment': environment_label}

    current_configuration.update(config[environment_label])
    return current_configuration
