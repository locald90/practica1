import random

def main():
    print("Добро пожаловать! Поговорите с глухой бабушкой.")
    print("Чтобы выйти, скажите ей «ПОКА» (заглавными).")
    print("-----------------------------------------------")

    while True:

        user_input = input("Вы: ").strip()


        if user_input == "ПОКА":
            print("Бабушка: ДО СВИДАНИЯ, МИЛЫЙ!")
            break


        if not user_input:
            print("Бабушка: ЧТО? Я НИЧЕГО НЕ СЛЫШУ!")
            continue


        if user_input.isupper():

            year = random.randint(1930, 1950)  # для разнообразия
            print(f"Бабушка: НЕТ, ТАК НЕЛЬЗЯ, С {year} ГОДА!")
        else:
            print("Бабушка: ЧТО? ГОВОРИ ГРОМЧЕ!")

if __name__ == "__main__":
    main()