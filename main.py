import keyboard


class Key:
    def init(self, key_value):
        # Eventually add some logic for primary key and secondary key
        # Exmple is "!" and "1" on the same key
        self.key_value = key_value


class Spacer:
    def __init__(self, width: float = 0, height: float = 0):
        self.width: float = width
        self.height: float = height

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height


char_map = {
    '{': '}',
    '[': ']'
}


def keyparse(key_string):
    char_stack = []

    expect = None
    readUntil = None
    for i in key_string:
        # Debug print all chars
        # print(f'"{i}"')

        # Skip whitespacing for now
        # TODO: We don't always want to skip white spacing. Ex. "Caps Lock" is valid key and contains space
        if expect is not None:
            if expect == i:
                print("correct expected")
                expect = None
            else:
                print("FILE ERR: 003. unexpected char")
                expect = None


        elif i in "\r\n":
            continue
        if i in "[{":
            print(f'Pushed: {i}')
            char_stack.append(i)

        elif i in "}]":
            if i == char_map[char_stack[-1]]:
                print(f'Popped: {i}')
                char_stack.pop(-1)

        else:
            # if previous char is { this is a hwxy modifier so if the proceeding char
            # isn't in "hwxy" we must throw error
            if char_stack[-1] == '{':
                if i not in "hwxy":
                    print("FILE ERR: 002. Invalid sizing modifier char")
                else:
                    expect = ":"

    if len(char_stack) > 0:
        print("FILE ERR: 001. Stack not empty")
        print(char_stack)


# with open("ansi104.kb", 'r', encoding='utf-8') as kb_file:
#     keyparse(kb_file)

keyboard_file = """
[{w:1.75},"Caps Lock","A","S]"
"""
keyparse(keyboard_file)
