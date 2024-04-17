def exibir_capital(estado):  #>>>  Esta linha define uma função chamada exibir_capital que recebe um argumento estado.

    estados = {
        "Oregon": "OR",
        "Alabama": "AL",        #>>> Aqui é definido um dicionário chamado estados, onde as chaves são os nomes completos dos estados 
        "Nova Jersey": "NJ",    #>>>e os valores são os códigos de duas letras para esses estados
        "Colorado": "CO"
    }


    capitais = {
        "OR": "Salem",
        "AL": "Montgomery",    #Este é outro dicionário chamado capitais, onde as chaves são os códigos 
        "NJ": "Trenton",       #de estados e os valores são as capitais correspondentes
        "CO": "Denver"
    }

    if estado in estados:  #>> Esta linha verifica se o estado fornecido como argumento está presente no dicionário estados
        codigo_estado = estados[estado] #Se o estado estiver presente no dicionário estados, esta linha obtém o código de duas letras do estado
        if codigo_estado in capitais:   #Esta linha verifica se o código de estado obtido anteriormente está presente no dicionário capitais
            print(capitais[codigo_estado])  #Se a capital correspondente ao código de estado estiver presente no dicionário capitais, esta linha imprime o nome da capital
        else:
            print("Capital não encontrada para este estado.")  #Se o código de estado não estiver presente no dicionário capitais, 
                                                               #esta linha imprime uma mensagem informando que a capital não foi encontrada para esse estado
    else:
        print("Estado desconhecido.") #Se o estado fornecido como argumento não estiver presente no dicionário estados,
                                       # esta linha imprime uma mensagem informando que o estado é desconhecido

import sys  #Esta linha importa o módulo sys, que fornece acesso a algumas variáveis ​​do interpretador e a funcionalidades relacionadas ao sistema

if __name__ == "__main__":  #Esta linha verifica se o script está sendo executado diretamente (não importado como um módulo)
    args = sys.argv[1:]      #Esta linha obtém os argumentos da linha de comando, excluindo o nome do script.
    if len(args) == 1:       #Esta linha verifica se foi fornecido exatamente um argumento na linha de comando.
        exibir_capital(args[0])  #Se um único argumento foi fornecido na linha de comando, chama a função exibir_capital com esse argumento
    elif len(args) > 1:          #Esta linha verifica se mais de um argumento foi fornecido na linha de comando
        print("Muitos argumentos fornecidos.") #Se mais de um argumento foi fornecido, imprime uma mensagem informando que muitos argumentos foram fornecidos
    else:
        pass  # Nenhum argumento fornecido, o script não faz nada


    #obs: ápos rodar o codigo inserir o estado no terminal para obetr resultado Capital dp estado.
