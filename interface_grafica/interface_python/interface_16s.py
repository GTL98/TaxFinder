# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_16sQKedXm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(624, 258)
        MainWindow.setMinimumSize(QSize(624, 258))
        MainWindow.setMaximumSize(QSize(16777215, 258))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.linha_arquivo_entrada = QLineEdit(self.centralwidget)
        self.linha_arquivo_entrada.setObjectName(u"linha_arquivo_entrada")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.linha_arquivo_entrada.setFont(font1)

        self.horizontalLayout.addWidget(self.linha_arquivo_entrada)

        self.botao_abrir_arquivo_entrada = QPushButton(self.centralwidget)
        self.botao_abrir_arquivo_entrada.setObjectName(u"botao_abrir_arquivo_entrada")
        self.botao_abrir_arquivo_entrada.setFont(font1)
        self.botao_abrir_arquivo_entrada.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icones/icones/botao_abrir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_abrir_arquivo_entrada.setIcon(icon)

        self.horizontalLayout.addWidget(self.botao_abrir_arquivo_entrada)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.groupBox.setFont(font2)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radio_greengenes = QRadioButton(self.groupBox)
        self.radio_greengenes.setObjectName(u"radio_greengenes")

        self.verticalLayout.addWidget(self.radio_greengenes)

        self.radio_rdp = QRadioButton(self.groupBox)
        self.radio_rdp.setObjectName(u"radio_rdp")

        self.verticalLayout.addWidget(self.radio_rdp)

        self.radio_silva = QRadioButton(self.groupBox)
        self.radio_silva.setObjectName(u"radio_silva")

        self.verticalLayout.addWidget(self.radio_silva)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font2)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radio_documento = QRadioButton(self.groupBox_2)
        self.radio_documento.setObjectName(u"radio_documento")

        self.verticalLayout_2.addWidget(self.radio_documento)

        self.radio_grafico = QRadioButton(self.groupBox_2)
        self.radio_grafico.setObjectName(u"radio_grafico")

        self.verticalLayout_2.addWidget(self.radio_grafico)

        self.radio_documento_grafico = QRadioButton(self.groupBox_2)
        self.radio_documento_grafico.setObjectName(u"radio_documento_grafico")

        self.verticalLayout_2.addWidget(self.radio_documento_grafico)


        self.horizontalLayout_2.addWidget(self.groupBox_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.linha_arquivo_taxonomia = QLineEdit(self.centralwidget)
        self.linha_arquivo_taxonomia.setObjectName(u"linha_arquivo_taxonomia")
        self.linha_arquivo_taxonomia.setFont(font1)

        self.horizontalLayout_3.addWidget(self.linha_arquivo_taxonomia)

        self.botao_abrir_arquivo_taxonomia = QPushButton(self.centralwidget)
        self.botao_abrir_arquivo_taxonomia.setObjectName(u"botao_abrir_arquivo_taxonomia")
        self.botao_abrir_arquivo_taxonomia.setFont(font1)
        self.botao_abrir_arquivo_taxonomia.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_abrir_arquivo_taxonomia.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.botao_abrir_arquivo_taxonomia)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.linha_arquivo_quantidade = QLineEdit(self.centralwidget)
        self.linha_arquivo_quantidade.setObjectName(u"linha_arquivo_quantidade")
        self.linha_arquivo_quantidade.setFont(font1)

        self.horizontalLayout_4.addWidget(self.linha_arquivo_quantidade)

        self.botao_abrir_arquivo_quantidade = QPushButton(self.centralwidget)
        self.botao_abrir_arquivo_quantidade.setObjectName(u"botao_abrir_arquivo_quantidade")
        self.botao_abrir_arquivo_quantidade.setFont(font1)
        self.botao_abrir_arquivo_quantidade.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_abrir_arquivo_quantidade.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.botao_abrir_arquivo_quantidade)

        self.botao_salvar_arquivo_taxonomia = QPushButton(self.centralwidget)
        self.botao_salvar_arquivo_taxonomia.setObjectName(u"botao_salvar_arquivo_taxonomia")
        self.botao_salvar_arquivo_taxonomia.setFont(font1)
        self.botao_salvar_arquivo_taxonomia.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icones/icones/botao_salvar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_salvar_arquivo_taxonomia.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.botao_salvar_arquivo_taxonomia)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Arquivo entrada:", None))
        self.botao_abrir_arquivo_entrada.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Banco de dados", None))
        self.radio_greengenes.setText(QCoreApplication.translate("MainWindow", u"Greengenes", None))
        self.radio_rdp.setText(QCoreApplication.translate("MainWindow", u"RDP", None))
        self.radio_silva.setText(QCoreApplication.translate("MainWindow", u"SILVA", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es", None))
        self.radio_documento.setText(QCoreApplication.translate("MainWindow", u"Documento", None))
        self.radio_grafico.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico", None))
        self.radio_documento_grafico.setText(QCoreApplication.translate("MainWindow", u"Documento + Gr\u00e1fico", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Arquivo taxonomia:", None))
        self.botao_abrir_arquivo_taxonomia.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Arquivo quantidade:", None))
        self.botao_abrir_arquivo_quantidade.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.botao_salvar_arquivo_taxonomia.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
    # retranslateUi

