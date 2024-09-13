class Rectangle:
    def _init_(self, length: int, width: int):
        self.length = length
        self.width = width

    def _iter_(self):
        yield {'length': self.length}
        yield {'width': self.width}

    def _repr_(self):
        return f"Rectangle(length={self.length}, width={self.width})"
rect=Rectangle(10,5)
for value in rect:
print(value)
