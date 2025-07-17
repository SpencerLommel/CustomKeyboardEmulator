class Key:
    def __init__(self, key_value, width=1, height=1):
        # Eventually add some logic for primary key and secondary key
        # Exmple is "!" and "1" on the same key
        # We will probably want to represent this as a key array
        # then have .getSymbol() just get the first key and .getSymbol(1) get second
        self.key_value = key_value
        self.width = width
        self.height = height

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def __str__(self):
        return f'Key [{self.key_value}] w:{self.width},h:{self.height}'