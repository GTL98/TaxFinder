import matplotlib.pyplot as plt
from contagem_taxonomia import contagem_taxonomia


def criar_graficos(arquivo, hierarquia, caminho):
    """Função responsável por criar os gráficos de cada banco de dados usado."""
    # Contagem dos itens taxonômicos
    contagem_grafico = contagem_taxonomia(arquivo)

    # Contagem da hierarquia taxonômica
    contagem_hierarquia = contagem_grafico[hierarquia]

    # Criar as listas com a hierarquia taxonômica e a quantidade
    lista_hierarquia = list(contagem_hierarquia.keys())
    lista_quantidade = list(contagem_hierarquia.values())

    # Criar o gráfico
    _, ax = plt.subplots(figsize=(30, 20), dpi=120)

    # Deixar o gráfico na horizontal
    ax.barh(lista_hierarquia, lista_quantidade)
    for i in ax.patches:
        # Colocar a quantidade de cada item no gráfico
        plt.text(
            i.get_width()+0.2,
            i.get_y()+0.4,
            str(i.get_width()),
            fontsize=10,
            fontweight='bold'
        )

    # Título do gráfico
    plt.title(f'{hierarquia.title()}')

    # Salvar a imagem
    plt.savefig(f'{caminho}/{hierarquia}.png')
