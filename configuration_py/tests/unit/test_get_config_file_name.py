from unittest import TestCase

from configuration_py.configuration_py import _get_config_file_name


class TestGetConfigFileName(TestCase):
    def test_get_config_file_return_name_with_yaml_ext_by_default(self):
        expected_value = 'testconfig.yaml'
        actual_value = _get_config_file_name('testconfig')
        self.assertEqual(expected_value, actual_value)

    def test_get_config_file_use_passed_extension(self):
        expected_value = 'testconfig.ini'
        actual_value = _get_config_file_name('testconfig', 'ini')
        self.assertEqual(expected_value, actual_value)

    def test_get_config_file_should_raised_exception_when_empty_name_given(self):
        self.assertRaises(ValueError, _get_config_file_name, '', 'ini')

    def test_get_config_file_should_raised_exception_when_empty_extension_provided(self):
        self.assertRaises(ValueError, _get_config_file_name, 'testname', '')