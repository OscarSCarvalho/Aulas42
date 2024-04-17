def exibir_estado(capital):
    estados = {
        "Salem": "Oregon",
        "Montgomery": "Alabama",
        "Trenton": "Nova Jersey",
        "Denver": "Colorado"
    }
    
    if capital in estados:
        print(estados[capital])
    else:
        print("Capital desconhecida.")

import sys   #Aqui, estamos importando um módulo chamado sys, 
            #Esse módulo fornece acesso a algumas variáveis e funções especiais relacionadas ao sistema
            #incluindo os argumentos passados para o script quando ele é executado




if __name__ == "__main__": #Isso verifica se o script está sendo executado diretamente ou se está sendo importado como um módulo em outro script. 
                          # o código dentro deste bloco será executado


    args = sys.argv[1:] 
    if len(args) == 1:
        exibir_estado(args[0])
    elif len(args) > 1:
        print("Muitos argumentos fornecidos.")




"""projeto states de maneira mais simplificada menoo complexa nesse código só temso if esle na capital in estado"""


#explicação sobre sys

"""args = sys.argv[1:]
Nesta linha, estamos atribuindo à variável args uma lista contendo os argumentos passados para o script quando ele é executado. sys.argv é uma lista que contém esses argumentos. Aqui, estamos pegando todos os argumentos, exceto o primeiro (índice 0), que é o nome do próprio script. Portanto, args contém apenas os argumentos que foram passados após o nome do script.
python
Copy code
if len(args) == 1:
Esta linha verifica se o comprimento da lista de argumentos args é igual a 1. Ou seja, se apenas um argumento foi passado para o script.
python
Copy code
exibir_estado(args[0])
Se houver apenas um argumento passado para o script, esta linha chama uma função chamada exibir_estado e passa o primeiro (e único) argumento para essa função. Estamos assumindo que exibir_estado é uma função definida em outro lugar do código.
python
Copy code
elif len(args) > 1:
Se mais de um argumento foi passado para o script, esta linha é acionada. elif é uma abreviação de "else if", o que significa que é uma condição adicional que é verificada se a condição anterior não for verdadeira.
python
Copy code
print("Muitos argumentos fornecidos.")
Se houver mais de um argumento passado para o script, esta linha imprime uma mensagem dizendo que foram fornecidos muitos argumentos. Isso indica que o script não pode lidar com mais de um argumento."""