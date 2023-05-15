from memoize import memoize
from algoritmos_taxonomia import *
from contagem_taxonomia import contagem_taxonomia


@memoize
def arquivo_especies(arquivo_entrada, arquivo_saida):
    """Função responsável por gerar o arquivo com todas as espécies
    do documento gerado com o banco de dados Greengenes."""
    # Obter as espécies do documento
    especies = taxonomia_greengenes(arquivo_entrada)['especie']

    # Criar o arquivo
    with open(f'{arquivo_saida}.txt', 'w') as txt:
        for especie in especies:
            txt.write(especie)
            txt.write('\n')


@memoize
def arquivo_generos(arquivo_entrada, arquivo_saida, banco):
    """Função responsável por gerar o arquivo com todas os gêneros
       do documento gerado com os bancos de dados RDP e SILVA."""
    # Selecionar o banco de dados usado
    if banco == 'rdp':
        # Obter os gêneros do documento
        generos = taxonomia_rdp(arquivo_entrada)['genero']

        # Criar o arquivo
        with open(f'{arquivo_saida}.txt', 'w') as txt:
            for genero in generos:
                txt.write(genero)
                txt.write('\n')

    # Selecionar o banco de dados usado
    elif banco == 'silva':
        # Obter os gêneros do documento
        generos = taxonomia_silva(arquivo_entrada)

        # Criar o arquivo
        with open(f'{arquivo_saida}.txt', 'w') as txt:
            for genero in generos:
                if genero != 'uncultured':
                    txt.write(genero)
                    txt.write('\n')


@memoize
def quantidade_taxonomia(arquivo_entrada, arquivo_saida, banco):
    """Função responsável por gerar o arquivo com a quantiadade de
    cada item taxônomico conforme o banco de dados."""
    # Obter a contagem de cada item
    taxonomia = contagem_taxonomia(arquivo_entrada)
    # Selecionar o banco de dados usado
    if banco == 'greengenes':
        filo = taxonomia['filo']
        classe = taxonomia['classe']
        ordem = taxonomia['ordem']
        familia = taxonomia['familia']
        genero = taxonomia['genero']

    elif banco == 'rdp':
        filo = taxonomia['filo']
        classe = taxonomia['classe']
        ordem = taxonomia['ordem']
        familia = taxonomia['familia']

    elif banco == 'silva':
        filo = taxonomia['filo']
        classe = taxonomia['classe']
        ordem = taxonomia['ordem']
        familia = taxonomia['familia']

    # Abrir o arquivo
    with open(f'{arquivo_saida}.txt', 'w') as txt:
        # Filo
        txt.write('## Filo ##')
        txt.write('\n')
        lista_id_filo = []
        for valor in filo.values():
            if valor not in lista_id_filo:
                lista_id_filo.append(valor)
        lista_id_filo_ordenada = sorted(lista_id_filo, reverse=True)
        for ids in lista_id_filo_ordenada:
            for chave, valor in filo.items():
                if valor == ids:
                    txt.write(f'{chave} {filo[chave]}')
                    txt.write('\n')
        txt.write('\n\n')

        # Classe
        txt.write('## Classe ##')
        txt.write('\n')
        lista_id_classe = []
        for valor in classe.values():
            if valor not in lista_id_classe:
                lista_id_classe.append(valor)
        lista_id_classe_ordenada = sorted(lista_id_classe, reverse=True)
        for ids in lista_id_classe_ordenada:
            for chave, valor in classe.items():
                if valor == ids:
                    txt.write(f'{chave} {classe[chave]}')
                    txt.write('\n')
        txt.write('\n\n')

        # Ordem
        txt.write('## Ordem ##')
        txt.write('\n')
        lista_id_ordem = []
        for valor in ordem.values():
            if valor not in lista_id_ordem:
                lista_id_ordem.append(valor)
        lista_id_ordem_ordenada = sorted(lista_id_ordem, reverse=True)
        for ids in lista_id_ordem_ordenada:
            for chave, valor in ordem.items():
                if valor == ids:
                    txt.write(f'{chave} {ordem[chave]}')
                    txt.write('\n')
        txt.write('\n\n')

        # Família
        txt.write('## Família ##')
        txt.write('\n')
        lista_id_familia = []
        for valor in familia.values():
            if valor not in lista_id_familia:
                lista_id_familia.append(valor)
        lista_id_familia_ordenada = sorted(lista_id_familia, reverse=True)
        for ids in lista_id_familia_ordenada:
            for chave, valor in familia.items():
                if valor == ids:
                    txt.write(f'{chave} {familia[chave]}')
                    txt.write('\n')
        txt.write('\n\n')

        # Gênero
        if banco == 'greengenes':
            txt.write('## Gênero ##')
            txt.write('\n')
            lista_id_genero = []
            for valor in genero.values():
                if valor not in lista_id_genero:
                    lista_id_genero.append(valor)
            lista_id_genero_ordenada = sorted(lista_id_genero, reverse=True)
            for ids in lista_id_genero_ordenada:
                for chave, valor in genero.items():
                    if valor == ids:
                        txt.write(f'{chave} {genero[chave]}')
                        txt.write('\n')
            txt.write('\n\n')
