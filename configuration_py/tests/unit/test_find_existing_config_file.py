from unittest import TestCase

from mock import patch

from configuration_py.configuration_load import _find_existing_config_file


class TestGetPathsExistedFile(TestCase):
    @patch('configuration_py.configuration_load._generate_possible_paths_to_config')
    def test_should_call_generate_possible_paths_to_config_with_the_correct_parameters(self, mock):
        list(_find_existing_config_file('testconfig', '/config'))
        mock.assert_called_once_with('testconfig', '/config')

    @patch('os.path.exists', return_value=True)
    def test_should_return_path_if_it_exists(self, mock):
        expected_value = '/config/testconfig.yaml'
        paths = _find_existing_config_file('testconfig', '/config')
        self.assertIn(expected_value, paths)
