from unittest import TestCase

from configuration_py.configuration_py import _read_config_file
from mock import patch, mock_open


class TestReadConfigFile(TestCase):
    def test_read_config_file_should_return_file_content(self):
        expected_data = "data"
        with patch("__builtin__.open", mock_open(read_data="data")) as mock_file:
            actual_data = _read_config_file('/path/to/config.yaml')

        self.assertEqual(expected_data, actual_data)