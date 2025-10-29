import random, os

print("Seja Bem-vindo(a) ao adivinha número 😃")

try:
    
    choice_number = input("Digite um número para começar: ").strip()
    choice_number_Int = int(choice_number)
    
    random_number = random.randint(0, choice_number_Int)
    
except ValueError:
    print("Error: o valor informado não é númerico!")
    exit()

number_kicks = 0
while True:
    try:
        
        guess_input = input("Chute um numero: ").strip()
        guess_number = int(guess_input) 
        
    except ValueError:
        print("Error: o valor informado não é númerico!")
        continue 

    number_kicks += 1 

    if guess_number == random_number:
        os.system("cls")
        print(f'Parabéns, você encontrou o número correto!🥳')
        print(f'Seu número de chutes foi {number_kicks}')
        break
    
    elif guess_number > random_number:
        print("Chutou alto! O número secreto é menor!") 
    elif guess_number < random_number:
        print("Chutou baixo! O número secreto é maior!") 