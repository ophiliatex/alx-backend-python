#!/usr/bin/env python3
"""
Test cases for the utils module
"""
import unittest
from unittest.mock import patch, MagicMock

from parameterized import parameterized, parameterized_class

utils = __import__("utils")
access_nested_map = utils.access_nested_map
get_json = utils.get_json
memoize = utils.memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for the utils module
    """

    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, mapping, path, expected_value):
        self.assertEqual(access_nested_map(mapping, path), expected_value)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, mapping, path, expected_exception):
        with self.assertRaises(expected_exception):
            access_nested_map(mapping, path)


class TestGetJson(unittest.TestCase):
    """
    Test cases for the utils module
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test cases for the utils module
    """

    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_method):
        """
        Test the memoize decorator
        Returns
        -------
        """

        test_instance = self.TestClass()

        result = test_instance.a_property
        result2 = test_instance.a_property

        self.assertEqual(result, 42)
        self.assertEqual(result2, 42)

        mock_method.assert_called_once()
