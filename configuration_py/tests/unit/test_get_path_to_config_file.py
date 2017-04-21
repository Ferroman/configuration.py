from unittest import TestCase

from configuration_py.configuration_load import _get_path_to_config_file
from mock import patch


class TestGetPathToConfigFile(TestCase):
    @patch('configuration_py.configuration_load._find_existing_config_file', return_value=['/path/to/config/test.yaml'])
    def test_should_return_path_directory_with_file(self, mock):
        config_name = 'test'
        config_folder = 'config'
        expected_value = "/path/to/config/test.yaml"

        actual_value = _get_path_to_config_file(config_name, config_folder)

        self.assertEqual(expected_value, actual_value)

    @patch('configuration_py.configuration_load._find_existing_config_file', return_value=['/path/to/config/test.yaml'])
    def test_call_get_paths_existed_file_with_the_right_parameters(self, mock):
        config_name = 'test'
        config_folder = 'config'

        _get_path_to_config_file(config_name, config_folder)

        mock.assert_called_once_with(config_name, config_folder)

    @patch('configuration_py.configuration_load._find_existing_config_file', return_value=[])
    def test_should_raise_exception_if_no_files_found(self, mock):

        self.assertRaises(IOError, _get_path_to_config_file, 'test', 'config')

    @patch('configuration_py.configuration_load._find_existing_config_file', return_value=['/path/test.yaml', '/path/test.yml'])
    def test_should_raise_exception_if_more_than_one_config_found(self, mock):

        self.assertRaises(EnvironmentError, _get_path_to_config_file, 'test', 'config')
