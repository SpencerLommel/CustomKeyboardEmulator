# Spencer Lommel
# July 17th, 2025
# CustomKeyboardEmulator test_key.py

from src.keyboard import Key, Spacer


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

def test_key_str() -> None:
    test_key = Key("B", width=2.2, height=3)
    assert str(test_key) == "Key [B] w:2.2,h:3"

def test_key_equality() -> None:
    k1 = Key("A", 1.0, 2.0)
    k2 = Key("A", 1.0, 2.0)
    k3 = Key("B", 1.0, 2.0)
    s1 = Spacer(1.0, 2.0)
    assert k1 == k2
    assert k1 != k3
    assert k1 != s1