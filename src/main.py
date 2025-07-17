from keyboard import Keyboard, Key, Spacer

# Test keyparse
# This sohuld denote a keyboard with 3 keys (3 columns 1 row)
# Caps Lock (1.75 wide), then standard size "A", "S"
# keyboard_file = """
# [{w:1.75},"Caps Lock","A","S"]
# """
# keyparse(keyboard_file)

# Test spacer
s = Spacer(float("1.22"))
print(s)

# Test key
k = Key("A", width=1, height=2)
print(k)
k.setHeight(10)
k.setWidth(2.5)
print(k)