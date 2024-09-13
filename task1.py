class Rectangle:
    def _init_(self, length: int, width: int):
        self.length = length
        self.width = width

    def _repr_(self):
        return f"Rectangle(length={self.length}, width={self.width})"
