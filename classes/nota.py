

class Nota(float):
    
    def __init__(self, nota: float) -> None:
        super().__init__()
        self.nota = nota


    def __repr__(self) -> str:
        return str(self.nota).replace('.', ',')

    def __str__(self) -> str:
        return self.__repr__()