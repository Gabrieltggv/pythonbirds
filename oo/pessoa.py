class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}, Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    gabriel = Mutante(nome='Gabriel')
    leonel = Homem(gabriel, nome='leonel')
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
    print(Pessoa.olhos)
    print(leonel.olhos)
    print(gabriel.olhos)
    print(id(Pessoa.olhos), id(leonel.olhos), id(gabriel.olhos))
    print(Pessoa.metodo_estatico(), leonel.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), leonel.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(gabriel.olhos)
    print(leonel.cumprimentar())
    print(gabriel.cumprimentar())

