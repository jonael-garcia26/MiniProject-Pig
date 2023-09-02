import random
import time

def dice():
    min_num = 1
    max_num = 6
    rand_num = random.randint(min_num, max_num)

    return rand_num

final_score = 50
players_list = []
cicle = 0

def scoreboard():
    print("\n\nSCORE BOARD:")
    for i in players_list:
        print(f"Jugador #{i[0]}: {i[1]} pts.")

while True:
    print("----------------------------------------------------------\n")
    player_num = input("Selecciona la cantidad de jugadores (2-4): ")

    if player_num.isdigit():
        player_num = int(player_num)

        if player_num >= 2 and player_num <= 4:

            for i in range(player_num):
                players_list.append([i + 1, 0])

            break

        else:
            print("\nDebe ser un numero entre 2 - 4")
    else:
        print("\nInvalido, intente nuevamente.\n")

print(f"\nPerfecto!! son {player_num} jugadores")
time.sleep(1)

while True:

    for i in players_list:
        if i[1] >= final_score:
            print(f"\nEl JUGADOR #{i[0]} GANA")
            scoreboard()
            time.sleep(5)
            exit()

    if cicle >= player_num:
        cicle = 0
    print("\n-------------------------------------------------\n")
    print(f"turno del Jugador #{players_list[cicle][0]}\n")
    score = 0

    while True:
        play = str.strip(str.lower(input("\nQuieres tirar el dado? (y/n) ")))

        if play != "y":
            players_list[cicle][1] += score
            break
        else:
            num = dice()
            print(f"El dado saco un {num}\n")

            if num != 1:
                score += num
                if score >= final_score:
                    players_list[cicle][1] += score
                    print(f"\nEl JUGADOR #{players_list[cicle][0]} GANA")
                    scoreboard()
                    time.sleep(5)
                    exit()
                print(f"Puntuacion por turno: {score}\n")

            else:
                score = 0
                print("oh! Perdiste tus puntos y turno")
                break

    scoreboard()
    cicle += 1
