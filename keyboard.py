# w & h affect the proceeding key.
# ex. [{w:2},"Backspace"] makes the Backspace key 2 wide
# w specifies key width
# h specifies key height
# x specifies horizontal spacing
# y specifies vertical spacing
class Keyboard:
    def __init__(self, kb_string):
        self.data = kb_string
        self.length = 4

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as kb_file:
            # initialize keyboard data here
            cls.length = 5
            return cls("test")

    def __str__(self):
        return f'{self.name} | {self.test}'

    class Key:
        def __init__(self, key_string):
            keys = self.parse_key_string(key_string)

        def parse_key_string(self, key_string):
            return key_string.split("\n")
