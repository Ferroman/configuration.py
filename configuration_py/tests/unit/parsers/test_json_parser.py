from unittest import TestCase

from configuration_py.parsers.json_parser import JSONParser


class TestParseJSON(TestCase):
    def test_should_return_dict_of_parsed_yaml_content(self):
        content = '''{ "development": {
                           "variable": true
                         }
                      }
                  '''
        expected_result = {'development': {'variable': True}}
        actual_result = JSONParser().parse(content)
        self.assertDictEqual(expected_result, actual_result)

    def test_should_raise_exception_if_no_content_provided(self):
        content = ""
        self.assertRaises(ValueError, JSONParser().parse, content)
