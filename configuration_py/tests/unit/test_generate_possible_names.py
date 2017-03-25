from unittest import TestCase

from configuration_py.configuration_py import _generate_possible_names


class TestGeneratePossibleNames(TestCase):
    def test_generate_possible_names_return_name_with_yaml_long_ext_in_it(self):
        expected_value = 'testconfig.yaml'
        actual_value = _generate_possible_names('testconfig')
        self.assertIn(expected_value, actual_value)

    def test_generate_possible_names_return_name_with_yml_short_ext_in_it(self):
        expected_value = 'testconfig.yml'
        actual_value = _generate_possible_names('testconfig')
        self.assertIn(expected_value, actual_value)