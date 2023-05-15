from algoritmos_taxonomia import *


def contagem_taxonomia(arquivo):
    """Função responsável por contar a quantidade de cada item
    taxonômico do arquivo gerado com os bancos de dados."""
    # Dicionário com a contagem de cada item taxonômico
    dic_contagem = {
        'filo': {},
        'classe': {},
        'ordem': {},
        'familia': {},
        'genero': {}
    }

    # Obter os itens taxonômicos
    dic_taxonomia = taxonomia_greengenes(arquivo)

    # Filo
    for filo in dic_taxonomia['filo']:
        contagem_filo = dic_taxonomia['filo'].count(filo)
        dic_contagem['filo'][filo] = contagem_filo

    # Classe
    for classe in dic_taxonomia['classe']:
        contagem_classe = dic_taxonomia['classe'].count(classe)
        dic_contagem['classe'][classe] = contagem_classe

    # Ordem
    for ordem in dic_taxonomia['ordem']:
        contagem_ordem = dic_taxonomia['ordem'].count(ordem)
        dic_contagem['ordem'][ordem] = contagem_ordem

    # Família
    for familia in dic_taxonomia['familia']:
        contagem_familia = dic_taxonomia['familia'].count(familia)
        dic_contagem['familia'][familia] = contagem_familia

    # Gênero
    for genero in dic_taxonomia['genero']:
        contagem_genero = dic_taxonomia['genero'].count(genero)
        dic_contagem['genero'][genero] = contagem_genero

    return dic_contagem
