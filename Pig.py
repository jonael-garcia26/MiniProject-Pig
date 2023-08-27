import random

def dice():
    min_num = 2
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

final_score = 50
dict_scores = {}

#****************************BROKEN CODE******************************
while True:
    for i in range(player_num):
        print("------------------------------------------------------------")
        print(f"\nJugador #{str(i + 1)}:\n")
        dice_roll = str.strip(str.lower(input("Quieres tirar el dado? (y/n): ")))
        player_score = 0
        
        if dice_roll == "n":
            continue
        if dice_roll == "y":
            dice_num = dice()
            print("\n" + dice_num)
            if dice_num == 1:
                player_score = 0
            else:
                dict_scores[f"Jugador #{str(i + 1)}"] = dice_num
                print(dict_scores)

#***************************TEST CODE***************************************

# x = 4
# for i in range(x):
#     print(i)
#     if f"{i}" == f"{range(x)[-1]}":