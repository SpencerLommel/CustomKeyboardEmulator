from keyboard import Keyboard, Key

# Test keyparse
# This sohuld denote a keyboard with 3 keys (3 columns 1 row)
# Caps Lock (1.75 wide), then standard size "A", "S"
# keyboard_file = """
# [{w:1.75},"Caps Lock","A","S"]
# """
# keyparse(keyboard_file)

# Test spacer
# s = Spacer(float("1.22"))
# print(s)
#
# # Test key
# k = Key("A", width=1, height=2)
# print(k)
# k.set_height(10)
# k.set_width(2.5)
# print(k)

keyboard_layout = [
    [Key("7"), Key("8"), Key("9")],
    [Key("4"), Key("5"), Key("6")],
    [Key("1"), Key("2"), Key("3")],
    [Key("0", width=2), Key(".")]
]

my_keyboard = Keyboard(keyboard_layout)

first_key = my_keyboard.get_key(3, 0)
test = Key("0", width=2)

print(test == first_key)

#
# print(my_keyboard)
#
# print(my_keyboard.get_key(3,0))

# print(my_keyboard.size)
# new_keyboard_row = [Key("A"), Key("B")]
# my_keyboard.add_row(new_keyboard_row)
# print(my_keyboard.size)
# my_keyboard.remove_row(0)
# print(my_keyboard.size)
