from unittest import TestCase

from configuration_py.configuration_load import _normalize_environment_label


class TestNormalizeEnvironmentLabel(TestCase):
    def test_normalize_environment_label_should_return_label_for_available_environment(self):
        available_environments = ['production', 'development']
        label = 'development'
        expected_value = label
        actual_value = _normalize_environment_label(label, available_environments)
        self.assertEqual(expected_value, actual_value)

    def test_normalize_environment_label_should_return_label_for_short_development_environment(self):
        available_environments = ['production', 'development']
        label = 'dev'
        expected_value = 'development'
        actual_value = _normalize_environment_label(label, available_environments)
        self.assertEqual(expected_value, actual_value)

    def test_normalize_environment_label_should_return_label_for_short_production_environment(self):
        available_environments = ['production', 'development']
        label = 'prod'
        expected_value = 'production'
        actual_value = _normalize_environment_label(label, available_environments)
        self.assertEqual(expected_value, actual_value)

    def test_normalize_environment_label_should_raise_exception_if_no_such_environment_in_config(self):
        available_environments = ['production']
        label = 'development'
        self.assertRaises(EnvironmentError, _normalize_environment_label, label, available_environments)
