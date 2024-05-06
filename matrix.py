class Matrix():
    values: list[list[int]] = []

    def __init__(self, values: list[list[int]]) -> None:
        self.values = values
        self.__verify()
        
    def __verify(self):
        if len(self.values) == 0:
            return
        for i, row in enumerate(self.values, 1):
            if len(row) != len(self.values[0]):
                raise ValueError(f"Invalid matrix: Inconsistent row length. (Row {i})")
    
    def __str__(self) -> str:
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.values)
    
    def __getitem__(self, key: int) -> list[int]:
        return self.values[key]
    
    def __setitem__(self, key: int, value: list[int]) -> None:
        self.values[key] = value
        self.__verify()

    def __len__(self) -> int:
        return len(self.values)
    
    def column(self, index: int) -> list[int]:
        return [row[index] for row in self.values]
    
    def row(self, index: int) -> list[int]:
        return self.values[index]
    
    def columns(self):
        for i in range(len(self.values[0])):
            yield self.column(i)
    
    def rows(self):
        for row in self.values:
            yield row

    def __mul__(self, other: int) -> 'Matrix':
        return Matrix([[cell * other for cell in row] for row in self.values])
    
    def __truediv__(self, other: int) -> 'Matrix':
        return Matrix([[cell / other for cell in row] for row in self.values])