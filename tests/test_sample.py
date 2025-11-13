"""Sample test file to verify test infrastructure."""

import pytest


def test_basic_assertion():
    """Test basic assertion."""
    assert True


def test_addition():
    """Test basic arithmetic."""
    assert 1 + 1 == 2


def test_string_operations():
    """Test string operations."""
    result = "hello".upper()
    assert result == "HELLO"


class TestSampleClass:
    """Sample test class."""

    def test_list_operations(self):
        """Test list operations."""
        test_list = [1, 2, 3]
        test_list.append(4)
        assert len(test_list) == 4
        assert test_list[-1] == 4

    def test_dict_operations(self):
        """Test dictionary operations."""
        test_dict = {"key": "value"}
        assert "key" in test_dict
        assert test_dict["key"] == "value"
