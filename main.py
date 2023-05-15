import sys
from PySide2 import QtGui
from criar_documentos import *
from criar_graficos import criar_graficos
from PySide2.QtWidgets import QMessageBox
from interface_grafica.interface_python import recursos
from interface_grafica.interface_python.interface_16s import *


class TaxFinder(QMainWindow):
    """Classe do App."""
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)

        # Carregar o arquivo da GUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Colocar o título da tela
        self.setWindowTitle('TaxFinder')

        # Colocar o ícone da tela
        self.setWindowIcon(QtGui.QIcon('./interface_grafica/interface_ui/icones/icone.svg'))

        # Abrir o documento com as análises da metagenômica
        self.ui.botao_abrir_arquivo_entrada.clicked.connect(self.abrir_arquivo_entrada)

        # Abrir o caminho do arquivo de saída da taxonomia
        self.ui.botao_abrir_arquivo_taxonomia.clicked.connect(self.abrir_arquivo_saida_taxonomia)

        # Abrir o caminho do arquivo de saída da quantidade
        self.ui.botao_abrir_arquivo_quantidade.clicked.connect(self.abrir_arquivo_saida_quantidade)

        # Salvar o documento e o gráfico da taxonomia
        self.ui.botao_salvar_arquivo_taxonomia.clicked.connect(self.salvar_arquivo_taxonomia)

    def abrir_arquivo_entrada(self):
        """Função responsável por abrir o arquivo com os dados da análise
        da metagenômica."""
        # Obter o caminho do arquivo de entrada
        self.caminho_entrada = QFileDialog.getOpenFileName()[0]
        self.ui.linha_arquivo_entrada.setText(self.caminho_entrada)
        caminho_split = self.caminho_entrada.split('/')[:-1]
        self.caminho_grafico = f'{"/".join(caminho_split)}/'

    def abrir_arquivo_saida_taxonomia(self):
        """Função responsável por abrir o arquivo de saída da taxonomia."""
        # Obter o caminho do arquivo de saída da taxonomia
        self.caminho_saida_taxonomia = QFileDialog.getSaveFileName()[0]
        self.ui.linha_arquivo_taxonomia.setText(f'{self.caminho_saida_taxonomia}.txt')

    def abrir_arquivo_saida_quantidade(self):
        """Função responsável por abrir o arquivo de quantidade dos item taxonômicos."""
        # Obter o caminho do arquivo de saída da quantidade
        self.caminho_saida_quantidade = QFileDialog.getSaveFileName()[0]
        self.ui.linha_arquivo_quantidade.setText(f'{self.caminho_saida_quantidade}.txt')

    def salvar_arquivo_taxonomia(self):
        """Função responsável por salvar o documento com os itens
        taxonômicos e os gráficos."""
        # Verificar qual é o banco de dados usado na análise
        rdp = self.ui.radio_rdp.isChecked()
        silva = self.ui.radio_silva.isChecked()
        greengenes = self.ui.radio_greengenes.isChecked()

        # Verificar qual a opção informada
        grafico = self.ui.radio_grafico.isChecked()
        arquivo = self.ui.radio_documento.isChecked()
        arquivo_grafico = self.ui.radio_documento_grafico.isChecked()

        # Listas com os gráficos
        graficos_rdp_silva = ['filo', 'classe', 'ordem', 'familia']
        graficos_greengenes = ['filo', 'classe', 'ordem', 'familia', 'genero']

        # Criar os documentos
        if arquivo:
            if greengenes:
                arquivo_especies(self.caminho_entrada, self.caminho_saida_taxonomia)
                quantidade_taxonomia(self.caminho_entrada, self.caminho_saida_quantidade, 'greengenes')
                QMessageBox.information(
                    self,
                    'Sucesso',
                    'Arquivos criados com sucesso!'
                )
            if rdp:
                arquivo_generos(self.caminho_entrada, self.caminho_saida_taxonomia, 'rdp')
                quantidade_taxonomia(self.caminho_entrada, self.caminho_saida_quantidade, 'rdp')
                QMessageBox.information(
                    self,
                    'Sucesso',
                    'Arquivos criados com sucesso!'
                )
            if silva:
                arquivo_generos(self.caminho_entrada, self.caminho_saida_taxonomia, 'silva')
                quantidade_taxonomia(self.caminho_entrada, self.caminho_saida_quantidade, 'silva')
                QMessageBox.information(
                    self,
                    'Sucesso',
                    'Arquivos criados com sucesso!'
                )

        # Criar os gráficos
        if grafico:
            if greengenes:
                for g in graficos_greengenes:
                    criar_graficos(self.caminho_entrada, g, self.caminho_grafico)
                QMessageBox.information(
                    self,
                    'Sucesso',
                    'Gráficos criados com sucesso!'
                )
            if rdp:
                for g in graficos_rdp_silva:
                    criar_graficos(self.caminho_entrada, g, self.caminho_grafico)
                QMessageBox.information(
                    self,
                    'Sucesso',
                    'Gráficos criados com sucesso!'
                )
            if silva:
                for g in graficos_rdp_silva:
                    criar_graficos(self.caminho_entrada, g, self.caminho_grafico)
                QMessageBox.information(
                    self,
                    'Sucesso',
                    'Gráficos criados com sucesso!'
                )

        # Criar os arquivos + gráficos
        if arquivo_grafico:
            if greengenes:
                arquivo_especies(self.caminho_entrada, self.caminho_saida_taxonomia)
                quantidade_taxonomia(self.caminho_entrada, self.caminho_saida_quantidade, 'greengenes')
                for g in graficos_greengenes:
                    criar_graficos(self.caminho_entrada, g, self.caminho_grafico)
                QMessageBox.information(
                    self,
                    'Sucesso',
                    'Arquivos e gráficos criados com sucesso!'
                )
            if rdp:
                arquivo_generos(self.caminho_entrada, self.caminho_saida_taxonomia, 'rdp')
                quantidade_taxonomia(self.caminho_entrada, self.caminho_saida_quantidade, 'rdp')
                for g in graficos_rdp_silva:
                    criar_graficos(self.caminho_entrada, g, self.caminho_grafico)
                QMessageBox.information(
                    self,
                    'Sucesso',
                    'Arquivos e gráficos criados com sucesso!'
                )
            if silva:
                arquivo_generos(self.caminho_entrada, self.caminho_saida_taxonomia, 'silva')
                quantidade_taxonomia(self.caminho_entrada, self.caminho_saida_quantidade, 'silva')
                for g in graficos_rdp_silva:
                    criar_graficos(self.caminho_entrada, g, self.caminho_grafico)
                QMessageBox.information(
                    self,
                    'Sucesso',
                    'Arquivos e gráficos criados com sucesso!'
                )


# Executar o App
if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')
    tax_finder = TaxFinder()
    tax_finder.show()
    sys.exit(app.exec_())
