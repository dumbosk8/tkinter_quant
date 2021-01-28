import pandas as pd
import yfinance as yf
from statsmodels.tsa.stattools import coint
from tkinter import *
from tkinter.ttk import *


tickers_setores = pd.read_csv('https://raw.githubusercontent.com/dumbosk8/tkinter_quant/main/setores_tickers.csv') #IMPORTAÇÃO DOS SETORES E DOS TICKERS ATRAVES DE UM ARQUIVO CSV QUE COLOQUEI NO MEU GITHUB

setores = list(tickers_setores['SETOR'].unique()) #SETORES DO IBOVESPA
tickers = list(tickers_setores['TICKER']) #TICKERS DO IBOVESPA

data = yf.download(tickers, start = '2020-10-01', end = '2021-01-23') #IMPORTAÇÃO DOS DADOS VIA BIBLIOTECA DO YAHOO FINANCE
data = data['Close']

def find_coint_pairs(papel1, papel2): #FUNÇÃO PARA ENCONTRAR O PVALOR DO RESÍDUO DA COINTEGRAÇÃO 
    S1 = data[str(papel1)] #SELCIONA O ATIVO 1, VEJA QUE POSSUI UM OBJETO QUE É UMA LACUNA(COMBOBOX) A PARTIR DA BIBLIOTECA TKINTER
    S2 = data[str(papel2)] #SELECIONA O ATIVO 2
    result = coint(S2, S1) #COINTEGRA OS DOIS ATIVOS USANDO A BIBLIOTECA STATSMODELS E ARMAZENA DENTRO DO OBJETO result OS RESULTADOS DA COINTEGRAÇÃO
    pvalue = result[1] #UM DOS RESULTADOS É O PVALOR QUE É ARMAZENADO NESSE OBJETO DE MESMO NOME
    lbl = Label(window, text="") #ESTE É O CAMPO ONDE O PVALOR IRÁ SER EXIBIDO NA JANELA, AQUI EU CRIEI O OBJETO LBL
    lbl.grid(column = 8, row = 3) #NESSA LINHA EU POSICIONEI O OBJETO
    lbl.configure(text = pvalue) #AQUI CONFIGUREI PRO TEXTO A SER EXIBIDO SER O RESULTADO DO PVALOR

window = Tk() #AQUI COMEÇA A ESTRUTURA DO FRONTEND, UTILIZANDO A BIBLIOTECA TKINTER
window.title("PAIR TRADING") # DEI O NOME PARA A JANELA
papel1 = Combobox(window,width=10) #CRIEI A COMBOBOX PARA EXIBIR OS PAPEIS
papel2 = Combobox(window,width=10) #A COMBOBOX DO PAPEL 2
papel1.grid(column = 1, row = 2) #POSICIONAMENTO DA COMBOBOX1
papel2.grid(column = 1, row = 3) #POSICIONAMENTO DA COMBOBOX2
papel1['values']= tickers #CONTEUDO DAS COMBOBOX
papel2['values']= tickers #CONTEUDO DAS COMBOBOX
papel1.current(2) #ATIVO 1 A SER INICIADO NA COMBOBOX
papel2.current(1) #ATIVO 2 A SER INICIADO NA COMBOBOX


window.geometry('350x200') #TAMANHO DA JANELA



def clicked(): #FUNÇÃO DO BOTAO PARA MOSTRAR O PVALOR
    find_coint_pairs(papel1 = papel1.get(), papel2 = papel2.get()) #MINHA FUNÇÃO POSSUI DOIS PARAMETROS, COLOQUEI OS DOIS PARA SEREM AS PROPRIA COMBOBOX ATRAVES DO ATRIBUTO get()

btn = Button(window, text="Cointegrar", command = clicked) #CRIAÇÃO DO BOTÃO DE COINTEGRAÇÃO, OBSERVEM OS PARAMETROS, EM command COLOQUEI A FUNÇÃO CLICKED

btn.grid(column = 1, row = 4) #POSICIONAMENTO DO BOTÃO

window.mainloop() #FINAL DA ESTRUTURA DE FRONTEND DO TKINTER
