from pymongo import MongoClient, DESCENDING
import time

class Banco():

    def __init__(self):
        self.client = MongoClient('127.0.0.1')
        self.db = self.client['chat']

    def add_mensagem(self,**kwargs):
        self.db.mensagens.insert({"nome":kwargs['nome'],
                                  "mensagem":kwargs['mensagem'],
                                  "hora":str(time.strftime('%d-%m-%Y %H:%M:%S'))})

    def filtrar_mensagens(self):
        lista = []
        for mensagem in self.db.mensagens.find().sort("hora"), DESCENDING.limit(30):
            lista.append(mensagem)
            lista.reverse()
        return lista
        

if __name__ == '__main__':
    banco = Banco()
    banco.add_mensagem (nome='Fernando', mensagem='Oi')
    banco.filtrar_mensagens ()
