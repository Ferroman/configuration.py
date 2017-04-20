from unittest import TestCase

from mock import patch

from configuration_py.configuration_load import load

# class TestGetAvailableConfigEnvList(TestCase):
# @patch('configuration_py.configuration_py._normalize_environment_label', return_value={'test': ''})
# @patch('configuration_py.configuration_py._get_available_config_environments_list')
# @patch('configuration_py.configuration_py._load_yaml_config_by_name')
# def test_should_call_load_yaml_config_by_name_with_correct_parameters(self, load_mock, available_mock, normalize_mock):
#     config_name = 'test'
#     config_folder = './config'
#     load(config_name, config_name)
#     load_mock.assert_called_once_with(config_name, config_folder)
