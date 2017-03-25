from unittest import TestCase

from configuration_py.configuration_py import _get_available_config_environments_list


class TestGetAvailableConfigEnvList(TestCase):
    def test_get_available_config_environments_list_should_return_available_envs(self):
        environments = {'dev': {'variable': 'value'}, 'prod': {'variable': 'value'}}
        expected_list = ['prod', 'dev']
        actual_list = _get_available_config_environments_list(environments)
        self.assertEqual(expected_list, actual_list)

    def test_get_available_config_environments_list_should_return_list_without_default(self):
        environments = {'dev': {'variable': 'value'}, 'default': {'variable': 'value'}}
        expected_list = ['dev']
        actual_list = _get_available_config_environments_list(environments)
        self.assertEqual(expected_list, actual_list)