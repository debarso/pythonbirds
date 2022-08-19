class Pessoa:
    olhos = 2  #atributo default/atributo de classe

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
    renzo.olhos = 1
    del renzo.olhos
    print(renzo.__dict__)
    print(debarso.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(debarso.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(debarso.olhos), id(renzo.olhos))


