"""Para este exercício, você pode definir quantas funções quiser e nomeá-las
como você gosta também.
O tarball d00.tar.gz no apêndice deste assunto contém uma subpasta ex03/
que contém um arquivo numbers.txt contendo os números de 1 a 100 separados por vírgula.
Projete um script Python chamado numbers.py cuja função é abrir um arquivo numbers.txt,
leia os números que ele contém e exiba-os na saída padrão, um por linha,
sem qualquer coma."""


def display_numbers_without_commas(file_path):
    """
    Abre o arquivo numbers.txt, lê os números e os exibe na saída padrão, um por linha, sem vírgulas.
    """
    try:
        with open(file_path, 'r') as file:
            numbers = file.read().strip().split(',')
            for num in numbers:
                print(num.strip())
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

def main():
    file_path = "ex03/numbers.txt"
    display_numbers_without_commas(file_path)

if __name__ == "__main__":
    main()