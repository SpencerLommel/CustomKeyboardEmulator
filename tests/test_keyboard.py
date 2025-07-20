# Spencer Lommel
# July 18th, 2025
# CustomKeyboardEmulator test_keyboard.py

from src.keyboard import Key, Keyboard


def test_keyboard_default_initialization() -> None:
    test_keyboard = Keyboard()
    assert test_keyboard.size == 0
    assert test_keyboard.width == 0
    assert test_keyboard.height == 0
    assert test_keyboard.rows == []


def test_keyboard_initialize_with_numpad() -> None:
    keyboard_layout = [
        [Key("7"), Key("8"), Key("9")],
        [Key("4"), Key("5"), Key("6")],
        [Key("1"), Key("2"), Key("3")],
        [Key("0", width=2), Key(".")]
    ]

    # TODO: once I refactor keyboard.py initialization change this test to accommodate new initialization method
    # Once I refactor keyboard.py anyways this should fail which is why unit testing is nice =D
    test_keyboard = Keyboard()
    for key_row in keyboard_layout:
        test_keyboard.add_row(key_row)

    assert test_keyboard.height == 4
    assert test_keyboard.width == 3
