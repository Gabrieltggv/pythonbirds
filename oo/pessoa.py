class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    gabriel = Pessoa(nome='Gabriel')
    leonel = Pessoa(gabriel, nome='leonel')
    print(Pessoa.cumprimentar(leonel))
    print(id(leonel))
    print(leonel.cumprimentar())
    print(leonel.nome)
    print(leonel.idade)
    for filho in leonel.filhos:
        print(filho.nome)
    leonel.sobrenome = "Antonio"
    del leonel.filhos
    print(leonel.__dict__)
    print(gabriel.__dict__)

