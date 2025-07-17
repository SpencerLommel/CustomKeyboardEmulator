from src.keyboard import Key

def test_key_initialization() -> None:
    my_key = Key("A", width=1, height=2.5)
    assert my_key.key_value == "A"
    assert my_key.width == 1
    assert my_key.height == 2.5