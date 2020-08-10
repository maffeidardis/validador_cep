
#Criando a classe validar cep

class ValidarCEP:
    def __init__(self, cep):
        self.cep = cep

    def validar_todas_condicoes(self):
        self.validar_se_inteiro()
        self.validar_range_cep()
        self.validar_se_par_repetido()

    def validar_se_inteiro(self):
        if not self.cep.isdigit():
            raise ValueError(f'Insira apenas valores numéricos para o CEP({self.cep})')
        else:
            pass

    def validar_range_cep(self):
        if int(self.cep) > 100000 and int(self.cep) < 999999:
            pass
        else:
            raise ValueError(f'O CEP inserido ({self.cep}) não se encaixa no range permitido (entre 100.000 e 999999)')

    def validar_se_par_repetido(self):
        cep_lista = [numero for numero in str(self.cep)]
        for i in range(len(cep_lista) - 2):
            if cep_lista[i] == cep_lista[i + 2]:
                raise ValueError(f'Erro, número repetido em par ({cep_lista[i]} = {cep_lista[i + 2]}) para o CEP {self.cep} ')
            else:
                return print(f"CEP ({self}.cep) validado com sucesso")


if __name__ == '__main__':
    validar = ValidarCEP('111111')
    validar.validar_todas_condicoes()