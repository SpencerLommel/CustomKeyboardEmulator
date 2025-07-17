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

    def __str__(self):
        return f'w:{self.width},h:{self.height}'


char_map = {
    '{': '}',
    '[': ']'
}


def keyparse(key_string):
    char_stack = []
    key_stack = []

    expect = None
    # Should be some char in 'hwxy'
    sizeModifierType = ''
    keyValue = ''
    readUntil = None
    for i in range(len(key_string)):
        # Debug print all chars
        # print(f'"{key_string[i]}"')

        if readUntil is not None:
            if key_string[i] == readUntil:
                print("done reading key value")
                # a readUntil ending in '}' means we should have a spacer size in keyValue
                if readUntil == '}':
                    key_stack.append(Spacer(float(keyValue)))

                print(keyValue)
                readUntil = None
            else:
                keyValue += key_string[i]


        # Skip whitespacing for now
        # TODO: We don't always want to skip white spacing. Ex. "Caps Lock" is valid key and contains space
        if expect is not None:
            if expect == key_string[i]:
                # the format {x:__} indicates size modifier where x in "hwxy" and __ some float
                if key_string[i] == ':':
                    readUntil = '}'
                print("correct expected")
                expect = None
            else:
                print("FILE ERR: 003. unexpected char")
                expect = None


        elif key_string[i] in "\r\n":
            continue
        if key_string[i] in "[{":
            print(f'Pushed: {i}')
            char_stack.append(key_string[i])

        elif key_string[i] in "}]":
            if key_string[i] == char_map[char_stack[-1]]:
                print(f'Popped: {key_string[i]}')
                char_stack.pop(-1)

        else:
            # if previous char is { this is a hwxy modifier so if the proceeding char
            # isn't in "hwxy" we must throw error
            if char_stack[-1] == '{':
                if key_string[i] not in "hwxy":
                    print("FILE ERR: 002. Invalid sizing modifier char")
                else:
                    # assign "hwxy" to here so when we finish parsing float value we can initialize a spacer
                    sizeModifierType = key_string[i]
                    expect = ":"

    if len(char_stack) > 0:
        print("FILE ERR: 001. Stack not empty")
        print(char_stack)

    print(key_stack)


# with open("ansi104.kb", 'r', encoding='utf-8') as kb_file:
#     keyparse(kb_file)


# Test keyparse
keyboard_file = """
[{w:1.75},"Caps Lock","A","S]"
"""
keyparse(keyboard_file)



# Test spacer
# s = Spacer(float("1.22"))
# print(s)