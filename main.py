print ("Hello world" , 15) # Pokud chci vice datových typů v printu, musí

# Vytvoření proměnné (deklarace/inicializace)
cislo = 1 # Do proměnné číslo je uložná hodnota 1: datový typ Int

print("Druhý způsob s proměnou", cislo)

# Vytvoření proměnné s názvem text
text = "Zde je v proměnné uložený text" # Datový typ string

# Do konzole vypsiujeme obě proměné, oddělujeme čárkou
print(text, cislo)

# text - proměnná text vypíš co je v ní uložené
# cislo - proměnná vypíše číslo, který je v proměnné uložena

# Vytvoření vstupní hodnoty - Uživatel musí zadt hodnotu do terminálu
# následně se hodnota zadaná do terminálu uloží do proměnné
vstupni_promenna = input() # input() - Příkaz pro vstupní data

# input() - do závorek zapisujeme případnou zprávu pro uživatele, který se vypíše v terminálu

druha_vstupni_promenna = input("Zadejte číslo: ")

# print() nám vypíše do konzole, co uživatel zdal to inputu 
print(vstupni_promenna, druha_vstupni_promenna)