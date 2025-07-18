# Spencer Lommel
# July 17th, 2025
# CustomKeyboardEmulator test_key.py

from src.keyboard import Key


def test_key_default_initialization() -> None:
    test_key = Key("A")
    assert test_key.width == 1.0
    assert test_key.height == 1.0


def test_key_initialization_with_size_args() -> None:
    test_key = Key("A", width=1, height=2.5)
    assert test_key.key_value == "A"
    assert test_key.width == 1
    assert test_key.height == 2.5


def test_key_modifiers() -> None:
    test_key = Key("B", width=2.2, height=3)
    assert test_key.width == 2.2
    assert test_key.height == 3

    test_key.set_width(4)
    assert test_key.width == 4

    test_key.set_height(1.0)
    assert test_key.height == 1

def test_key_equals() -> None:
    test_key_1 = Key("B", width=2.2, height=3)
    test_key_2 = Key("C", width=2.2, height=3)

    assert (test_key_1 == test_key_2) == False

    test_key_2.key_value = "B"
    assert (test_key_1 == test_key_2) == True

    test_key_2.width = 2.5
    assert (test_key_1 == test_key_2) == False

