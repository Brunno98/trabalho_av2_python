

class Nota(float):
    
    def __init__(self, nota: float) -> None:
        super().__init__()
        self.nota = nota


    def __repr__(self) -> str:
        if self.nota < 4:
            return str(self.nota).replace('.', ',') + '*'
        return str(self.nota).replace('.', ',')

    def __str__(self) -> str:
        return self.__repr__()