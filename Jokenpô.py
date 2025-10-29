import random, os

print("Seja Bem-vindo ao Jokenpô")

player_points = 0
machine_points = 0

options = ["r", "p", "t"]

while True:
    startJokepo = input("Deseja jogar SIM[S] N[NÃO]")

    if startJokepo.upper() == "S":
        os.system("cls")
        player_choice = input("Escolha R(PEDRA) P(PAPEL) T(TESOURA)").lower().strip()

        if player_choice not in options:
            print("Escolha inválida! Por favor, digite R, P ou T.")
            continue 
        
        machine_choice = random.randint(0,2)
        machine_options = options[machine_choice]

        print(f'O computador escolheu {machine_options}')

    
        if player_choice == machine_options:
            os.system("cls")
            print("EMPATE!!🚨")
        elif player_choice == "r" and machine_options == "t":
            os.system("cls")
            print("PEDRA GANHA DA TESOURA. VOCÊ GANHOU! 🏆")
            player_points += 1 

        elif player_choice == "p" and machine_options == "r":
            os.system("cls")
            print("VOCÊ GANHOU! PAPEL GANHA DA PEDRA 🏆")
            player_points += 1

        elif player_choice == "t" and machine_options == "p":
            os.system("cls")
            print("VOCÊ GANHOU! TESOURA GANHA DO PAPEL 🏆")
            player_points += 1

        else: 
            os.system("cls")
            print("VOCÊ PERDEU! ❌")
            machine_points += 1

    elif startJokepo.upper() == "N":
        break
    else:
        os.system("cls")
        print("Opção inválida. Por favor, digite S ou N.")

os.system("cls")
print(f'Sua pontuação é de {player_points}')
print(f'Pontuação da máquina é de {machine_points}')

if player_points > machine_points:
    print("PARÁBENS VOCÊ GANHOU! 🏆")
elif player_points == machine_points: 
    print("EMPATE! 🚨")
else:
    print("DERROTA!❌")