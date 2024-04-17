def exibir_estado(capital):
    estados = {
        "Oregon": "OR",
        "Alabama": "AL",
        "Nova Jersey": "NJ",
        "Colorado": "CO"
    }
    capitais = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if capital in capitais.values():
        codigo_estado = [estado for estado, cap in capitais.items() if cap == capital][0]
        if codigo_estado in estados.values():
            estado = [est for est, code in estados.items() if code == codigo_estado][0]
            print(estado)
        else:
            print("Estado não encontrado para esta capital.")
    else:
        print("Capital desconhecida.")


import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 1:
        exibir_estado(args[0])
    elif len(args) > 1:
        print("Muitos argumentos fornecidos.")
    else:
        pass  # Nenhum argumento fornecido, o script não faz nada
        
        # Nenhum argumento fornecido, o script não faz nada



#Criando as Listas: No início, o código tem duas listas. Uma lista tem os nomes dos estados e seus códigos, como se fosse um código de identificação de cada estado. A outra lista tem os códigos dos estados e o nome de suas capitais.

#Verificando a Capital: Depois, o código pergunta se você sabe o nome de uma capital. Se você disser o nome de uma capital, ele vai procurar essa capital na lista que tem todas as capitais. Se encontrar, vai pegar o código do estado correspondente.

#Descobrindo o Estado: Com o código do estado, ele vai olhar na lista de estados para encontrar o nome do estado que tem esse código.

#Mostrando o Estado: Finalmente, ele vai te dizer o nome do estado que tem a capital que você disse.

#Aviso de Erro: Se você disser o nome de uma capital que não está na lista, ele vai dizer que não sabe qual é o estado. E se você disser alguma coisa que não é uma capital, ele vai dizer que não entendeu.

#Olhando os Comandos: No final, ele olha se você escreveu alguma coisa junto com o nome do programa. Se escreveu, ele tenta usar essa informação como a capital. Se escreveu mais de uma coisa, ele diz que você escreveu demais. Se não escreveu nada, ele não faz nada.

#Entendeu? É como se fosse uma brincadeira de descobrir estados e capitais usando um computador!
