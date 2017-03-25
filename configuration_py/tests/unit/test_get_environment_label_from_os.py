from unittest import TestCase

import os

from configuration_py.configuration_py import _get_environment_label_from_os


class TestGetEnvironmentLabelFromOS(TestCase):
    def setUp(self):
        os.environ['ENV'] = os.environ['ENVIRONMENT'] = ''

    def test_should_return_env_value(self):
        os.environ['ENV'] = 'test'
        expected_value = 'test'
        actual_value = _get_environment_label_from_os([])
        self.assertEqual(expected_value, actual_value)

    def test_should_return_environment_value(self):
        os.environ['ENVIRONMENT'] = 'test'
        expected_value = 'test'
        actual_value = _get_environment_label_from_os([])
        self.assertEqual(expected_value, actual_value)

    def test_should_return_environment_value_in_lower_case(self):
        os.environ['ENVIRONMENT'] = 'TEST'
        expected_value = 'test'
        actual_value = _get_environment_label_from_os([])
        self.assertEqual(expected_value, actual_value)

    def test_should_raise_exception_if_no_environment_set(self):
        self.assertRaises(EnvironmentError, _get_environment_label_from_os, [])
