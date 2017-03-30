from unittest import TestCase

import os

from mock import patch

from configuration_py.configuration_load import _generate_possible_paths_to_config


class TestGeneratePossiblePathsToConfig(TestCase):
    @patch('configuration_py.configuration_load._generate_possible_config_file_names', return_value=['testconfig.yaml'])
    def test_return_relative_paths_for_relative_config_folder_path(self, mock):
        expected_path = os.getcwd()

        paths = _generate_possible_paths_to_config('testconfig', 'config')

        self.assertTrue(all(path.startswith(expected_path) for path in paths))

    @patch('configuration_py.configuration_load._generate_possible_config_file_names', return_value=['testconfig.yaml'])
    def test_return_absolute_paths_for_absolute_config_folder_path(self, mock):
        expected_path = '/config'

        paths = _generate_possible_paths_to_config('testconfig', '/config')

        self.assertTrue(all(path.startswith(expected_path) for path in paths))

    @patch('configuration_py.configuration_load._generate_possible_config_file_names', return_value=['testconfig.yaml'])
    def test_should_call_get_paths_existed_file_with_the_correct_parameters(self, mock):

        list(_generate_possible_paths_to_config('testconfig', '/config'))
        mock.assert_called_once_with('testconfig')
