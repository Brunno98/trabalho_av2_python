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
        # A media do aluno é calculada a partir da média aritmética entre os graus
        # das avaliações presenciais e digitais, sendo consideradas a nota da
        # AVD ou AVDS e apenas as duas maiores notas obtidas dentre as três etapas 
        # de avaliação (AV1, AV2 e AV3)
        nota1 = nota2 = digital = 0

        notas_presencial = [self.av1, self.av2, self.av3]
        notas_presencial.sort(reverse=True)
        nota1, nota2 = notas_presencial[:2]

        notas_digital = [self.avd, self.avds]
        notas_digital.sort(reverse=True)
        digital = notas_digital[0]

        media = (nota1 + nota2 + digital) / 3
        return round(media, 1)


    @property
    def situacao(self):
        # Para estar Aprovado o aluno deve cumprir os seguintes requisitos:
        #   Obter grau igual ou superior a 4,0 em, pelo menos, duas das três
        #   avaliações presenciais e em uma das avaliações digitais (AVD ou AVDs).
        #   Ter média maior ou igual a 6,0
        notas_insuficientes = 0
        if self.av1 < 4:
            notas_insuficientes += 1        
        if self.av2 < 4:
            notas_insuficientes += 1
        if self.av3 < 4:
            notas_insuficientes += 1
        if notas_insuficientes > 1:
            return "Reprovado"

        if self.avd < 4 and self.avds < 4:
            return "Reprovado"

        if self.media < 6:
            return "Reprovado"

        return "Aprovado"
