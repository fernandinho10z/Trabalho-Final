import curses
from modulo.banco import Banco
import sys

class Chat():

    def __init__(self):
        self.tela = curses.initscr()    

    def mostrar_mensagens(self):
        try:
            banco = Banco()
            busca = banco.filtrar_mensagens()
            self.tela.clear()            
            for item in busca:
                self.tela.addstr("%s %s: %s\n" %(item['hora'], item ['nome'], item ['mensagem']))
            
        except KeyboardInterrupt as e:
            curses.endwin()
            sys.exit()
     
    def enviar_mensagem(self, nome):
        try:
            self.tela.addstr("Mensagem: ")
            msg = self.tela.getstr().decode(encoding="utf-8")
            self.tela.clear() #limpar a tela            
            banco = Banco()
            banco.add_mensagem (nome = nome, mensagem = msg)
            

        except KeyboardInterrupt as e: #KeyboardInterrupt é um ctrl + C
            curses.endwin()
            sys.exit()




'''
while  True:
    tela = curses.initscr() #trava a tela
    nome = tela.getstr() #verifica o que esta digitando
    tela.addstr(nome) #adiciona o que digitou na tela

reset
'''

if __name__ == '__main__':
    try:
        nome = input('Digite seu nome: ')
        iniciar = Chat()
        while True:
            iniciar.mostrar_mensagens()
            iniciar.enviar_mensagem(nome)
    except KeyboardInterrupt as e: #KeyboardInterrupt é um ctrl + C
            curses.endwin()
            sys.exit()
