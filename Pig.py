import random

def dice():
    min_num = 1
    max_num = 6
    rand_num = random.randint(min_num, max_num)

    return rand_num

while True:
    print("----------------------------------------------------------\n")
    player_num = input("Selecciona la cantidad de jugadores (2-4): ")

    if player_num.isdigit():
        player_num = int(player_num)

        if player_num >= 2 and player_num <= 4:
            break

        else:
            print("\nDebe ser un numero entre 2 - 4")
    else:
        print("\nInvalido, intente nuevamente.\n")

print(f"\nPerfecto!! son {player_num} jugadores")
print("***************************************************************\n")

final_score = 50
dict_scores = {}

while True:
    for i in range(player_num):
        print(f"Player #{str(i + 1)}:\n")
        input("Do you want to roll the dice? (y/n): ")

