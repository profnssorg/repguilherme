## Nome do Programa: Validação de números inteiros
## Autor: Guilherme Mendes
## Descrição: Valida a resposta a um input como sendo um número inteiro dentro da faixa especificada
## Versão: 1.0
## Data: 26/11/2017


## Definição de funções

def valida_inteiro(mensagem, mínimo, máximo):
    '''
    Valida a resposta a um input como sendo um número inteiro dentro da faixa especificada
        mensagem : input a ser exibido
        mínimo : valor mínimo aceitável
        máximo : valor máximo aceitável
    '''
    
    while True:
        try:
            v = int(input(mensagem))

            if v >= mínimo and v <= máximo:
                return v
            else:
                print("Digite um valor entre %d e %d" % (mínimo, máximo))
        except:
            print("Você deve digitar um número inteiro")
