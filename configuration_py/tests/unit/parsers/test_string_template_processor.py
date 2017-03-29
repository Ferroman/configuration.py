from unittest import TestCase

import os

from configuration_py.parsers.string_template_processor import ConfigStringTemplateProcessor


class TestConfigStringTemplateProcessor(TestCase):
    def test_should_return_string_of_content_without_changes(self):
        content = "development: variable: True"
        expected_result = content
        actual_result = ConfigStringTemplateProcessor().parse(content)
        self.assertEqual(expected_result, actual_result)

    def test_should_evaluate_variables_from_passed_context(self):
        context = {'debug': True}
        content = "development: variable: $debug"
        expected_result = "development: variable: True"
        actual_result = ConfigStringTemplateProcessor().parse(content, context=context)
        self.assertEqual(expected_result, actual_result)

    def test_should_evaluate_current_environment_variables(self):
        os.environ['DEBUGTEST'] = 'True'
        content = "development: variable: $DEBUGTEST"
        expected_result = "development: variable: True"
        actual_result = ConfigStringTemplateProcessor().parse(content)
        self.assertEqual(expected_result, actual_result)

    def test_should_raise_exception_if_no_variable_passed_but_expected(self):
        content = "development: variable: $NOTEXIST"
        self.assertRaises(EnvironmentError, ConfigStringTemplateProcessor().parse, content)