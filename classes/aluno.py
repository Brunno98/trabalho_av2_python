from .nota import Nota

class Aluno:

    def __init__(self, nome: str, materia: str, nota1: float, nota2: float,
            recuperacao: float, digital: float, recuperacaoDigital: float):
        self.nome = nome.strip().title()
        self.materia = materia.strip().capitalize()
        self.av1 = Nota(nota1)
        self.av2 = Nota(nota2)
        self.av3 = Nota(recuperacao)
        self.avd = Nota(digital)
        self.avds = Nota(recuperacaoDigital)

    
    @property
    def media(self):
        nota1 = nota2 = digital = 0
        if (self.av1 < self.av2 and self.av1 < self.av3):
            nota1 = self.av2
            nota2 = self.av3
        elif (self.av2 < self.av3):
            nota1 = self.av1
            nota2 = self.av3
        else:
            nota1 = self.av1
            nota2 = self.av2

        digital = self.avd if self.avds < self.avd else self.avds

        return (nota1 + nota2 + digital) / 3


    @property
    def situacao(self):
        media = self.media
        if media < 7:
            return "Reprovado"
        return "Aprovado"