from unittest import TestCase

from configuration_py.configuration_py import _parse_yaml


class TestParseYAML(TestCase):
    def test_parse_yaml_should_return_dict_of_parsed_yaml_content(self):
        content = """ development:
                        variable: True"""
        expected_result = {'development': {'variable': True}}
        actual_result = _parse_yaml(content)
        self.assertDictEqual(expected_result, actual_result)

    def test_parse_yaml_should_raise_exception_if_no_environment_variables_provided(self):
        content = """ development """
        self.assertRaises(EnvironmentError, _parse_yaml, content)

    def test_parse_yaml_should_raise_exception_if_no_content_provided(self):
        content = ""
        self.assertRaises(EnvironmentError, _parse_yaml, content)
