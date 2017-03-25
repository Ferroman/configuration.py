from unittest import TestCase

from configuration_py.configuration_py import _get_path_to_config_file
from mock import MagicMock, patch


class TestGetPathToConfigFile(TestCase):
    def test_get_path_to_config_file_should_return_path_directory_with_file(self):
        file_name = 'config.yaml'
        config_folder = 'config'
        expected_value = "/path/to/config/config.yaml"

        mock = MagicMock(return_value=['/path/to/config/config.yaml'])

        with patch('configuration_py.configuration_py._get_paths_existed_file', mock):
            actual_value = _get_path_to_config_file(file_name, config_folder)

        self.assertEqual(expected_value, actual_value)