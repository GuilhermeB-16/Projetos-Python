import os
print("Seja Bem-Vindo ao Quiz!😃")

questionMath =[
    {
        'Pergunta': 'Quanto é 52 X 2 ?',
        'Opções':['322', '104','124', '110'],
        'Resposta': 'B'
    },
    {
        'Pergunta': 'Quanto é 15 − 9?',
        'Opções':['2', '10','8', '6'],
        'Resposta': 'D'
    },

    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções':['2', '4','8', '6'],
        'Resposta': 'B'
    },
]
questionPort =[
    {
        'Pergunta': 'Qual é o plural da palavra “livro”📖?', 
        'Opções':['Livroes', 'Livras','Livros', 'Livrões'],
        'Resposta': 'C'
    },
    {   
        'Pergunta': 'Qual palavra é acentuada corretamente 👨🏽‍⚖️?', 
        'Opções':['Júri', 'Juri', 'Júrií', 'Jurí'],
        'Resposta': 'A'
    },
]
questionIglês =[
    {
        'Pergunta': 'Qual é a tradução de "cachorro quente" 🌭?', 
        'Opções':['Hot Dog', 'Warm Puppy', 'Heated Canine', 'Dog Food'],
        'Resposta': 'A'
    },
    {   'Pergunta': 'Qual verbo significa "nadar" 🏊‍♀️?', 
        'Opções':['Sleep', 'Run', 'Walk', 'Swim'],
        'Resposta': 'D'
    },
]

while True:
    qntdPontos = 0
    CHAVE_LETRA ='ABCDE'
    startQuiz = input("Você deseja jogar Sim[S] Não[N]" )
    os.system('cls')
    if startQuiz.upper() == 'S':
        opcaoMateria = input('Escolha uma matéria Português[P] Mátematica[M] Inglês[I]')
        os.system('cls')
        # CASO O JOGADOR ESCOLHA 'P' 
        if opcaoMateria.upper() == 'P':
            
            for questão in questionPort:
                print('\nPergunta:', questão['Pergunta']) 
        #EXIBI AS OPÇÕES PARA O JOGADOR ESCOLHER
                for i, opcao in enumerate(questão['Opções']):
                    letra = CHAVE_LETRA[i]
                    print(f'{letra}) {opcao}')

                respostaQuestion = input('ESCOLHA UMA OPÇÃO: ').strip().upper() 
        # VERIFICAR SE A RESPOSTA ESTÁ CORRETA
                if respostaQuestion == questão['Resposta']:
                    qntdPontos += 1
                    print('CERTA RESPOSTA ✅')
                else:
                    qntdPontos -= 1
                    print('RESPOSTA INCORRETA❌')

        elif opcaoMateria.upper() == 'M':
            
            for questão in questionMath:
                print('\nPergunta:', questão['Pergunta']) 
        #EXIBI AS OPÇÕES PARA O JOGADOR ESCOLHER
                for i, opcao in enumerate(questão['Opções']):
                    letra = CHAVE_LETRA[i]
                    print(f'{letra}) {opcao}')

                respostaQuestion = input('ESCOLHA UMA OPÇÃO: ').strip().upper() 
        # VERIFICAR SE A RESPOSTA ESTÁ CORRETA
                if respostaQuestion == questão['Resposta']:
                    qntdPontos += 1
                    print('CERTA RESPOSTA ✅')
                else:
                    qntdPontos -= 1
                    print('RESPOSTA INCORRETA❌')
        
        elif opcaoMateria.upper() == 'I':
            
            for questão in questionIglês:
                print('\nPergunta:', questão['Pergunta']) 
        #EXIBI AS OPÇÕES PARA O JOGADOR ESCOLHER
                for i, opcao in enumerate(questão['Opções']):
                    letra = CHAVE_LETRA[i]
                    print(f'{letra}) {opcao}')

                respostaQuestion = input('ESCOLHA UMA OPÇÃO: ').strip().upper() 
        # VERIFICAR SE A RESPOSTA ESTÁ CORRETA
                if respostaQuestion == questão['Resposta']:
                    qntdPontos += 1
                    print('CERTA RESPOSTA ✅')
                else:
                    qntdPontos -= 1
                    print('RESPOSTA INCORRETA❌')        
        else:
            print('Escolha uma Opção Válida')
            continue
    else:
        quit('Saindo')
    os.system('cls')
    print(f'Sua pontuação foi de {qntdPontos}😄')  
