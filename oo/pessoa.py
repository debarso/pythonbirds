class Pessoa:
    def __init__(self, *filhos, nome=None, idade=49):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Hello {id(self)}'

if __name__ == '__main__':
    debarso = Pessoa(nome='DeBarso')
    renzo = Pessoa(debarso, nome='Renzo')
    print(Pessoa.cumprimentar(renzo))
    print(id(renzo))
    print(renzo.cumprimentar())
    print(renzo.nome)
    print(renzo.idade)
    for filho in renzo.filhos:
        print(filho.nome)
    renzo.sobrenome = 'Nuccitelli'
    del renzo.filhos
    print(renzo.__dict__)
    print(debarso.__dict__)


