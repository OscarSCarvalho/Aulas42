"""Exercício 02: Minhas primeiras variáveis
Diretório de entrega: ex02/
Arquivos para entregar: var.py
Funções permitidas: n/a """


"""

Exercício 02: Minhas primeiras variáveis
Diretório de entrega: ex02/
Arquivos para entregar: var.py
Funções permitidas: n/a
Crie um script chamado var.py no qual você definirá uma função my_var. Nisso
função, você declarará 9 variáveis ​​de tipos diferentes e as imprimirá no padrão
saída. Você reproduzirá esta saída exatamente:
$> python3 var.py
42 tem um tipo <class 'int'>
42 tem um tipo <class 'str'>
quarante-deux tem um tipo <class 'str'>
42.0 tem um tipo <class 'float'>
True tem um tipo <class 'bool'>
[42] tem um tipo <class 'list'>
{42: 42} tem um tipo <class 'dict'>
(42,) tem um tipo <class 'tuple'>
set() tem um tipo <class 'set'>
$>
Claro, escrever explicitamente seus tipos de variáveis ​​nas impressões do seu código é estritamente
Entrada. Não se esqueça de chamar sua função no final do script, conforme exigido por
As instruções:
se __nome__ == '__principal__':
minha_var"""

def my_var():

 X = 5  # Variável inteira
 nome = "Maria"  # Variável string
 y = 3.14  # Variável float
 ativo = True  # Variável booleana
 lista = [1, 2, 3, 4, 5]  # Variável lista
 tupla = (10, 20, 30)  # Variável tupla
 conjunto = {"a", "b", "c"}  # Variável conjunto
 dicionario = {"chave": "valor", "nome": "João"}  # Variável dicionário
 nulo = None  # Variável nula


 print("O tipo de x é:", X)
 print("O tipo de x é:", nome)
 print("O tipo de x é:", y)
 print("O tipo de x é:", ativo)
 print("O tipo de x é:", lista)
 print("O tipo de x é:", tupla)
 print("O tipo de x é:", conjunto)
 print("O tipo de x é:", dicionario)
 print("O tipo de x é:", nulo)

my_var()