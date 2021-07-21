import turtle # Chama a biblioteca turtle
turtle.shape("turtle") # Escolher qual formato a caneta vai receber, como se fosse o ponteiro do mouse
turtle.speed(5) # Escolhe a velocidade que a caneta se moverá


turtle.penup() # Desativando a caneta para que não apareça o desenho do caminho percorrido enquanto a posiciono no lugar certo

# Posicionando a caneta no lugar que quero que o desenho comece a ser construído
turtle.right(90) # Escolhendo o ângulo de 90 graus para direita para que a caneta possa virar sua direção para baixo
turtle.forward(200) # Indicando o número de pixel que ela deve "andar" para frente
turtle.left(90) # Escolhendo o ângulo de 90 graus para esquerda para que a caneta possa voltar para direção que estava, ou seja, voltará estar direcionada para esquerda

turtle.pendown() # Ativando a caneta para que agora apareça o desenho do caminho percorrido



# Cor para a casa
turtle.fillcolor("dark gray") # Escolhendo a cor que vai ser usada para preencher o desenho da casa, neste caso um tipo de cinza
turtle.begin_fill() # Ativando o preenchimento do desenho a partir deste ponto

# Começando o desenho da casa
turtle.forward(100) # Com a caneta apontada para a esquerda o desenho começa a avançar 100 pixels para começar a base do quadrado 
turtle.left(90) # Como o formato da casa é um quadrado seus ângulos são de 90º, então mudo a direção para 90º para poder desenhar a primeira linha vertical
turtle.forward(200) # Desenhando a primeira linha vertical 
turtle.left(90) # Como o formato da casa é um quadrado seus ângulos são de 90º, então mudo a direção para 90º para poder desenhar a segunda linha horizontal
turtle.forward(200) # Desenhando a segunda linha horizontal
turtle.left(90) # Como o formato da casa é um quadrado seus ângulos são de 90º, então mudo a direção para 90º para poder desenhar a segunda linha vertical
turtle.forward(200) # Desenhando a segunda linha vertical 
turtle.left(90)# Como o formato da casa é um quadrado seus ângulos são de 90º, então mudo a direção para 90º para poder finalizar o quadrado
turtle.forward(100) # Completando o desenho da base 

# Terminando de desenhar a casa
turtle.end_fill() # Definindo que o preenchimento do desenho deve ser feito até este ponto



turtle.penup()# Desativando a caneta para que não apareça o desenho do caminho percorrido enquanto a posiciono no lugar certo

# Posicionando a caneta
turtle.forward(100) # Definindo os pixels que a caneta andará para ir de volta para a lateral do quadrado e assim poder subir para construção do teto
turtle.left(90) # Definindo o ângulo para direcionar e assim poder voltar com a caneta para a parte superior da casa
turtle.forward(200) # Definindo os pixels que a caneta andará para ir de volta para a parte superior e assim poder começar a construir o teto

turtle.pendown() # Ativando a caneta para que agora apareça o desenho do caminho percorrido



# Cor para o teto
turtle.fillcolor("dark orange") # Escolhendo a cor que vai ser usada para preencher o desenho do teto
turtle.begin_fill() # Ativando o preenchimento do desenho a partir deste ponto

# Começando o desenho do teto
turtle.left(30) # Definindo o ângulo para direcionar a caneta, 30º pois a caneta está posicionada para cima então é só necessário 30º para a poicionar
turtle.forward(200) # Definindo os pixels que a caneta andará para começar o desenho do teto
turtle.left(120) # Definindo o ângulo para direcionar a caneta, 120º pois um triângulo equilátero tem suas retas separadas por 60º,
                #porém é preciso dobrar para direcionar para posição certa
turtle.forward(200) # Definindo os pixels que a caneta andará para terminar o desenho do teto
turtle.left(120) # Definindo o ângulo para direcionar a caneta, 120º pois um triângulo equilátero tem suas retas separadas por 60º,
                #porém é preciso dobrar para direcionar para posição certa
turtle.forward(200) # Definindo os pixels que a caneta andará para voltar para lateral do topo

# Terminando de desenhar o teto
turtle.end_fill() # Definindo que o preenchimento do desenho deve ser feito até este ponto



turtle.penup() # Desativando a caneta para que não apareça o desenho do caminho percorrido enquanto a posiciono no lugar certo

# Posicionando a caneta
turtle.left(-90) # Definindo o ângulo para direcionar e assim poder voltar com a caneta para a base para o próximo passo
turtle.forward(200) # Definindo os pixels que a caneta andará para descer de volta para a base
turtle.left(-90) # Definindo o ângulo para direcionar e assim poder voltar com a caneta para a região correta da base para o próximo passo
turtle.forward(75)  # Definindo os pixels que a caneta andará na base para ir ao lugar do começo do próximo passo

turtle.pendown()# Ativando a caneta para que agora apareça o desenho do caminho percorrido



# Cor para a porta
turtle.fillcolor("saddle brown") # Escolhendo a cor que vai ser usada para preencher o desenho da porta
turtle.begin_fill() # Ativando o preenchimento do desenho a partir deste ponto
# Começando o desenho da porta
turtle.left(-90) # Definindo o ângulo para direcionar a caneta para cima
turtle.forward(75) # Definindo os pixels que a caneta andará para marcar a primeira linha vertical da porta
turtle.left(90) # Definindo o ângulo para direcionar a caneta para direita
turtle.forward(50) # Definindo os pixels que a caneta andará para marcar a primeira linha horizontal da porta
turtle.left(90) # Definindo o ângulo para direcionar a caneta para baixo
turtle.forward(75) # Definindo os pixels que a caneta andará para marcar a segunda linha vertical da porta
# Terminando de desenhar a porta
turtle.end_fill() # Definindo que o preenchimento do desenho deve ser feito até este ponto



