'''
  Exemplo que será usado
  para elaboração do trabalho de algoritmos
'''
from tkinter import *
  
class Aplicacao:
    def __init__(self, janela):


        janela.title('Calculadora')
        self.fontePadrao = ("Arial", "12")
        self.primeiroContainer = Frame(janela)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(janela)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(janela)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(janela)
        self.quartoContainer["pady"] = 10
        self.quartoContainer.pack()

        self.quintoContainer = Frame(janela)
        self.quintoContainer["pady"] = 10
        self.quintoContainer.pack()
        
        self.titulo = Label(self.primeiroContainer, text="Soma dois valores")
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo.pack()
  
        self.n1Label = Label(self.segundoContainer,text="Número 1", font=self.fontePadrao)
        self.n1Label.pack(side=LEFT)
  
        self.n1 = Entry(self.segundoContainer)
        self.n1["width"] = 10
        self.n1["font"] = self.fontePadrao
        self.n1.pack(side=LEFT)
  
        self.n2Label = Label(self.terceiroContainer, text="Número 2", font=self.fontePadrao)
        self.n2Label.pack(side=LEFT)
  
        self.n2 = Entry(self.terceiroContainer)
        self.n2["width"] = 10
        self.n2["font"] = self.fontePadrao
        self.n2.pack(side=LEFT)
  
        self.ok = Button(self.quartoContainer)
        self.ok["text"] = "Somar"
        self.ok["font"] = ("Arial", "10")
        self.ok["width"] = 12
        self.ok["command"] = self.soma
        self.ok.pack()


        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        
        self.sair = Button(self.quintoContainer)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Arial", "10")
        self.sair["width"] = 12
        self.sair["command"] = self.saida
        self.sair.pack()               
  
    #Método para somar os valores
    def soma(self):
        num1 = self.n1.get()
        num1=int(num1)
        num2 = self.n2.get()
        num2=int(num2)
        result=(num1+num2)
        self.mensagem["text"] = '%d' %(result)
    #Método para finalizar a janela (fechar a janela)
    def saida(self):
        app.destroy()

app = Tk()
Aplicacao(app)
app.mainloop()
