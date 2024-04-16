"""Mais uma vez, você é livre para definir quantas funções quiser e nomeá-las como desejar.
como. Não repetiremos esta instrução, exceto se for explicitamente contradita.
Crie um script chamado var_to_dict.py no qual você copiará a seguinte lista de d
casais como está em uma de suas funções:"""

"""d = [
('Hendrix' , '1942'),
('Allman' , '1946'),
('King' , '1925'),
('Clapton' , '1945'),
('Johnson' , '1911'),
('Berry' , '1926'),
('Vaughan' , '1954'),
('Cooder' , '1947'),
('Page' , '1944'),
('Richards' , '1943'),
('Hammett' , '1962'),
('Cobain' , '1967'),
('Garcia' , '1942'),
('Beck' , '1944'),
('Santana' , '1947'),
('Ramone' , '1948'),
('White' , '1975'),
('Frusciante', '1970'),
('Thompson' , '1949'),
('Burton' , '1939')"""


"""nosso script deve transformar esta variável em um dicionário. O ano será a chave, o
nome do músico o valor. Ele deve então exibir este dicionário no padrão
saída seguindo um formato claro:"""

"""1970 : Frusciante
1954 : Vaughan
1948 : Ramone
1944 : Page Beck
1911 : Johnson"""

def couples_to_dict():
    d = [
    ('Hendrix' , '1942'),
    ('Allman' , '1946'),
    ('King' , '1925'),
    ('Clapton' , '1945'),
    ('Johnson' , '1911'),
    ('Berry' , '1926'),
    ('Vaughan' , '1954'),
    ('Cooder' , '1947'),
    ('Page' , '1944'),
    ('Richards' , '1943'),
    ('Hammett' , '1962'),
    ('Cobain' , '1967'),
    ('Garcia' , '1942'),
    ('Beck' , '1944'),
    ('Santana' , '1947'),
    ('Ramone' , '1948'),
    ('White' , '1975'),
    ('Frusciante', '1970'),
    ('Thompson' , '1949'),
    ('Burton' , '1939')
    ]

    musician_dict = {}

    for musician, year in d:
        if year in musician_dict:
            musician_dict[year].append(musician)
        else:
            musician_dict[year] = [musician]

    for year, musicians in sorted(musician_dict.items()):
        print(f"{year} : {' '.join(musicians)}")

if __name__ == "__main__":
    couples_to_dict()
