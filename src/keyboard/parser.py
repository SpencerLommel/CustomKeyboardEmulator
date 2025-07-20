# Spencer Lommel
# July 17th, 2025
# CustomKeyboardEmulator parser.py

# w & h affect the proceeding key.
# ex. [{w:2},"Backspace"] makes the Backspace key 2 wide
# w specifies key width
# h specifies key height
# x specifies horizontal spacing
# y specifies vertical spacing

from spacer import Spacer

char_map = {
    '{': '}',
    '[': ']'
}


# https://www.keyboard-layout-editor.com/
def parse_kle_data(key_string):
    char_stack = []
    key_stack = []

    expect = None
    # Should be some char in 'hwxy'
    sizeModifierType = ''
    keyValue = ''
    readUntil = None

    # Smallest valid keyboard is: [""]
    # We will just return an empty keyboard instead of throwing an error
    if len(key_string) < 3:
        return []

    for i in range(len(key_string)):
        # Debug print all chars
        print(f'"{key_string[i]}"')
        print(f'Read Until {readUntil}')

        if readUntil is not None:
            if key_string[i] == readUntil:
                print("done reading key value")
                readUntil = None
                # a readUntil ending in '}' means we should have a spacer size in keyValue
                if readUntil == '}':
                    key_stack.append(Spacer(float(keyValue)))

                print(keyValue)
                readUntil = None
            else:
                keyValue += key_string[i]

        # If our char_stack is empty and the next char is a comma, that must mean we've started the next column
        if len(char_stack) == 0 and i > 1:
            # print(f'{key_string[i-1]}{key_string[i]}{key_string[i+1]}')
            if key_string[i] == ',':
                print("New column")
            else:
                print("Finished parsing!")
            # continue

        # Skip whitespacing for now
        # TODO: We don't always want to skip white spacing. Ex. "Caps Lock" is valid key and contains space
        if expect is not None:
            if expect == key_string[i]:
                # the format {x:__} indicates size modifier where x in "hwxy" and __ some float
                if key_string[i] == ':':
                    readUntil = '}'
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
                    print(key_string[i])
                    print("FILE ERR: 002. Invalid sizing modifier char")
                else:
                    # assign "hwxy" to here so when we finish parsing float value we can initialize a spacer
                    sizeModifierType = key_string[i]
                    expect = ":"

    if len(char_stack) > 0:
        print("FILE ERR: 001. Stack not empty")
        print(char_stack)

    print("Here's the keyboard layout:")
    for key in key_stack:
        print(key)
