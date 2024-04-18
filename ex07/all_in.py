
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
    "oregon": "OR",      #Esta linha cria um dicionário chamado estados, 
    "alabama": "AL",     #onde as chaves são os nomes dos estados em letras minúsculas e os valores são as siglas dos estados em letras maiúsculas.
    "nova jersey": "NJ",
    "colorado": "CO"
}

capitais = {
    "OR": "Salem",       #Esta linha cria um dicionário chamado capitais, onde as chaves são as siglas dos estados em letras
    "AL": "Montgomery",  #minúsculas e os valores são as siglas dos estados em letras maiúsculas
    "NJ": "Trenton",
    "CO": "Denver"
}

def verificar_expressao(expressao):       #Esta linha define uma função chamada verificar_expressao que recebe uma expressão como
    expressao = expressao.strip().lower() #argumento. A expressão é convertida para minúsculas e tem seus espaços em branco removidos.

    estado = estados.get(expressao)     #Essas linhas verificam se a expressão fornecida corresponde a um estado. Se corresponder, ela obtém 
    if estado:                          #a sigla do estado correspondente e, em seguida, obtém o nome da capital correspondente usando 
        capital = capitais.get(estado)  #essa sigla. Em seguida, retorna uma frase indicando a capital do estado.


        return f"{capital} is the capital of {expressao.title()}"
    
    capital = [cap for cod, cap in capitais.items() if expressao == cap.lower()]  #Essa linha verifica se a expressão fornecida corresponde a uma capital. 
                                                                                  #Se corresponder, ela obtém o nome da capital.
    
    if capital:                        
        estado = [est for est, cod in estados.items() if cod == [cod for cod, cap in capitais.items() if cap.lower() == expressao][0]][0]
        return f"{expressao.title()} is the capital of {estado}" #Essa linha verifica se a variável capital tem um valor (ou seja, se a expressão corresponde a uma
                                                                 #capital). Se corresponder, ela obtém a sigla do estado correspondente à capital e retorna uma frase 
                                                                #indicando o estado da capital.



    
    return f"{expressao.title()} is neither a capital city nor a state"  #Se a expressão não corresponder a nenhum estado nem a nenhuma capital, esta linha retorna uma
                                                                         #frase indicando que a expressão não é nem uma capital nem um estado.



import sys

if __name__ == "__main__":
    args = " ".join(sys.argv[1:]).split(",")
    for arg in args:
        arg = arg.strip()
        if arg and not arg.isspace():
            print(verificar_expressao(arg)) 

            """As linhas restantes do código lidam com a entrada de argumentos da linha de comando, dividem esses argumentos em uma lista e,
              para cada argumento, chamam a função verificar_expressao e imprimem o resultado."""
