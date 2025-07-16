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
    for i in key_string:
        print(i)
        if i in "[{":
            print(f'Pushed: {i}')
            char_stack.append(i)

        elif i in "}]":
            if i == char_map[char_stack[-1]]:
                print(f'Popped: {i}')
                char_stack.pop(-1)

        else:
            pass

    if len(char_stack) > 0:
        print("FILE ERR: 001. Stack not empty")
        print(char_stack)


# with open("ansi104.kb", 'r', encoding='utf-8') as kb_file:
#     keyparse(kb_file)

# keyboard_file = """
# [{w:1.75},"Caps Lock","A","S]"
# """
# keyparse(keyboard_file)
