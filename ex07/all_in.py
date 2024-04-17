
"""Começando com os mesmos dicionários, você deve copiá-los novamente sem alterações em um dos
suas funções de script e escreva um programa que se comporte da seguinte maneira:
• O programa deve tomar como argumento uma string contendo tantas expressões quanto
procuramos, separados por um coma.
• Para cada expressão nesta string, o programa deve detectar se é maiúscula, estado
ou nenhum deles.
• O programa não deve diferenciar maiúsculas de minúsculas. Também não deve levar em consideração vários espaços.
• Se não houver parâmetro ou se houver muitos parâmetros, o programa não exibe
qualquer coisa.
• Quando há duas vírgulas sucessivas na string, o programa não exibe
qualquer coisa.
• O programa deve exibir resultados separados por um retorno de carro e usar estritamente
o seguinte formato:"""




"""$> python3 all_in.py "New jersey, Tren ton, NewJersey, Trenton, toto, , sAlem"
Trenton is the capital of New Jersey
Tren ton is neither a capital city nor a state
NewJersey is neither a capital city nor a state
Trenton is the capital of New Jersey
toto is neither a capital city nor a state
Salem is the capital of Oregon"""




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

def verificar_expressao(expressao):
    expressao = expressao.strip().lower()
    if expressao in capitais.values():
        estado = [est for est, code in estados.items() if code == [code for code, cap in capitais.items() if cap == expressao][0]][0]
        return f"{expressao} is the capital of {estado}"
    elif expressao in estados.values():
        capital = [cap for code, cap in capitais.items() if code == expressao][0]
        return f"{capital} is the capital of {expressao}"
    else:
        return f"{expressao} is neither a capital city nor a state"

import sys

if __name__ == "__main__":
    args = " ".join(sys.argv[1:]).split(",")
    for arg in args:
        arg = arg.strip()
        if arg and not arg.isspace():
            print(verificar_expressao(arg))
