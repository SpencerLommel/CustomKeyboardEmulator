# Spencer Lommel
# July 17th, 2025
# CustomKeyboardEmulator test_spacer.py


from src.keyboard import Spacer, Key


def test_spacer_default_initialization() -> None:
    test_spacer = Spacer()
    assert test_spacer.width == 0
    assert test_spacer.height == 0


def test_spacer_initialization_with_size_args() -> None:
    test_spacer = Spacer(width=1.0, height=2.2)
    assert test_spacer.width == 1
    assert test_spacer.height == 2.2


def test_spacer_modifiers() -> None:
    test_spacer = Spacer(width=2.2, height=3)
    assert test_spacer.width == 2.2
    assert test_spacer.height == 3

    test_spacer.set_width(4)
    assert test_spacer.width == 4

    test_spacer.set_height(1.0)
    assert test_spacer.height == 1

def test_spacer_str() -> None:
    test_spacer = Spacer(width=1.5, height=2.0)
    assert str(test_spacer) == "Spacer w:1.5,h:2.0"

def test_spacer_equality() -> None:
    s1 = Spacer(1.0, 2.0)
    s2 = Spacer(1.0, 2.0)
    s3 = Spacer(2.0, 1.0)
    k1 = Key("A", 1.0, 2.0)
    assert s1 == s2
    assert s1 != s3
    assert s1 != k1
