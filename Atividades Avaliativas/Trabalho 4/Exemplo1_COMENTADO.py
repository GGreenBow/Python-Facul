'''
  Exemplo que será usado
  para elaboração do trabalho de algoritmos
'''
from tkinter import *
'''importa todas as funções da biblioteca "tkinter" para o Python'''
  
class Aplicacao:
    '''Cria a classe Aplicacao'''
    def __init__(self, janela):
        '''Define a variavel "__init__" com os parametros "self" e "janela" '''


        janela.title('Calculadora')
        '''Define o título da janela'''
        self.fontePadrao = ("Arial", "12")
        '''Define a fonte padrão como Arial tamanho 12'''
        self.primeiroContainer = Frame(janela)
        '''Cria um área a ser determinada para o parametro "janela"'''
        self.primeiroContainer["pady"] = 10
        '''Determina o tamanho vertical do primeiro container'''
        self.primeiroContainer.pack()
        '''Posiciona o primeiro container dentro do Frame da janela'''
        
        self.segundoContainer = Frame(janela)
        '''Cria um área a ser determinada para o parametro "janela"'''
        self.segundoContainer["padx"] = 20
        '''Determina o tamanho horizontal do segundo container'''
        self.segundoContainer.pack()
        '''Posiciona o segundo container dentro do Frame da janela'''
  
        self.terceiroContainer = Frame(janela)
        '''Cria um área a ser determinada para o parametro "janela"'''
        self.terceiroContainer["padx"] = 20
        '''Determina o tamanho horizontal do terceiro container'''
        self.terceiroContainer.pack()
        '''Posiciona o terceiro container dentro do Frame da janela'''
  
        self.quartoContainer = Frame(janela)
        '''Cria um área a ser determinada para o parametro "janela"'''
        self.quartoContainer["pady"] = 10
        '''Determina o tamanho vertical do quarto container'''
        self.quartoContainer.pack()
        '''Posiciona o quarto container dentro do Frame da janela'''

        self.quintoContainer = Frame(janela)
        '''Cria um área a ser determinada para o parametro "janela"'''
        self.quintoContainer["pady"] = 10
        '''Determina o tamanho vertical do quinto container'''
        self.quintoContainer.pack()
        '''Posiciona o quinto container dentro do Frame da janela'''
        
        self.titulo = Label(self.primeiroContainer, text="Soma dois valores")
        '''Cria o texto "Soma dois valores" que ficará em cima das caixas de entrada'''
        self.titulo["font"] = ("Arial", "12", "bold")
        '''Define a fonte/tamanho do texto criado acima'''
        self.titulo.pack()
        '''Posiciona o texto para cima dentro da janela do programa'''
  
        self.n1Label = Label(self.segundoContainer,text="Número 1", font=self.fontePadrao)
        '''Cria o texto "Número1" que ficará do lado da primeira caixa de entrada, e ja define qual seu estilo de fonte e tamanho'''
        self.n1Label.pack(side=LEFT)
        '''Posiciona o texto ao lado esquerdo da janela'''
  
        self.n1 = Entry(self.segundoContainer)
        '''Cria uma caixa de entrada dentro da área do segundo container'''
        self.n1["width"] = 10
        '''Define o comprimento da caixa de entrada'''
        self.n1["font"] = self.fontePadrao
        '''Define a fonte do que será escrito na caixa de entrada'''
        self.n1.pack(side=LEFT)
        '''Posiciona a caixa de entrada ao lado esquerdo da janela'''
  
        self.n2Label = Label(self.terceiroContainer, text="Número 2", font=self.fontePadrao)
        '''Cria o texto "Número2" que ficará do lado da segunda caixa de entradae, e ja define qual seu estilo de fonte e tamanho'''
        self.n2Label.pack(side=LEFT)
        '''Posiciona o texto ao lado esquerdo da janela'''
  
        self.n2 = Entry(self.terceiroContainer)
        '''Cria uma caixa de entrada dentro da área do terceiro container'''
        self.n2["width"] = 10
        '''Define o comprimento da caixa de entrada'''
        self.n2["font"] = self.fontePadrao
        '''Define a fonte do que será escrito na caixa de entrada'''
        self.n2.pack(side=LEFT)
        '''Posiciona a caixa de entrada ao lado esquerdo da janela'''
  
        self.ok = Button(self.quartoContainer)
        '''Cria um botão dentro da área do quarto container'''
        self.ok["text"] = "Somar"
        '''Define o texto "Somar" dentro do botão'''
        self.ok["font"] = ("Arial", "10")
        '''Define a fonte e o tamanho do texto do botão'''
        self.ok["width"] = 12
        '''Define o comprimento do botão'''
        self.ok["command"] = self.soma
        '''Executa a função de soma criada posteriormente'''
        self.ok.pack()
        '''Posiciona o botão de soma centralizadamente dentro da janela'''


        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        '''Define o texto do resultado que aparecerá embaixo do botão de soma'''
        self.mensagem.pack()
        '''Posiciona o texto centralizadamente dentro da janela'''
        
        self.sair = Button(self.quintoContainer)]
        '''Cria um botão dentro da área do quinto container'''
        self.sair["text"] = "Sair"
        '''Define o texto "Sair" dentro do botão'''
        self.sair["font"] = ("Arial", "10")
        '''Define a fonte e o tamanho do texto do botão'''
        self.sair["width"] = 12
        ]'''Define o comprimento do botão'''
        self.sair["command"] = self.saida
        '''Executa a função de sair do programa criada posteriormente'''
        self.sair.pack()
        '''Posiciona o botão de sair centralizadamente dentro da janela'''
  
    #Método para somar os valores
    def soma(self):
        '''Define a função de soma'''
        num1 = self.n1.get()
        '''Chama a variável escrita na primeira caixa de entrada'''
        num1=int(num1)
        '''Define a variável como um número inteiro'''
        num2 = self.n2.get()
        '''Chama a variável escrita na segunda caixa de entrada'''
        num2=int(num2)
        '''Define a variável como um número inteiro'''
        result=(num1+num2)
        '''Cria uma variável de resultado que é equivalente a soma das duas variáveis anteriores'''
        self.mensagem["text"] = '%d' %(result)
        '''Cria o objeto para imprimir o resultado'''
    #Método para finalizar a janela (fechar a janela)
    def saida(self):
        '''Define a função de saída'''
        app.destroy()
        '''Cria um objeto que fecha a aplicação'''

app = Tk()
'''Cria variável App para instanciar a classe Tk'''
Aplicacao(app)
'''Passa tudo criado na classe aplicação para a variável app'''
app.mainloop()
'''Deixa o programa rodando até a pessoa clicar no botão de sair'''
