from memoize import memoize


@memoize
def taxonomia_greengenes(arquivo):
    """Função responsável por tratar o documento gerado com o banco de dados Greengenes."""
    # Dicionário para armazenar cada taxonomia presente no documento
    dic_taxonomia = {
        'filo': [],
        'classe': [],
        'ordem': [],
        'familia': [],
        'genero': [],
        'especie': []
    }

    # Abrir o arquivo
    with open(arquivo, 'r') as txt:
        # Obter as linhas
        linhas = txt.readlines()
        linhas_split = [dado.split('\t') for dado in linhas]

    # Armazenar cada taxonomia na chave correta
    for linha in linhas_split:
        if 's__' in linha[-1]:
            # Filo
            filo = linha[2].split('p__')
            dic_taxonomia['filo'].append(filo[1])

            # Classe
            classe = linha[3].split('c__')
            dic_taxonomia['classe'].append(classe[1])

            # Ordem
            ordem = linha[4].split('o__')
            dic_taxonomia['ordem'].append(ordem[1])

            # Família
            familia = linha[5].split('f__')
            dic_taxonomia['familia'].append(familia[1])

            # Gênero
            genero = linha[6].split('g__')
            dic_taxonomia['genero'].append(genero[1])

            # Espécie
            especie_split = linha[7].split('s__')
            especie = ' '.join(especie_split[1].split('_'))
            dic_taxonomia['especie'].append(especie.split('\n')[0])

    return dic_taxonomia


@memoize
def taxonomia_rdp(arquivo):
    """Função responsável por tratar o documento gerado com o banco de dados RDP."""
    # Dicionário para armazenar cada taxonomia presente no documento
    dic_taxonomia = {
        'filo': [],
        'classe': [],
        'ordem': [],
        'familia': [],
        'genero': []
    }

    # Abrir o arquivo
    with open(arquivo, 'r') as txt:
        # Obter as linhas
        linhas = txt.readlines()
        linhas_split = [dado.split('\t') for dado in linhas]

    # Armazenar cada taxonomia na chave correta
    for linha in linhas_split:
        if len(linha) == 7:
            if 'g__' in linha[-1]:
                # Filo
                filo = linha[2].split('p__')
                filo = filo[1].replace('"', '')
                dic_taxonomia['filo'].append(filo)

                # Classe
                classe = linha[3].split('c__')
                classe = classe[1].replace('"', '')
                dic_taxonomia['classe'].append(classe)

                # Ordem
                ordem = linha[4].split('o__')
                ordem = ordem[1].replace('"', '')
                dic_taxonomia['ordem'].append(ordem)

                # Família
                familia = linha[5].split('f__')
                familia = familia[1].replace('"', '')
                dic_taxonomia['familia'].append(familia)

                # Gênero
                genero = linha[6].split('g__')
                genero = genero[1].replace('"', '')
                dic_taxonomia['genero'].append(genero.split('\n')[0])

    return dic_taxonomia


@memoize
def taxonomia_silva(arquivo):
    """Função responsável por tratar o documento gerado com o banco de dados SILVA."""
    # Dicionário para armazenar cada taxonomia presente no documento
    dic_taxonomia = {
        'filo': [],
        'classe': [],
        'ordem': [],
        'familia': [],
        'genero': []
    }

    # Abrir o arquivo
    with open(arquivo, 'r') as txt:
        # Obter as linhas
        linhas = txt.readlines()
        linhas_split = [dado.split('\t') for dado in linhas]

    # Armazenar cada taxonomia na chave correta
    for linha in linhas_split:
        if len(linha) == 7:
            if 'g__' in linha[-1]:
                # Filo
                filo = linha[2].split('p__')
                dic_taxonomia['filo'].append(filo[1])

                # Classe
                classe = linha[3].split('c__')
                dic_taxonomia['classe'].append(classe[1])

                # Ordem
                ordem = linha[4].split('o__')
                dic_taxonomia['ordem'].append(ordem[1])

                # Família
                familia = linha[5].split('f__')
                dic_taxonomia['familia'].append(familia[1])

                # Gênero
                genero = linha[6].split('g__')
                dic_taxonomia['genero'].append(genero[1].split('\n')[0])

    return dic_taxonomia
