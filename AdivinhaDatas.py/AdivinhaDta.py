import json
import random
import os

print("Bem-Vindo(a) ao meu jogo de Adivinhar data!😃")

try:
    with open("word.json", encoding="utf8") as f:
        dates_game = json.load(f)
except FileNotFoundError:
    print("Erro: O arquivo 'word.json' não foi encontrado.")
    exit()

while True:
    start_Game = input("\nVocê deseja jogar Sim[S] Não[N]? ").strip().upper()
    
    if start_Game == "N":
        print("Até a próxima! Volte quando quiser adivinhar uma data. 👋")
        break
    
    elif start_Game == "S":
        game_Theme = input("Digite o tema Mundo[M] Entretenimento[E]: ").strip().upper()
        
        if game_Theme == "M":
            name_category = "Mundo"
        elif game_Theme == "E":
            name_category = "Entretenimento"
        else:
            print("Opção de tema Inválida! Tente novamente.")
            continue

        os.system("cls") 
        #PEGANDO A DICA ALEATORIA NO ARQUIVO JSON
        lista_eventos = dates_game[name_category]
        
        evento_sorteado = random.choice(lista_eventos)
        pergunta = evento_sorteado['evento']
        resposta_correta = evento_sorteado['data']

        print(f"\n--- Tema: {name_category} ---")
        print(f"Qual a data do seguinte evento: {pergunta}")
        
        number_choice = 5
        
        # INÍCIO DO SISTEMA DE TENTATIVAS
        while number_choice > 0:
            resposta_usuario = input(f"Tentativas restantes ({number_choice}): Sua resposta (DD/MM/AAAA): ").strip()
            
            if resposta_usuario == resposta_correta:
                print("\n🎉 Parabéns! Você acertou a data!")
                break 
            
            number_choice -= 1
            
            if number_choice > 0:
                os.system("cls")
                print("❌ Resposta incorreta. Tente novamente.")
        
        # VERIFICA SE O JOGADOR PERDEU POR FALTA DE TENTATIVAS
        if number_choice == 0 and resposta_usuario != resposta_correta:
            print("\n❌ Suas tentativas acabaram!")
            print(f"A data correta era: {resposta_correta}")
            
    else:
        print("Opção inválida. Digite S para Sim ou N para Não.")