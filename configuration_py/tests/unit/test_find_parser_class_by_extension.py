from unittest import TestCase

from mock import patch, MagicMock

from configuration_py.parser_lookup import _find_parser_class_by_extension


class TestFindParserClassByExtension(TestCase):
    @patch('configuration_py.parser_lookup._lookup_for_available_parsers')
    def test_should_return_parser_class_when_extension_supported(self, mock):
        parser_class_mock = MagicMock()
        parser_class_mock.extensions = ('yaml',)
        mock.return_value = [parser_class_mock]

        expected_value = parser_class_mock
        actual_value = _find_parser_class_by_extension('yaml')
        self.assertEqual(actual_value, expected_value)

    @patch('configuration_py.parser_lookup._lookup_for_available_parsers')
    def test_should_raise_exceptions_when_parsers_class_support_extension(self, mock):
        parser_class_mock = MagicMock()
        parser_class_mock.extensions = ('yaml',)
        mock.return_value = [parser_class_mock]

        self.assertRaises(EnvironmentError, _find_parser_class_by_extension, 'json')
