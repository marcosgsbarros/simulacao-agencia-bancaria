from random import randint

class Agencia:
    
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 1000000
        self.emprestimos = []
    
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado, caixa atual é R$ {:,.2f}'.format(self.caixa))
        else:
            print('O valor do caixa está OK, caixa atual é R$ {:,.2f}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            print('Empréstimo realizado com sucesso! valor solicitado foi de R$ {:,.2f}'.format(valor))
        else:
            print('Saldo insuficiente para realizar empréstimo')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

class AgenciaVirtual(Agencia):
    
    def __init__(self,site,telefone, cnpj):
        super().__init__(telefone, cnpj, 1000)
        self.site = site
        self.caixa = 1000000
        self.caixa_paypal = 1000000
    
    def depositar_paypal(self,valor):
        self.caixa_paypal += valor
        self.caixa -= valor

    def saque_paypal(self,valor):
        self.caixa_paypal -= valor
        self.caixa += valor

class AgenciaComum(Agencia):
    
    def __init__(self,telefone, cnpj):
        super().__init__(telefone, cnpj, numero = randint(1001,9999))
        self.caixa = 2000000
        

class AgenciaPremium(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero= randint(1001,9999))
        self.caixa = 10000000
    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio >= 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O cliente não tem o patrimonio minimo necessário para ter conta na agencia premium')

if __name__=='__main__':    
    agencia_comum = AgenciaComum('34152478','0151515000165')
    agencia_premium = AgenciaPremium('25214545','1457874000184')
    agencia_virtual = AgenciaVirtual('www.modalmais.com', '3232-3232', '16254847000160')
    agencia_premium.adicionar_cliente('marcos premium',121616516516,100000)






