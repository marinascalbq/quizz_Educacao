import csv
import os
import random
import time
score = 0
nivel = ""
name = input('''  --------------------------------------------------------
           Olá, esse é um quiz sobre educação!
  ---------------------------------------------------------
Qual o Seu Nome?: ''')

def start():
  os.system("cls")
  

  print('''
  Esse quiz possui 3 assuntos com três niveis de difilcudades, você pode escolher das opções abaixo o que você quer fazer?
  Digite o número referente ao que quer fazer:
  ''')
  time.sleep(1)
  option1()


def option1():
  # Definindo as dificuldades do quiz
  menuInicial = int(input('''  1- Para escolher o nível fácil e jogar o quiz sobre Matemática
  2- Para escolher o nível médio e jogar o quiz sobre a Amazônia
  3- Para escolher o nível difícil e jogar o quiz sobre Paulo Freire 
  4- Para adicionar uma pergunta a um dos níveis do quiz
  5- Para remover uma pergunta do quiz
  0- Sair  
  '''))
  if menuInicial == 1:
    print("Ótima escolha, o primeiro degrau da escada é sempre o mais dificil. Vamos lá!")
    time.sleep(2)
    print("Quiz abrindo...")
    time.sleep(3)
    quizFacil()

  elif menuInicial == 2:
    print("Esse é o nível médio, teremos mais complexidade, está pronto? ")
    time.sleep(1)
    print("Vamos lá...")
    time.sleep(3)
    quizMedio()

  elif menuInicial == 3:
    print("WOW, você gosta de desafios ou já é um expert!")
    time.sleep(1)
    print("Quiz abrindo...")
    time.sleep(3)
    quizDificil()

  elif menuInicial == 4:
        os.system("cls")
        addQuestions()

  elif menuInicial == 5:
        os.system("cls")
        removeQuestion()

  elif menuInicial == 0:
        os.system("cls")
        print("Até a próxima! :)")

  else:
    print("Você digitou alguma coisa errada! :(")
    time.sleep(2)
    print("Por favor digite algumas das opções do menu.")
    option1()



def quizDificil():
  global score
#Abrindo o arquivo csv e lendo as perguntas
  with open('perguntasDificil.csv', 'r',) as csvfile:
    with open('arquivo_saida.csv', 'w') as csvSaida:

     linhas = csv.reader(csvfile, delimiter=',')
     linha = list(linhas)
     
#Imprimindo as questões e as alternativas
    for escolhida in linha:
      escolhida = random.choice(linha)
      question = escolhida[0]
      print('''{}'''.format(str(question)))
      alternativas = (escolhida[1],escolhida[2],escolhida[3],escolhida[4])
      time.sleep (2)
      print ('''
        {} 
        {}
        {}
        {}
        '''.format(alternativas[0], alternativas[1], alternativas[2], alternativas[3]))
      respostaCerta = escolhida[5]
      respostaJogador = input("Qual a resposta certa?").lower()
      time.sleep (1)
      print("A resposta certa é a",respostaCerta)
      if respostaJogador == respostaCerta:
        print("Você acertou!")
        time.sleep(1)
        score = score + 3
        print("Seu total de pontos é",score)
        print("Carregando....")
        time.sleep (2)
        
      else:
        print("Poxa, você errou, continue tentando!")
        time.sleep(1)
        print("Não tem problema errar, você também pode aprender com o erro.")
        time.sleep (1)
        print("Olhe os seus",score,"pontos e tente melhorar!")
        time.sleep (1)
        print("Você pode tentar ser melhor na próxima.")
        print("Continuando...")
        time.sleep (1)
  # Após 4 questões o jogo acaba e pergunta se quer começar de novo 
    print("Fim das questões")
    time.sleep (2)
    addRanking()

     # se o jogador fez mais que 12 pontos ele conclui a etapa mnais difícil do quiz      
    if score > 8:
      print("Parabéns!!! Você atingir a média de um expert!")
      time.sleep (2)
      print("Você somou",score,"pontos e podemos dizer que você já pode argumentar com pontos de vistas reais sobre a educação e suas teorias do conhecimento.")
      time.sleep (2)
      print("Até a próxima rodada :)")
      print("")

    option = int(input("Quer jogar outra outra vez ou sair? 1- Para jogar outra vez | 2- Para sair"))
    if option == 1:
      option1()
    elif option == 2:
      print("Tchau tchau...")
      print("")
    else:
      print("Você digitou alguma coisa errada! :(")
      time.sleep (1)
      print("Por favor digite 1 ou 2")
      option

def quizMedio():
  global score
#Abrindo o arquivo csv e lendo as perguntas
  with open('perguntasMedio.csv', 'r') as csvfile:
    with open('arquivo_saida.csv', 'w') as csvSaida:

     linhas = csv.reader(csvfile, delimiter=',')
     linha = list(linhas)
     
#Imprimindo as questões e as alternativas
    for escolhida in linha:
      escolhida = random.choice(linha)
      question = escolhida[0]
      print('''{}'''.format(question))
      alternativas = (escolhida[1],escolhida[2],escolhida[3],escolhida[4])
      time.sleep (2)
      print ('''
        {} 
        {}
        {}
        {}
        '''.format(alternativas[0], alternativas[1], alternativas[2], alternativas[3]))
      respostaCerta = escolhida[5]
      respostaJogador = input("Qual a resposta certa?").lower()
      time.sleep (1)
      print("A resposta certa é a",respostaCerta)
      if respostaJogador == respostaCerta:
        print("Você acertou!")
        time.sleep(1)
        score = score + 3
        print("Seu total de pontos é",score)
        print("Carregando....")
        time.sleep (2)
        
      else:
        print("Poxa, você errou, continue tentando!")
        time.sleep(1)
        print("Não tem problema errar, você também pode aprender com o erro.")
        time.sleep (1)
        print("Olhe os seus",score,"pontos e tente melhorar!")
        time.sleep (1)
        print("Você pode tentar ser melhor na próxima.")
        print("Continuando...")
        time.sleep (1)
  # Após 4 questões o jogo acaba e pergunta se quer começar de novo 
    print("Fim das questões")
    time.sleep (2)
  # se o jogador fez mais que 6 pontos o quiz pergunta se quer ir para outro nível        
    if score > 6:
      print("Parabéns!!! Você conseguiu passe livre para o próximo nível!")
      time.sleep (2)
      print("Você somou",score,"pontos")
      time.sleep (2)

    addRanking()

    option = int(input("Quer jogar outra rodada ou sair? 1- Para jogar outra | 2- Para sair"))
    if option == 1:
      option1()
    elif option == 2:
      print("Tchau tchau...")
      print("")
    else:
      print("Você digitou alguma coisa errada! :(")
      time.sleep (1)
      print("Por favor digite 1 ou 2")
      option
  


def quizFacil():
  global score
  score = 0
#Abrindo o arquivo csv e lendo as perguntas
  with open('perguntasFacil.csv', 'r') as csvfile:
    with open('arquivo_saida.csv', 'w') as csvSaida:

     linhas = csv.reader(csvfile, delimiter=',')
     linha = list(linhas)
     
#Imprimindo as questões e as alternativas
    for escolhida in linha:
      escolhida = random.choice(linha)
      question = escolhida[0]
      print('''{}'''.format(question))
      alternativas = (escolhida[1],escolhida[2],escolhida[3],escolhida[4])
      time.sleep (2)
      print ('''
        {} 
        {}
        {}
        {}
        '''.format(alternativas[0], alternativas[1], alternativas[2], alternativas[3]))
      respostaCerta = escolhida[5]
      respostaJogador = input("Qual a resposta certa?").lower()
      time.sleep (1)
      print("A resposta certa é a",respostaCerta)
      if respostaJogador == respostaCerta:
        print("Você acertou!")
        time.sleep(1)
        score = score + 3
        print("Seu total de pontos é",score)
        print("Carregando....")
        time.sleep (2)
        
      else:
        print("Poxa, você errou, continue tentando!")
        time.sleep(1)
        print("Não tem problema errar, você também pode aprender com o erro.")
        time.sleep (1)
        print("Olhe os seus",score,"pontos e tente melhorar!")
        time.sleep (1)
        print("Você pode tentar ser melhor na próxima.")
        print("Continuando...")
        time.sleep (1)
  # Após 4 questões o jogo acaba e pergunta se quer começar de novo 
    print("Fim das questões")
    time.sleep (2)
  # se o jogador fez mais que 6 pontos o quiz pergunta se quer ir para outro nível        
    if score > 6:
      print("Parabéns!!! Você conseguiu passe livre para o próximo nível!")
      time.sleep (2)
      print("Você somou",score,"pontos")
      time.sleep (2)
    addRanking()

    option = int(input("Quer jogar outra rodada ou sair? 1- Para jogar outra | 2- Para sair"))
    if option == 1:
      option1()
    elif option == 2:
      print("Tchau tchau...")
      print("")
    else:
      print("Você digitou alguma coisa errada! :(")
      time.sleep (1)
      print("Por favor digite 1 ou 2")
      option
  
    


def delete_line(filename, line_number):
    with open(filename, 'r', encoding='utf-8') as file:
      lines = file.readlines()

  
    if (line_number <= len(lines)):
      del lines[line_number - 1]
      with open(filename, "w") as file:
        for line in lines:
          file.write(line)

    else:
      print("Line", line_number, "not in file.")
      print("File has", len(lines), "lines.")

def removeQuestion():
   os.system("cls")
   question_file = int(input('''De qual destes quiz você gostaria de remover a pergunta?
    Digite:
    1- Fácil
    2- Médio
    3- Difícil
     '''))
  
   if question_file == 1:
        delete_filename = 'perguntasFacil.csv'
        archive = open(delete_filename)
        questions = csv.reader(archive)
        for question in questions:
          print('''{}
          '''.format(question))
        delete_line_number = int(input("Qual dessas questões deseja remover? Ex: Se quiser excluir a questão 1 digite 1: "))
        delete_line(delete_filename, delete_line_number)
        print('A pergunta', delete_line_number, 'foi deletada!')
        option = int(input("Quer voltar para o menu ou sair? 1- Voltar para o menu | 2- Sair"))
        if option == 1:
          option1()
        elif option == 2:
          print("Tchau tchau...")
          print("")
        else:
          print("Você digitou alguma coisa errada! :(")
          time.sleep (1)
          print("Por favor digite 1 ou 2")
          option
   elif question_file == 2:
        delete_filename = 'perguntasMedio.csv'
        archive = open(delete_filename)
        questions = csv.reader(archive)
        for question in questions:
          print('''{}
          '''.format(question))
        delete_line_number = int(input("Qual dessas questões deseja remover? Ex: Se quiser excluir a questão 1 digite 1: "))
        delete_line(delete_filename, delete_line_number)
        print('A pergunta', delete_line_number, 'foi deletada!')
        option = int(input("Quer voltar para o menu ou sair? 1- Voltar para o menu | 2- Sair"))
        if option == 1:
          option1()
        elif option == 2:
          print("Tchau tchau...")
          print("")
        else:
          print("Você digitou alguma coisa errada! :(")
          time.sleep (1)
          print("Por favor digite 1 ou 2")
          option

   elif question_file == 3:
        delete_filename = 'perguntasDificil.csv'
        archive = open(delete_filename)
        questions = csv.reader(archive)
        for question in questions:
          print('''{}
          '''.format(question))
        delete_line_number = int(input("Qual dessas questões deseja remover? Ex: Se quiser excluir a questão 1 digite 1: "))
        delete_line(delete_filename, delete_line_number)
        print('A pergunta', delete_line_number, 'foi deletada!')
        option = int(input("Quer voltar para o menu ou sair? 1- Voltar para o menu | 2- Sair"))
        if option == 1:
          option1()
        elif option == 2:
          print("Tchau tchau...")
          print("")
        else:
          print("Você digitou alguma coisa errada! :(")
          time.sleep (1)
          print("Por favor digite 1 ou 2")
          option
   else:
        print("Digite uma opção válida.")
        removeQuestion()  

def addQuestions():
    os.system("cls")
    question_level_add = int(input('''Você gostaria de adicionar questões de que nível?
    Digite:
    1- Fácil
    2- Médio
    3- Difícil
     '''))
    if question_level_add == 1:
      csvfile = open('perguntasFacil.csv', 'a', newline="\n")
    elif question_level_add == 2:
      csvfile = open('perguntasMedio.csv', 'a', newline="\n")
    elif question_level_add == 3:
      csvfile = open('perguntasDificil.csv', 'a', newline="\n")
    else:
      print("Escolha uma opção de adicionar válida.")
      addQuestions()

    question = input("Escreva aqui sua pergunta: ")
    answer1 = input('''Escreva aqui a primeira opção de alternativa:
    Ex.: a) Paulo freire
    ''')
    answer2 = input('''Escreva aqui a segunda opção de alternativa:
    Ex.: b) Isaac Newton
    ''')
    answer3 = input('''Escreva aqui a terceira opção de alternativa:
    Ex.: c) Albert Sabin
    ''')
    answer4 = input('''Escreva aqui a quarta opção de alternativa:
    Ex.: d) Nicolas Tesla
    ''')
    correctAnswer = input('''Agora escreva a letra da alternativa correta:
    Ex.: a
    ''')
    questions_and_answers = (question, answer1, answer2, answer3, answer4, correctAnswer)
    writer = csv.writer(csvfile)
    writer.writerow(questions_and_answers)
    print("Questão registrada. Obrigada!")
    time.sleep(3)
    csvfile.close()
    start()

def addRanking():
    os.system("cls")
    resp = "Olá jogador",name,"você fez",score,"!",
    csvfile = open('arquivo_saida.csv', 'a', encoding='utf-8', newline="")
    writer = csv.writer(csvfile)
    writer.writerow(resp)
    print("Pontuação Registrada no Ranking!")
    csvfile.close()


start()