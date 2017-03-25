from unittest import TestCase

from configuration_py.configuration_py import _load_yaml_config_by_name
from mock import patch


class TestLoadYAMLConfigByName(TestCase):
    @patch('configuration_py.configuration_py._get_path_to_config_file')
    @patch('configuration_py.configuration_py._read_config_file', return_value='')
    @patch('configuration_py.configuration_py._parse_yaml', return_value='value')
    def test_should_return_parse_yaml_return_value(self, _parse_yaml_mock, _read_config_file_mockget_path_mock, get_path_mock):
        config_name = 'test'
        config_folder = '/config'
        expected_value = 'value'
        actual_value = _load_yaml_config_by_name(config_name, config_folder)
        self.assertEqual(expected_value, actual_value)

    @patch('configuration_py.configuration_py._get_path_to_config_file')
    @patch('configuration_py.configuration_py._read_config_file', return_value='value')
    @patch('configuration_py.configuration_py._parse_yaml')
    def test_should_call_parse_yaml_with_correct_parameters(self, _parse_yaml_mock, _read_config_file_mock, get_path_mock):
        config_name = 'test'
        config_folder = '/config'

        _load_yaml_config_by_name(config_name, config_folder)
        _parse_yaml_mock.assert_called_once_with('value')

    @patch('configuration_py.configuration_py._get_path_to_config_file', return_value='value')
    @patch('configuration_py.configuration_py._read_config_file')
    @patch('configuration_py.configuration_py._parse_yaml')
    def test_should_read_config_file_with_correct_parameters(self, _parse_yaml_mock, _read_config_file_mock, get_path_mock):
        config_name = 'test'
        config_folder = '/config'

        _load_yaml_config_by_name(config_name, config_folder)
        _read_config_file_mock.assert_called_once_with('value')

    @patch('configuration_py.configuration_py._get_path_to_config_file')
    @patch('configuration_py.configuration_py._read_config_file', return_value='')
    @patch('configuration_py.configuration_py._parse_yaml')
    def test_should_call_get_path_to_config_file_with_correct_parameters(self, _parse_yaml_mock, _read_config_file_mock, get_path_mock):
        config_name = 'test'
        config_folder = '/config'
        _load_yaml_config_by_name(config_name, config_folder)
        get_path_mock.assert_called_once_with(config_name, config_folder)