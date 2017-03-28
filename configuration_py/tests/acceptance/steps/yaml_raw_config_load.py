import os

from behave import *
import sure

import configuration_py
from configuration_py.tests.steps_utils import create_config_folder, get_config_folder_path


@given('we have "{config_file}" config in "{folder}" folder with the content')
def step_impl(context, config_file, folder):
    configuration = context.text
    config_folder_path = create_config_folder(context, folder)
    path_to_config_file = os.path.join(config_folder_path, config_file)

    with open(path_to_config_file, 'w') as config_file:
        config_file.write(configuration)


@step('environment set to "{environment}"')
def step_impl(context, environment):
    os.environ['ENVIRONMENT'] = environment


@when('we load default config from folder "{folder}"')
def step_impl(context, folder):
    context.app_config = configuration_py.load(folder=get_config_folder_path(context, folder))


@when('we load "{config_name}" config from folder "{folder}"')
def step_impl(context, config_name, folder):
    context.app_config = configuration_py.load(config_name, folder=get_config_folder_path(context, folder))


@then('"{environment}" configuration loaded')
def step_impl(context, environment):
    (context.app_config.get('environment')).should.be.equal(environment)


@when('we load "{config_name}" config from folder "{folder}" with "{environment}" environment')
def step_impl(context, config_name, folder, environment):
    context.app_config = configuration_py.load(config_name, environment=environment,
                                               folder=get_config_folder_path(context, folder))


@step("it should looks like dictionary")
def step_impl(context):
    context.app_config.should.be.a('dict')