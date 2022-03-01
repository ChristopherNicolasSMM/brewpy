from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from ui_main import Ui_MainWindow
import sys
#from ui_funtions import *
import funcoes
from database import Data_base
import pandas as pd
import sqlite3

class FuncoesTela(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(FuncoesTela, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("DevBrew Sistema Cervejeiro - BR")
        appIcon = QIcon(u"logo_sistema.png")
        self.setWindowIcon(appIcon)
        
def salvar(self):
        if self.paginacao.currentIndex() == 5:#Cadastros
            if self.cadastro_tabw.currentIndex() == 0: #Malte
                parametros = {}
                if self.gv_id_malte != 0:
                    parametros["id_malte"] =  self.gv_id_malte
                parametros["nome"] =  self.descricao_malte_tbx.text()
                parametros["origem"] =  self.origem_malte_tbx.text()
                parametros["fabricante"] =  self.fabricante_malte_tbx.text()
                parametros["tipo"] =  self.tipo_malte_cb.currentText()
                parametros["quantidade_max"] =  self.qntmax_malte_tbx.text()
                parametros["cor"] =  self.cor_malte_tbx.text()
                parametros["preco"] =  self.preco_malte_tbx.text()
                parametros["extrato_ibu"] =  self.extibulkg_malte_tbx.text()
                parametros["potencial_sg"] =  self.potencial_sg_malte_tbx.text()
                parametros["poder_diastatico"] =  self.poder_diastatico_malte_tbx.text()
                parametros["proteina"] =  self.proteina_malte_tbx.text()
                parametros["observacoes"] =  str(self.observacoes_malte_tbx.toPlainText()).strip('()').replace(',','')
                if self.usar_mostura_malte_cbx.isChecked() == True:
                    parametros["usar_mostura"] = True
                else:
                    parametros["usar_mostura"] = False
                if self.usar_fervura_malte_cbx.isChecked():
                    parametros["usar_fervura"] = True
                else:
                    parametros["usar_fervura"] = False
                if self.nao_fermentavel_malte_cbx.isChecked():
                    parametros["nao_fermentavel"] = True
                else:
                    parametros["nao_fermentavel"] = False
                parametros["aproveitamento"] =  self.aproveitamento_malte_tbx.text()
                print(db.salvar_info('malte', parametros))
            elif self.cadastro_tabw.currentIndex() == 1: #Adjunto
                parametros = {}
                if self.gv_id_adjunto != 0:
                    parametros["id_adjunto"] =  self.gv_id_adjunto
                parametros["nome"] =  self.descricao_adjunto_tbx.text()
                parametros["tipo"] =  self.tipo_adjunto_cb.currentText()
                parametros["fabricante"] =  self.fabricante_adjunto_tbx.text()
                parametros["max_litro"] =  self.maximo_por_litro_adjunto_tbx.text()
                parametros["preco"] =  self.preco_adjunto_tbx.text()      
                parametros["indicacao_breve"] =  self.indicacao_breve_adjunto_tbx.text()          
                parametros["observacoes"] =  str(self.observacoes_adjunto_tbx.toPlainText()).strip('()').replace(',','')
                print(db.salvar_info('adjunto', parametros))

            elif self.cadastro_tabw.currentIndex() == 2: #Levedura
                pass

                parametros = {}
                if self.gv_id_levedura != 0:
                    parametros["id_levedura"] =  self.gv_id_levedura
                parametros["nome"] =  self.descricao_levedura_tbx.text()

                parametros["sigla"] =  self.sigla_levedura_tbx.text()	
                parametros["laboratorio"] =  self.laboratorio_levedura_tbx.text()	
                parametros["preco"] =  self.preco_levedura_tbx.text()	
                parametros["formato"] =  self.formato_levedura_cb.currentText	
                parametros["floculacao"] =  self.floculacao_levedura_cb.currentText()
                parametros["viabilidade"] =  self.viabilidade_levedura_tbx.text()	
                parametros["gramas_pacote"] =  self.gramas_unidade_levedura_tbx.text()	
                parametros["cebulas_bilhoes_unidade"] =  self.celulas_por_pacote_levedura_tbx.text()	
                parametros["atenuacao_max"] =  self.atenuacao_maxima_levedura_tbx.text()	
                parametros["atenuacao_min"] =  self.atenuacao_minima_levedura_tbx.text()	
                parametros["temperatura_max"] =  self.temperatura_maxima_levedura_tbx.text()	
                parametros["temperatura_min"] =  self.temperatura_minima_levedura_tbx.text()

                if self.ale_levedura_cbx.isChecked() == True:
                    parametros["familia"] = True
                else:                	
                    parametros["familia"] = False

                parametros["observacoes"] =  str(self.observacoes_levedura_tbx_tbx.toPlainText()).strip('()').replace(',','')
                print(db.salvar_info('levedura', parametros))

            elif self.cadastro_tabw.currentIndex() == 3: #Lupulo
                parametros = {}
                if self.gv_id_luplulo != 0:
                    parametros["id_lupulo"] =  self.gv_id_lupulo
                parametros["nome"] =  self.descricao_lupulo_tbx.text()
                parametros["origem"] =  self.origem_lupulo_tbx.text()
                parametros["fabricante"] =  self.fabricante_lupulo_tbx.text()
                parametros["tipo"] =  self.tipo_lupulo_tbx.currentText()
                parametros["formato"] =  self.formato_lupulo_tbx.currentText()
                parametros["preco"] =  self.preco_lupulo_tbx.text()
                parametros["acido_alfa"] =  self.acido_alfa_lupulo_tbx.text()
                parametros["acido_beta"] =  self.acido_beta_lupulo_tbx.text()
                parametros["observacoes"] =  str(self.observacoes_lupulo_tbx.toPlainText()).strip('()').replace(',','')
                print(db.salvar_info('lupulo', parametros))
    ####################################################################
    #Final Salvar         