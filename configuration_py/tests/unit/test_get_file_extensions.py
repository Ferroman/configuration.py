from unittest import TestCase

from configuration_py.configuration_py import _get_file_extensions


class TestGetFileExtensions(TestCase):
    def test_should_return_list_of_extensions_for_given_path_to_file(self):
        file_path = '/path/to/config/file.yaml.tmpl'
        expected_value = ['yaml', 'tmpl']
        actual_value = _get_file_extensions(file_path)

        self.assertEqual(actual_value, expected_value)

    def test_should_return_list_of_extensions_for_windows_path(self):
        file_path = 'C:\\path\\to\\config\\file.yaml.tmpl'
        expected_value = ['yaml', 'tmpl']
        actual_value = _get_file_extensions(file_path)

        self.assertEqual(actual_value, expected_value)

    def test_should_return_list_of_extensions_for_file_name(self):
        file_path = 'config/file.yaml.tmpl'
        expected_value = ['yaml', 'tmpl']
        actual_value = _get_file_extensions(file_path)

        self.assertEqual(actual_value, expected_value)

    def test_should_return_list_of_extensions_for_file_name_with_one_extension(self):
        file_path = 'config/file.yaml'
        expected_value = ['yaml']
        actual_value = _get_file_extensions(file_path)

        self.assertEqual(actual_value, expected_value)

    def test_should_return_empty_list_for_file_name_without_extension(self):
        file_path = 'config/file'
        expected_value = []
        actual_value = _get_file_extensions(file_path)

        self.assertEqual(actual_value, expected_value)

    def test_should_return_empty_list_for_empty_file_path(self):
        file_path = ''
        expected_value = []
        actual_value = _get_file_extensions(file_path)

        self.assertEqual(actual_value, expected_value)
