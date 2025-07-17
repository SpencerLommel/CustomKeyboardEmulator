from src.keyboard import Spacer

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

    test_spacer.setWidth(4)
    assert test_spacer.width == 4

    test_spacer.setHeight(1.0)
    assert test_spacer.height == 1