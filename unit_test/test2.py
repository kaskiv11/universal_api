import pytest


def is_even(number):
    return number%2 == 0


@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False),
    (10, True),
    (11, False),
    (100, True),
    (101, False)
])
def test_is_even(number, expected):
    assert is_even(number) == expected


@pytest.fixture
def simple_data():
    return {"name": "John", "age": 30}


def test_simple_data(simple_data):
    assert simple_data["name"] == "John"
    assert simple_data["age"] == 30