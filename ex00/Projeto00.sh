#!/bin/bash

# Verifica se o usuário forneceu um URL como argumento
if [ -z "$1" ]; then
    echo "cript.sh bit.ly/1O72s3U
http://42.fr/."
    exit 1
fi

# Use o curl para obter o cabeçalho HTTP do URL e, em seguida, use o grep para filtrar a linha que contém o endereço real
real_address=$(curl -sI "$1" | grep -i '^location' | cut -d' ' -f2-)

# Verifica se o endereço real foi encontrado
if [ -z "$real_address" ]; then
    echo "Não foi possível encontrar o endereço real."
    exit 1
fi

echo "O endereço real é: $real_address"
    



    #exemplo scrip shel  $> ./myawesomescript.sh bit.ly/1O72s3U
#http://42.fr/
#$>  