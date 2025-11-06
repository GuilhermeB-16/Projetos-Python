import json

f = open("aquarium.json", encoding="utf8")

data_aquarium = json.load(f)
# Assume que 'data_aquarium' é a fonte de dados.
# Extrai a lista principal de animais.
animals = data_aquarium["data"]

# Função auxiliar para o 'filter'.
# Retorna True apenas se o tipo do animal for "fish".
def verify_fish(animal):
    if animal["type"] == "fish":
        return True
    return False
    
# Filtra a lista completa para obter apenas os animais que são peixes.
animal_fish = list(filter(verify_fish, animals))



# Extrai e retorna o nome do animal.
def animal_name(animal):
    return animal["name"]

# Mapeia a lista de peixes para obter uma lista contendo apenas os seus nomes.
animal_fish_name = list(map(animal_name, animal_fish))

# Percorre a lista de animais e altera o número do tanque para os nomes selecionados.
def assing_to_tank(animals, names_selected, new_tank_number):
    # Função interna de mapeamento para modificar o número do tanque.
    def change_tank_number(animal):
        
        if animal["name"] in names_selected:
        
            animal["tank number"] = new_tank_number
        return animal
        
    # Aplica a mudança de tanque em todos os animais e retorna a nova lista.
    return list(map(change_tank_number, animals))

# Execução: move todos os peixes (animal_fish_name) para o tanque 42.
new_aquarium = assing_to_tank(animals, animal_fish_name, 42)

print(new_aquarium)