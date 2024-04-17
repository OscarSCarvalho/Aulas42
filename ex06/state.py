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
