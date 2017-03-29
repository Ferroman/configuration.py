from unittest import TestCase

from configuration_py.parsers.yaml_parser import YAMLParser


class TestParseYAML(TestCase):
    def test_should_return_dict_of_parsed_yaml_content(self):
        content = """ development:
                        variable: True
                  """
        expected_result = {'development': {'variable': True}}
        actual_result = YAMLParser().parse(content)
        self.assertDictEqual(expected_result, actual_result)

    def test_should_raise_exception_if_no_environment_variables_provided(self):
        content = """ development """
        self.assertRaises(EnvironmentError, YAMLParser().parse, content)

    def test_should_raise_exception_if_no_content_provided(self):
        content = ""
        self.assertRaises(EnvironmentError, YAMLParser().parse, content)
