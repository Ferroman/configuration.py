import ast

from behave import *
import sure

import configuration_py
from configuration_py.tests.steps_utils import get_config_folder_path


@when('we load "{config_file}" config from folder "{folder}" with context')
def step_impl(context, config_file, folder):
    load_context = context.text
    load_context_dict = ast.literal_eval(load_context)
    context.app_config = configuration_py.load(folder=get_config_folder_path(context, folder), context=load_context_dict)


@step('"{key}" is set to "{value}"')
def step_impl(context, key, value):
    value_string_representation = str(context.app_config.get(key))
    value_string_representation.should.be.equal(value)