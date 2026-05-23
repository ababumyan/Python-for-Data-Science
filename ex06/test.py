import pytest
from ft_filter import ft_filter


def test_filter_even_numbers():
    data = [1, 2, 3, 4, 5, 6]

    result = ft_filter(lambda x: x % 2 == 0, data)

    assert result == [2, 4, 6]


def test_filter_with_none_function():
    data = [1, 2, 3]

    result = ft_filter(None, data)

    assert result == data


def test_filter_with_none_iterable():
    result = ft_filter(lambda x: x > 0, None)

    assert result is None


def test_filter_empty_iterable():
    result = ft_filter(lambda x: x > 0, [])

    assert result == []


def test_filter_all_false():
    data = [1, 3, 5]

    result = ft_filter(lambda x: x % 2 == 0, data)

    assert result == []


def test_filter_strings():
    data = ["apple", "", "banana", ""]

    result = ft_filter(bool, data)

    assert result == ["apple", "banana"]