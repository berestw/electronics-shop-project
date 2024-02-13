import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_name(keyboard):
    assert str(keyboard) == "Dark Project KD87A"


def test_change_lang(keyboard):
    assert str(keyboard.language) == "EN"
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"


def teat_error(keyboard):
    with pytest.raises(AttributeError):
        keyboard.language = 'CH'
