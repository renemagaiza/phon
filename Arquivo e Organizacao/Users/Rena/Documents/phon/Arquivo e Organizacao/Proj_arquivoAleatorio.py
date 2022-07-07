#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
# Programa gerador de arquivos aleatorios de provas
"""
Eis o que o programa faz:
• Cria 35 provas diferentes.
• Cria 50 perguntas de múltipla escolha para cada prova em ordem aleatória.
• Fornece a resposta correta e três respostas incorretas aleatórias para cada
pergunta em ordem aleatória.
• Grava as provas em 35 arquivos-texto.
• Grava os gabaritos contendo as respostas em 35 arquivos-texto.
Isso significa que o código deverá fazer o seguinte:
• Armazenar os estados e suas capitais em um dicionário.
• Chamar open(), write() e close() para os arquivos-texto contendo as provas e
os gabaritos com as respostas.
• Usar random.shuffle() para deixar a ordem das perguntas e as opções de
múltipla escolha aleatórias.
"""
import random
# Os dados para as provas. As chaves são os estados e os valores são as capitais.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia':
'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky':
'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska':
'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'NorthDakota':
'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon':
'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina':
'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington':
'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# Gera 35 arquivos contendo as provas.
# TODO: Cria os arquivos com as provas e os gabaritos das respostas.
# TODO: Escreve o cabeçalho da prova.
# TODO: Embaralha a ordem dos estados.
# TODO: Percorre todos os 50 estados em um loop, criando uma pergunta para cada um.
for quizNum in range(35):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    # Escreve o cabeçalho da prova.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    # Embaralha a ordem dos estados.
    states = list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(50):
        #Obtém respostas corretas e incorretas.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        # TODO: Grava a pergunta e as opções de resposta no arquivo de prova.
        # TODO: Grava o gabarito com as respostas em um arquivo.
        # Grava a pergunta e as opções de resposta no arquivo de prova.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        # Grava o gabarito com as respostas em um arquivo.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
